from django.contrib import admin
from .models import Blog, Newrelease, Popular, Protein, Sleep , Trending 

# Register your models here.
admin.site.register(Blog),
admin.site.register(Trending),
admin.site.register(Popular),
admin.site.register(Newrelease),
admin.site.register(Sleep),
admin.site.register(Protein),
