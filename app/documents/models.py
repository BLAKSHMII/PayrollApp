from django.db import models

# Create your models here.
from django.db import models

class Document(models.Model):

    DOCUMENT_TYPES = (
        ('PAN', 'PAN'),
        ('AADHAAR', 'AADHAAR'),
        ('BANK', 'BANK'),
        ('CERTIFICATE', 'CERTIFICATE'),
    )

    STATUS = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )

    employee_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    document_number = models.CharField(max_length=100)

    document_file = models.FileField(upload_to='documents/')

    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name