from django.db import models
from authentication.models import User

class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employers')
    company_name = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name