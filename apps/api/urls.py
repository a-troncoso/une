from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.api import views

router = DefaultRouter()
router.register('places', views.PlaceViewSet)
router.register('profiles', views.ProfileViewSet)
router.register('stores', views.StoreViewSet)
router.register('collections', views.CollectionViewSet)
router.register('products', views.ProductViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
  path('', include(router.urls))
]