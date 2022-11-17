from django.db import models

# Create your models here.

class Supplier (models.Model):
    supplier = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.supplier
    

class Range (models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='Supplier')
    range = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.range


class RollCut (models.Model):
    range = models.ForeignKey(Range, on_delete=models.CASCADE, related_name='Range')
    roll_colour = models.CharField(max_length=20, null=False, blank=False)
    roll_width = models.CharField(max_length=2, null=False, blank=False, default='4m')
    roll_length = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, default='25.00')
    location = models.CharField(max_length=2, null=False, blank=False)
    invoice = 
    cut_size = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    cut = models.BooleanField(null=False, blank=False, default=False)
    date_cut = models.DateTimeField(auto_now_add=True)
    cut_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return