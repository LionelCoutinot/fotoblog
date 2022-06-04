from django.contrib import admin

from blog.models import Photo
admin.site.register(Photo)

from blog.models import Blog
admin.site.register(Blog)

from authentication.models import User
admin.site.register(User)

