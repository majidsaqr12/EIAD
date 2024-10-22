from django.shortcuts import render, redirect, get_object_or_404
from .models import Program,  ProgramRegistration
from .forms import ProgramRegistrationForm
from django.conf import settings
from django.core.mail import send_mail


def program(request):
    programs = Program.objects.all()
    return render(request, 'programs/programs.html', {'programs': programs})

def register_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)

    if request.method == 'POST':
        form = ProgramRegistrationForm(request.POST)
        if form.is_valid():
            # Save the registration
            registration = ProgramRegistration.objects.create(
                program=program,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                age=form.cleaned_data['age'],
                whatsapp_number=form.cleaned_data['whatsapp_number'],
            )

            # Send email to admin
            subject = f"New Program Registration for {program.title}"
            message = f"User {registration.name} has registered for {program.title}.\nEmail: {registration.email}\nPhone: {registration.phone}\nWhatsApp: {registration.whatsapp_number}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],  # Admin email from settings
                fail_silently=False,
            )

            # Send confirmation email to the user
            user_message = f"Hello {registration.name},\n\nThank you for registering for {program.title}.\nWe have received your registration and will get back to you soon.\n\nBest regards,\nYour Company Name"
            send_mail(
                "Program Registration Confirmation",
                user_message,
                settings.EMAIL_HOST_USER,
                [registration.email],  # User's email
                fail_silently=False,
            )

            return redirect('success')  # Redirect after successful registration
    else:
        form = ProgramRegistrationForm()

    return render(request, 'programs/register_program.html', {'form': form, 'program': program})