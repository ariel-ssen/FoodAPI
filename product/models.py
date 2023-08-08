from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    food_cd = models.CharField(max_length=70)
    group_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=70)
    research_year = models.CharField(max_length=100)
    maker_name = models.CharField(max_length=70)
    serving_size = models.CharField(max_length=70)
    calorie = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    province = models.CharField(max_length=70)
    carbohydrate = models.CharField(max_length=70)
    sugars = models.CharField(max_length=100)
    salt = models.CharField(max_length=70)
    cholesterol = models.CharField(max_length=100)
    saturated_fatty_acids = models.CharField(max_length=70)
    trans_fat = models.CharField(max_length=70)
    ref_name = models.CharField(max_length=100)
    
    def __str__(self):
         return self.food_name
    