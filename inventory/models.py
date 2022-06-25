from django.db import models

# Create your models here.
class supplier(models.Model):
    name        = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class inventory(models.Model):
    name            = models.CharField(max_length=150, unique=True)
    description     = models.CharField(max_length=150)
    note            = models.TextField()
    stock           = models.IntegerField(null=False)
    availability    = models.BooleanField()
    supplier        = models.ForeignKey(supplier, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name