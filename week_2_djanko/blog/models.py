from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

    def __str__(self): #__ 두개는 내부에 쓴다는 선언, self는 자기 자신을 지칭 
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=100)
