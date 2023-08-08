from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductListAPI, ProductViewSet, V1ExampleView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Food API",
        default_version='v1',
        description="안녕하세요. 'Food' Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="qhdghl75@gmail.com"),
        license=openapi.License(name="SSEN"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# Create a router and register the ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListAPI.as_view(), name='product-list'),
    path('api/', include(router.urls)),
    path('v1/', V1ExampleView.as_view(), name='v1-version'), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger 문서 경로


]
