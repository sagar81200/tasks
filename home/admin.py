from django.contrib import admin

from . models import *

admin.site.register(Details)
admin.site.register(Blog_Post)
admin.site.register(Comment)
admin.site.register(Reply)

