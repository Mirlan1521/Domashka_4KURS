from django.contrib import admin
from magazin.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Review)