from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Product
from .serializers import ProductSerializer

class ProductListAPI(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    


# Product 모델과 시리얼라이저 정의
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ProductListAPI 뷰 정의
class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['food_name', 'group_name', 'maker_name']

# 기타 다른 뷰들이 있다면 여기에 추가 

# 버전 1 예시 뷰 정의
class V1ExampleView(APIView):
    def get(self, request):
        data = {'message': 'This is API version 1'}
        return Response(data, status=status.HTTP_200_OK)
