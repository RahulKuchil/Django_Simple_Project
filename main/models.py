from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=100)
    roll_no=models.IntegerField()
    hindi= models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    science=models  .IntegerField(default=0)
    total=models.IntegerField(default=0)
    perecent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name