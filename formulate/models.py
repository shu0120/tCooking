from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#食譜清單
class Formulate(models.Model):
    author = models.ForeignKey(User)
    #食譜名稱
    title = models.CharField(max_length=200)
    #種類, 麵包/蛋糕/點心..
    category = models.IntegerField()
    #小圖示
    image = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
