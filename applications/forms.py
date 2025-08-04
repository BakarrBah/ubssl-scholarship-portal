# applications/forms.py
from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        # exclude any fields applicants shouldn’t set themselves
        exclude = ("status", "created_at", "updated_at", "year")
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "input w-full"}),
            "school_2024_2025": forms.TextInput(attrs={"class": "input w-full"}),
            "class_2024_2025": forms.TextInput(attrs={"class": "input w-full"}),
            "school_2025_2026": forms.TextInput(attrs={"class": "input w-full"}),
            "class_2025_2026": forms.TextInput(attrs={"class": "input w-full"}),
            "essay_text": forms.Textarea(
                attrs={"class": "textarea w-full h-40", "placeholder": "Paste your essay here…"}
            ),
        }