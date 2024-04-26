from django.contrib import admin
from .models import News
from .models import Category
from .models import *

admin.site.register(News)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Category)
# Register your models here.
