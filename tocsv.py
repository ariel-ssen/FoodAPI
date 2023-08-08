import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
import django
django.setup()

import csv
from product.models import Product  

file_path = '/Users/ssen/Documents/pratice/APIpratice4/djangoProject/Food_clean.csv'

def save_data_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) 
        for row in csv_reader:
            obj = Product.objects.create(
                # id = row[1],
                food_cd = row[2],
                group_name = row[3],
                food_name = row[4],
                research_year = row[5],
                maker_name = row[6],
                serving_size = row[7],
                calorie = row[8],
                protein = row[9],
                province = row[10],
                carbohydrate = row[11],
                sugars = row[12],
                salt = row[13],
                cholesterol =row[14],
                saturated_fatty_acids = row[15],
                trans_fat = row[16],
                ref_name = row[17],
                
            )

# save_data_from_csv 함수 호출
save_data_from_csv(file_path)
