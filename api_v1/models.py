from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Department(models.Model):
    department_name = models.CharField(max_length=25, unique=True)

    def __str__(self) :
        return self.department_name


class Position(models.Model):
    position_name = models.CharField(max_length=30, unique=True)

    def __str__(self) :
        return self.position_name


class Employee(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]


    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.first_name + '' + self.last_name



class Review(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=35)
    review_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    comment = models.CharField(max_length=150, null=True)
