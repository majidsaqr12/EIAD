from django.shortcuts import render

from .models import Program

def program(request):
    programs = Program.objects.all()
    return render(request, 'programs/programs.html', {'programs': programs})
