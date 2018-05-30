from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

class Menu_Item(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  position = models.PositiveSmallIntegerField()
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # Un menu item puede ser hijo de otro, esto es, en parent_menu_item puede hacer referencia a otro menu_item
  parent_menu_item = models.ForeignKey('self', on_delete=models.CASCADE)

  def __str__(self):
    return '{} ({})'.format(self.name, self.description)

class Menu(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  menu_items = models.ManyToManyField(Menu_Item, through='Menu_Menu_Item')

  def __str__(self):
    return '{} ({})'.format(self.name, self.description)

class Menu_Menu_Item(models.Model):
  menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
  menu_item = models.ForeignKey(Menu_Item, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return '{} ({})'.format(self.name, self.description)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  img_user_url = models.CharField(blank=True, null=True, max_length=512)
  img_cover_url = models.CharField(blank=True, null=True, max_length=512)
  activity_desc = models.CharField(blank=True, null=True, max_length=512)
  # null If True, Django guarda los datos vacíos como null
  # blank If True, se permiten datos en blanco
  role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return '{}'.format(self.user)

class Place_Image(models.Model):
  img_url = models.CharField(max_length=512)
  is_primary = models.BooleanField(default=True)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.description, self.img_url)

class Place(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  start_date = models.DateTimeField(default=None, blank=True, null=True)
  end_date = models.DateTimeField(default=None, blank=True, null=True)
  location_address = models.CharField(blank=True, null=True, max_length=256)
  location_lat = models.FloatField(default=None)
  location_lng = models.FloatField(default=None)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # Un Place puede contener muchos Users y para almacenar más información de la relación se usa un modelo intermediario
  users = models.ManyToManyField(User, through='User_Place')
  images = models.ManyToManyField(Place_Image)

  def __str__(self):
    return '{}'.format(self.name)
  
class User_Place(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  place = models.ForeignKey(Place, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} ESTÁ EN {}'.format(self.user, self.place)

class Store_Image(models.Model):
  img_url = models.CharField(max_length=512)
  is_primary = models.BooleanField(default=True)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.description, self.img_url)

class Store(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  images = models.ManyToManyField(Store_Image)

  def __str__(self):
    return '{} ({})'.format(self.name, self.description)

class Collection_Image(models.Model):
  img_url = models.CharField(max_length=512)
  is_primary = models.BooleanField(default=True)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.description, self.img_url)

class Collection(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  images = models.ManyToManyField(Collection_Image)

  def __str__(self):
    return '{} ({})'.format(self.name, self.description)

class Product_Image(models.Model):
  img_url = models.CharField(max_length=512)
  is_primary = models.BooleanField(default=True)
  description = models.CharField(blank=True, null=True, max_length=512)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return '{} - {}'.format(self.description, self.img_url)

class Product(models.Model):
  name = models.CharField(max_length=128)
  description = models.CharField(blank=True, null=True, max_length=512)
  price = models.PositiveIntegerField(default=0)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
  images = models.ManyToManyField(Product_Image)

  def __str__(self):
    return '{} ({})'.format(self.name, self.description)

class Product_Comment(models.Model):
  comment_text = models.TextField(max_length=2048)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# LIKES
class User_Like(models.Model):
  # fk con related name ya q user_creator y user_assignee hacen referencia al modelo User
  user_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
  # fk con related name ya q user_creator y user_assignee hacen referencia al modelo User
  user_assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee') 
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} LE DIÓ LIKE A: {}'.format(self.user_creator, self.user_assignee)

class Place_Like(models.Model):
  place = models.ForeignKey(Place, on_delete=models.CASCADE, default=1)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} LE GUSTA EL LUGAR: {}'.format(self.user, self.place)

class Product_Like(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} LE GUSTA EL PRODUCTO: {}'.format(self.user, self.product)