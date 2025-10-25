from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User



# class Author(models.Model):
#     name = models.CharField(max_length=100,verbose_name="Avtor ati")
#     bio = models.TextField(blank=True, verbose_name="Ozi haqqinda")

#     def __str__(self):
#         return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya ati")

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Teg ati")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False, verbose_name="Post juklengenba?")
    #view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Jaratilgan waqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ozgergen waqti")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya", related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tegler", related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Avtor", related_name='posts')
    #author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Avtor", related_name='posts')

    @property
    def get_view_count(self):
        return self.user_actions.aggregate(models.Sum('view_count'))['view_count__sum'] or 0
    
    @property
    def get_like_count(self):
        return self.user_actions.filter(liked=True).count()
    
    @property
    def get_dislike_count(self):
        return self.user_actions.filter(disliked=True).count()




    def __str__(self):
        return self.title
    

class UserPostAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='user_actions')
    view_count = models.IntegerField(default=1)
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by: {self.user.username} - {self.post.title}"