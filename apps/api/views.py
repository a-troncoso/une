from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Place_Image, Place, User_Place, Profile, Store, Collection, Product
from .serializers import PlaceImageSerializer, PlaceSerializer, UserPlaceSerializer, PlaceDetailSerializer, UserSerializer, ProfileSerializer, StoreSerializer, StoreDetailSerializer, CollectionSerializer, CollectionDetailSerializer, ProductSerializer, ProductDetailSerializer

class PlaceImageViewSet(viewsets.ModelViewSet):
  queryset = Place_Image.objects.all()
  serializer_class = PlaceImageSerializer

class PlaceViewSet(viewsets.ModelViewSet):
  """
  This viewset define views for get all Places, Detail of a place and Users of a Place
  """
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

  def retrieve(self, request, pk=None):
    serializer_context = { 'request': request, }
    queryset = Place.objects.all()
    place = get_object_or_404(queryset, pk=pk)
    serializer = PlaceDetailSerializer(place, context=serializer_context)
    return Response(serializer.data)
  
  # define la ruta api/places/<pk>/users: quien retorna los usuario perteneciente a un Store
  @action(detail=True)
  def users(self, request, pk=None):
    queryset = User_Place.objects.filter(pk=pk)
    serializer = UserPlaceSerializer(queryset, context={'request':request}, many=True)
    return Response(serializer.data)
  
  # define la ruta api/places/<pk>/users: quien retorna los usuario perteneciente a un Store
  # @action(detail=True)
  # def profiles(self, request, pk=None):
  #   queryset = User_Place.objects.filter(pk=pk)
  #   serializer = UserPlaceSerializer(queryset, context={'request':request}, many=True)
  #   return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  # define la ruta api/users/<pk>/stores: quien retorna los Stores perteneciente a un User
  @action(detail=True)
  def stores(self, request, pk=None):
    queryset = Store.objects.filter(user__pk=pk)
    serializer = StoreSerializer(queryset, context={'request':request}, many=True)
    return Response(serializer.data)

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

class StoreViewSet(viewsets.ModelViewSet):
  queryset = Store.objects.all()
  serializer_class = StoreSerializer

  def retrieve(self, request, pk=None):
    serializer_context = { 'request': request, }
    queryset = Store.objects.all()
    store = get_object_or_404(queryset, pk=pk)
    serializer = StoreDetailSerializer(store, context=serializer_context)
    return Response(serializer.data)
  
  # define la ruta api/stores/<pk>/collections: quien retorna las Collections perteneciente a un Store
  @action(detail=True)
  def collections(self, request, pk=None):
    queryset = Collection.objects.filter(store__pk=pk)
    serializer = CollectionSerializer(queryset, context={'request':request}, many=True)
    return Response(serializer.data)

class CollectionViewSet(viewsets.ModelViewSet):
  queryset = Collection.objects.all()
  serializer_class = CollectionSerializer

  # Detalle de una collection
  def retrieve(self, request, pk=None):
    serializer_context = { 'request': request, }
    queryset = Collection.objects.all()
    collection = get_object_or_404(queryset, pk=pk)
    serializer = CollectionDetailSerializer(collection, context=serializer_context)
    return Response(serializer.data)
  
  # define la ruta api/collections/<pk>/products: quien retorna los Products pertenecientes a una Collection
  @action(detail=True)
  def products(self, request, pk=None):
    queryset = Product.objects.filter(collection__pk=pk)
    serializer = ProductSerializer(queryset, context={'request':request}, many=True)
    return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def retrieve(self, request, pk=None):
    serializer_context = { 'request': request, }
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, pk=pk)
    serializer = ProductDetailSerializer(product, context=serializer_context)
    return Response(serializer.data)  