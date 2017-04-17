from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.conf import settings

# Create your models here.

#(目錄分類)
class Category(models.Model):
    CName = models.CharField(max_length=50)
    EName = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.CName

# (原料)
class Materials(models.Model):
    CName = models.CharField(max_length=50)
    EName = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.CName


#食譜清單
class Formulate(models.Model):
    author = models.ForeignKey(User)
    #種類, 麵包/蛋糕/點心..
    #category = models.IntegerField()
    category = models.ForeignKey(Category)

    #食譜名稱
    title = models.CharField(max_length=200)

    #小圖示
    #image = models.CharField(max_length=200,blank=True, null=True)
    image = models.FileField(upload_to=settings.UPLOAD_ROOT,blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#(配方表)
class FormulateDetails(models.Model):
    formulate = models.ForeignKey(Formulate)
    material = models.ForeignKey(Materials, default=1)

    volume = models.IntegerField()
    unit = models.CharField(max_length=10, default='公克')
    created_date = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return str(self.formulate)
