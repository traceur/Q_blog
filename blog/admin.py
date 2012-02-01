from django.contrib import admin
import markdown

from Q_blog.blog.models import post,link

admin.site.register(post)
admin.site.register(link)
