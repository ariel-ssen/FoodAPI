from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, filters
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer

# 페이징처리
class StudentPagination(PageNumberPagination): 
    page_size = 10
    
# Product 모델과 시리얼라이저 정의
class ProductViewSet(viewsets.ModelViewSet):
    '''
    Food 영양정보 [Foodapi]
    
        ---
        # 내용
            id : 번호
            food_cd : 식품코드
            group_name : 식품군
            food_name : 식품이름
            research_year : 조사년도
            maker_name : 지역/제조사
            serving_size : 1회 제공량
            calorie : 열량(kcal)(1회제공량당)
            protein : 단백질(g)(1회제공량당)
            province : 지방(g)(1회제공량당)
            carbohydrate : 탄수화물(g)(1회제공량당)
            sugars : 총당류(g)(1회제공량당)
            salt : 나트륨(mg)(1회제공량당)
            cholesterol : 콜레스테롤(mg)(1회제공량당)
            saturated_fatty_acids : 포화지방산(g)(1회제공량당)
            trans_fat : 트랜스지방(g)(1회제공량당)
            ref_name : 자료출처
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StudentPagination
# create
class ProductListAPI(generics.ListAPIView):
    '''
    Food 영양정보 CRUD
    
        ---
        # 내용
            id : 번호
            food_cd : 식품코드 
            group_name : 식품군 
            food_name : 식품이름 
            research_year : 조사년도 
            maker_name : 지역/제조사
            serving_size : 1회 제공량
            calorie : 열량(kcal)(1회제공량당)
            protein : 단백질(g)(1회제공량당)
            province : 지방(g)(1회제공량당)
            carbohydrate : 탄수화물(g)(1회제공량당)
            sugars : 총당류(g)(1회제공량당)
            salt : 나트륨(mg)(1회제공량당)
            cholesterol : 콜레스테롤(mg)(1회제공량당)
            saturated_fatty_acids : 포화지방산(g)(1회제공량당)
            trans_fat : 트랜스지방(g)(1회제공량당)
            ref_name : 자료출처
        
        # 검색clomns
            food_cd : 식품코드 
            group_name : 식품군 
            food_name : 식품이름 
            research_year : 조사년도
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['food_cd', 'food_name', 'research_year', 'maker_name' ]
    pagination_class = StudentPagination

#  version 
class V1ExampleView(APIView):
    '''
    현재 버전은 1 입니다. version.1
    
    
    '''
    def get(self, request):
        data = {'message': 'This is API version 1'}
        return Response(data, status=status.HTTP_200_OK)
