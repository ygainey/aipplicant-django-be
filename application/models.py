from django.db import models
from django.utils import timezone

# Create your models here.

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewing', 'Interviewing'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]

    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    jd_url = models.URLField()
    application_date = models.DateField(default=timezone.now().date)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    salary = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='applications_created'
    )
    notes = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.job_title} at {self.company}'