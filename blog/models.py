from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser


# CKEDITOR WITH IMAGE UPLOAD !!!!


# Create your models here.


class UserTrainer(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    age = models.PositiveIntegerField(null=True)
    info = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='media/stuff_images')
    inst = models.URLField(blank=True)
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.email


class Post(models.Model):
    DEFAULT_TRAINER_ID = 1

    article = models.CharField(max_length=50, default='Article text')
    slug = models.SlugField(max_length=30)
    keywords = models.CharField(max_length=100)
    text = RichTextUploadingField(blank=True, null=True)
    trainer = models.ForeignKey(UserTrainer, on_delete=models.CASCADE, null=False, default=0)

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
