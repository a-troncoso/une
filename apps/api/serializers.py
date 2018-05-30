from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Place_Image, Place, User_Place, Place_Like, Profile, User_Like, Store_Image, Store, Collection_Image, Product_Image, Collection, Product, Product_Like

class PlaceImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Place_Image
    fields = ('img_url', 'is_primary', 'description')

class PlaceSerializer(serializers.ModelSerializer):
  images = PlaceImageSerializer(many=True, read_only=True)
  user_count = serializers.SerializerMethodField()
  place_like_count = serializers.SerializerMethodField()

  # Obtiene la cantidad de Users que pertenece al Place
  def get_user_count(self, place):
    return User.objects.filter(place=place).count()

  # Obtiene la cantidad de Place_Likes pertenecientes al Place
  def get_place_like_count(self, place):
    return Place_Like.objects.filter(place=place).count()

  class Meta:
    model = Place
    fields = ('id', 'url', 'name', 'start_date', 'end_date', 'location_address', 'location_lat', 'location_lng', 'user_count', 'images', 'place_like_count', )

class PlaceDetailSerializer(serializers.ModelSerializer):
  images = PlaceImageSerializer(many=True, read_only=True)
  place_like_count = serializers.SerializerMethodField()

  # Obtiene la cantidad de Place_Likes pertenecientes al Place
  def get_place_like_count(self, place):
    return Place_Like.objects.filter(place=place).count()

  class Meta:
    model = Place
    fields = ('id', 'name', 'description', 'start_date', 'end_date', 'location_address', 'location_lat', 'location_lng', 'images', 'place_like_count', )

class ProfileSerializer(serializers.ModelSerializer):
  user_like_count = serializers.SerializerMethodField()

  # Obtiene la cantidad de User_Like perteneciente al User del Profile
  def get_user_like_count(self, profile):
    return User_Like.objects.filter(user_assignee=profile.user).count()

  class Meta:
    model = Profile
    fields = ('id', 'url', 'img_cover_url', 'img_user_url', 'activity_desc', 'user_like_count',)

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)

  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'profile',)

class StoreImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store_Image
    fields = ('img_url', 'is_primary', 'description',)

class StoreDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    fields = ('id', 'name', 'description',)

class StoreSerializer(serializers.ModelSerializer):
  images = StoreImageSerializer(many=True, read_only=True)

  class Meta:
    model = Store
    fields = ('id', 'url', 'name', 'images',)

class CollectionImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection_Image
    fields = ('img_url', 'is_primary', 'description',)

class CollectionSerializer(serializers.ModelSerializer):
  images = CollectionImageSerializer(many=True, read_only=True)

  class Meta:
    model = Collection
    fields = ('id', 'url', 'name', 'images',)

class CollectionDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields = ('id', 'name', 'description',)

class ProductImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product_Image
    fields = ('img_url', 'is_primary', 'description',)

class ProductSerializer(serializers.ModelSerializer):
  images = CollectionImageSerializer(many=True, read_only=True)

  class Meta:
    model = Product
    fields = ('id', 'url', 'name', 'images',)

class ProductDetailSerializer(serializers.ModelSerializer):
  images = CollectionImageSerializer(many=True, read_only=True)
  product_like_count = serializers.SerializerMethodField()

  # Obtiene la cantidad de Product_Like perteneciente al Product
  def get_product_like_count(self, product):
    return Product_Like.objects.filter(product=product).count()

  class Meta:
    model = Product
    fields = ('id', 'name', 'description', 'images', 'price', 'product_like_count',)

class UserPlaceSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = User_Place
    fields = ('user',)