from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'blog_date', 'blog_photo', 'description')
  list_display_links = ('id', 'title')
  search_fields = ('id', 'title')
  list_per_page = 25

admin.site.register(Blog, BlogAdmin)
