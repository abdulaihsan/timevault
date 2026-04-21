from django.db import models

class VaultLetter(models.Model):
    BATCH_CHOICES = [
        (32, 'Batch 32'),
        (33, 'Batch 33'),
        (34, 'Batch 34'),
        (35, 'Batch 35'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    instagram_handle = models.CharField(max_length=50, blank=True, null=True)
    backup_contact = models.CharField(max_length=20, blank=True, null=True)
    batch = models.IntegerField(choices=BATCH_CHOICES)
    plan_years = models.IntegerField(choices=[(3, '3 Years'), (5, '5 Years')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Batch {self.batch} ({self.plan_years} Years)"