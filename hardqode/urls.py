"""
URL configuration for hardqode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from task import views

router = routers.SimpleRouter()
router.register(r'users', views.UsersViewSet, basename="users")
router.register(r'products', views.ProductdStatisticsViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>/product/<int:product_id>/', views.UserProductViewSet.as_view({'get': 'get_lessons_for_product'}), name='get-lessons-for-product'),
]
