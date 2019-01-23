from django.conf.urls import include, url
#from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('SalesPvsrCym', views.SalesPvsrCymViewSet)
router.register('SalesPvsrCy', views.SalesPvsrCymViewSet)
router.register('SalesPvsrYm', views.SalesPvsrCymViewSet)

urlpatterns = [
    url('', include(router.urls))
]