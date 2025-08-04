# applications/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicantForm
from datetime import datetime

def apply(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.year = datetime.now().year   # e.g., 2025
            app.save()
            messages.success(request, "Application submitted 🎉")
            return redirect("apply-thanks")
    else:
        form = ApplicantForm()
    return render(request, "applications/apply.html", {"form": form})
