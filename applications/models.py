import uuid #unique identifier for each model instance
from django.db import models
from django.core.validators import FileExtensionValidator # File type validation
from django.core.exceptions import ValidationError # Custom validation errors



# Create your models here.


class Status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    SUBMITTED = 'Submitted', 'Submitted'
    REVIEWED = 'Reviewed', 'Reviewed'
    SHORTLISTED = 'Shortlisted', 'Shortlisted'
    ACCEPTED = 'Accepted', 'Accepted'
    REJECTED = 'Rejected', 'Rejected'


class Applicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.PositiveSmallIntegerField()

    full_name = models.CharField(max_length=150)

    school_2024_2025 = models.CharField(max_length=150)
    class_2024_2025 = models.CharField(max_length=150)

    school_2025_2026 = models.CharField(max_length=150)
    class_2025_2026 = models.CharField(max_length=150)

    essay_text = models.TextField(blank=True, null=True)
    essay_upload = models.FileField(upload_to="essays/%Y/%m/",
                                    blank= True,
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])

    report_card = models.FileField(upload_to="report_cards/%Y/%m/",
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])],)
    
    id_photo = models.ImageField(upload_to="id_photos/%Y/%m/",
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])
    
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.PENDING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('year', 'email')
        ordering = ['-created_at']
    
    def clean(self):
        if not self.essay_text and not self.essay_upload:
            raise ValidationError("Please provide either typed essay text or an uploaded scan.")
        if self.essay_text and self.essay_upload:
            #allowed we just don't want neither to be empty
            pass

    def __str__(self):
        return f"{self.full_name} - {self.year} - {self.status}"


class RecommendationLetter(models.Model):
    applicant = models.ForeignKey(
        "Applicant",
        related_name="recommendations",
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to="recommendation_letters/%Y/%m/",
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.file and self.file.size > 5 * 1024 * 1024:
            raise ValidationError("File size must be less than 5MB.")
        
        #max two recommendation letters per applicant
        existing_count = RecomendationLetter.objects.filter(applicant=self.applicant).exclude(pk=self.pk).count()
        if existing_count >= 2:
            raise ValidationError("You can only upload a maximum of two recommendation letters.")
    
    def __str__(self):
        return f"Recommendation for {self.applicant} uploaded on {self.uploaded_at.strftime('%Y-%m-%d')}"
    class Meta:
        verbose_name = "Recommendation Letter"
        verbose_name_plural = "Recommendation Letters"
    


