from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Menu_Item, Menu, Menu_Menu_Item, Role, Profile, Place_Image, Place, User_Place, Store_Image, Store, Collection_Image, Collection, Product_Image, Product, Product_Comment, User_Like, Place_Like, Product_Like

admin.site.register(Menu_Item)
admin.site.register(Menu)
admin.site.register(Menu_Menu_Item)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Place_Image)
admin.site.register(Place)
admin.site.register(User_Place)
admin.site.register(Store_Image)
admin.site.register(Store)
admin.site.register(Collection_Image)
admin.site.register(Collection)
admin.site.register(Product_Image)
admin.site.register(Product)
admin.site.register(Product_Comment)
admin.site.register(User_Like)
admin.site.register(Place_Like)
admin.site.register(Product_Like)