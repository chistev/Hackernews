from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'points', 'created_at')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('author',)  # Filter by author in the admin panel
    exclude = ('points',)  # Exclude the points field from the form


admin.site.register(Post, PostAdmin)
