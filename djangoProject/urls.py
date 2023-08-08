from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductListAPI, ProductViewSet, V1ExampleView

# Create a router and register the ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', ProductListAPI.as_view(), name='product-list'),
    path('api/', include(router.urls)),
    path('v1/', V1ExampleView.as_view(), name='v1-version'), 

]
