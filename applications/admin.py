from django.contrib import admin
from .models import Applicant, RecommendationLetter

# Register your models here.
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'year', 'status', 'created_at')
    list_filter = ('year', 'status')
    search_fields = ('full_name', 'email')

admin.site.register(RecommendationLetter)