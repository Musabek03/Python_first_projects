from django.contrib import admin
from .models import Post,Category,Tag,Comment


#admin.site.register(Post)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('category', 'tags')
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','post', 'created_date',)
    search_fields = ('text','post',)
    list_filter = ('post',)

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name',)



    


# Register your models here.

