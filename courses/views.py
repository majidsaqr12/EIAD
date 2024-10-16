from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Category
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings

def courses(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        all_courses = Course.objects.filter(category__name=selected_category)
    else:
        all_courses = Course.objects.all()

    # Paginate the courses
    paginator = Paginator(all_courses, 6)  # Show 6 courses per page
    page_number = request.GET.get('page')  # Get the page number from the request
    courses_page = paginator.get_page(page_number)  # Get the courses for the current page

    return render(request, 'courses/course.html', {
        'categories': categories,
        'courses': courses_page,  # Pass the paginated courses to the template
        'paginator': paginator,  # Pass the paginator to the template (if needed)
    })

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course-details.html', {'course': course})

def register_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.course = course
            registration.save()

            # Send email to admin
            subject = f"New Course Registration for {course.title}"
            message = f"User {registration.name} has registered for {course.title}.\nEmail: {registration.email}\nPhone: {registration.phone}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],  # Admin email from settings
                fail_silently=False,
            )

            # Send confirmation email to the user
            user_message = f"Hello {registration.name},\n\nThank you for registering for {course.title}.\nWe have received your registration and will get back to you soon.\n\nBest regards,\nYour Company Name"
            send_mail(
                "Course Registration Confirmation",
                user_message,
                settings.EMAIL_HOST_USER,
                [registration.email],  # User's email
                fail_silently=False,
            )

            return redirect('success')  # Replace with your success URL
    else:
        form = RegistrationForm()

    return render(request, 'courses/join_course.html', {'form': form, 'course': course})