from django.contrib import admin
from .models import Post


#admin.site.register(Post)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title', 'content')

# Register your models here.

