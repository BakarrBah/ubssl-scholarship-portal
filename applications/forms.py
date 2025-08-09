# applications/forms.py
from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ("status", "created_at", "updated_at", "year")

        # 👇 shared Tailwind classes
        _base = (
            "w-full rounded-md border border-gray-300 bg-white "
            "px-3 py-2 text-gray-800 placeholder-gray-400 "
            "focus:outline-none focus:ring-2 focus:ring-indigo-500/70"
        )

        widgets = {
            "full_name":          forms.TextInput(attrs={"class": _base}),
            "school_2024_2025":   forms.TextInput(attrs={"class": _base}),
            "class_2024_2025":    forms.TextInput(attrs={"class": _base}),
            "school_2025_2026":   forms.TextInput(attrs={"class": _base}),
            "class_2025_2026":    forms.TextInput(attrs={"class": _base}),
            "essay_text": forms.Textarea(
                attrs={
                    "class": _base + " h-40 resize-y",
                    "placeholder": "Paste your essay here…",
                }
            ),
            "email":  forms.EmailInput(attrs={"class": _base}),
            "phone":  forms.TextInput(attrs={"class": _base, "placeholder": "Optional"}),
            # File fields keep native styling for now
        }
