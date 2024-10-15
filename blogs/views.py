from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category, Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

def archive(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category')
    tag = request.GET.get('tag')

    posts = Post.objects.all()

    if category_id:
        posts = posts.filter(category_id=category_id)

    if tag:
        posts = posts.filter(tags__name__icontains=tag)

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-updated_at')[:4]

    tags = Tag.objects.all()

    return render(request, 'blogs/archives.html', {
        'page_obj': page_obj,
        'categories': categories,
        'recent_posts': recent_posts,
        'tags': tags,
        'query': query,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    # Fetch related posts based on the same category
    related_posts = Post.objects.filter(category=post.category).exclude(pk=pk)[:5]

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()

            # Construct the post URL
            post_url = request.build_absolute_uri(reverse('post_detail', args=[post.pk]))
            delete_url = request.build_absolute_uri(reverse('delete_comment', args=[comment.id]))

            # Send email notification to admin
            send_mail(
                subject=f'New Comment on Post: {post.title}',
                message=(
                    f'Name: {comment.name}\n'
                    f'Email: {comment.email}\n'
                    f'Comment: {comment.content}\n'
                    f'Post: {post.title}\n'
                    f'Link: {post_url}\n\n'
                    f'To delete this comment, click the following link: {delete_url}'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blogs/single-blog.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'related_posts': related_posts
    })


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id  # Get the post ID before deleting the comment
    comment.delete()
    messages.success(request, 'Comment has been deleted.')
    return redirect('post_detail', pk=post_id)

def search_results(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    return render(request, 'pages/search_result.html', {'results': results, 'query': query})



def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blogs/category_detail.html', {'category': category, 'page_obj': page_obj})
