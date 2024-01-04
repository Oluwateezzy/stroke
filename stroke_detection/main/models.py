from django.db import models

# Create your models here.
class Patient(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        # Add other gender options if needed
    ]

    marital_status_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        # Add other options if needed
    ]

    work_type_choices = [
        ('Private', 'Private'),
        ('Self-employed', 'Self-employed'),
        # Add other work type options if needed
    ]

    residence_type_choices = [
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
        # Add other residence type options if needed
    ]

    smoking_status_choices = [
        ('formerly smoked', 'Formerly Smoked'),
        ('never smoked', 'Never Smoked'),
        ('smokes', 'Smokes'),
        # Add other smoking status options if needed
    ]

    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    age = models.IntegerField()
    hypertension = models.BooleanField()
    heart_disease = models.BooleanField()
    ever_married = models.CharField(max_length=3, choices=marital_status_choices)
    work_type = models.CharField(max_length=20, choices=work_type_choices)
    Residence_type = models.CharField(max_length=5, choices=residence_type_choices)
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField(null=True, blank=True)  # Adjust based on actual data
    smoking_status = models.CharField(max_length=20, choices=smoking_status_choices)
    stroke = models.BooleanField()

    def __str__(self):
        return f"{self.id} - {self.gender} - {self.age} - {self.stroke}"
