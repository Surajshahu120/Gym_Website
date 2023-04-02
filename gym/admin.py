from django.contrib import admin
from .models import gym_website
from .models import contact_detail

class gym_website_admin(admin.ModelAdmin):
    list_display=("name","phone","email","gender","dob")

class contact_admin(admin.ModelAdmin):
    list_display=("name","email","message")

admin.site.register(gym_website,gym_website_admin)


admin.site.register(contact_detail,contact_admin)   

 

