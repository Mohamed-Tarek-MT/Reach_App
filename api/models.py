from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    ) 
    content = models.TextField(blank=True, null=True) 
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True
    )  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user.username}'s post at {self.created_at}"

    
    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )  
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    ) 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username} liked post {self.post.id}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    ) 
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"


