from django.db import models
from user.models import User
# Create your models here.


SERVICE_TYPES = (
        ('New Gas Registration', 'New Gas Registration'),
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
    )


STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )



class ServiceRequest(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    details = models.TextField()
    attached_file = models.FileField(upload_to='media/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.username} - {self.service_type}"