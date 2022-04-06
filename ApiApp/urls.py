from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ProductModel',views.ProductModelViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('api/',include(router.urls)),
]