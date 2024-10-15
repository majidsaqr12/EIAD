from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, SubscriptionForm
from django.core.mail import send_mail
from django.conf import settings
from blogs import models

def index(request):
    latest_posts = models.Post.objects.order_by('-updated_at')[:3] 
    return render(request, 'pages/index.html', {'latest_posts': latest_posts})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_data = form.save()
            
            subject = f"New Contact Form Submission from {contact_data.name}"
            message = f"Name: {contact_data.name}\nEmail: {contact_data.email}\nPhone: {contact_data.phone}\nCompany: {contact_data.company}\nMessage: {contact_data.message}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            user_message = f"Hello {contact_data.name},\n\nThank you for contacting us! We have received your message and will get back to you soon.\n\nBest regards,\nYour Company Name"
            send_mail(
                "EIAD School",
                user_message,
                settings.EMAIL_HOST_USER,
                [contact_data.email],
                fail_silently=False,
            )
            
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

def success(request):
    return render(request, 'pages/success.html')

def our_campus(request):
    return render(request, 'pages/our_campus.html')

def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription_data = form.save()           
            subject_admin = f"New Subscription: {subscription_data.email}"
            message_admin = f"A new subscription has been submitted with the following email: {subscription_data.email}."
            send_mail(
                subject_admin,
                message_admin,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            user_message = f"Hello,\n\nThank you for subscribing to our newsletter! We will send updates to {subscription_data.email}.\n\nBest regards,\nEIAD Team"
            send_mail(
                "Subscription Confirmation",
                user_message,
                settings.EMAIL_HOST_USER,
                [subscription_data.email],  
                fail_silently=False,
            )
            
            return redirect('success')
    else:
        form = SubscriptionForm()

    return render(request, 'base.html', {'form': form})