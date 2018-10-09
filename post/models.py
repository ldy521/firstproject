from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=64)
    # auto_now_add  第一次创建的时间
    created = models.DateTimeField(auto_now_add=True)
    # auto_now  最后一次修改的时间
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        # 排序方式 按照时间倒序， 最新创建在前
        ordering = ['-created']