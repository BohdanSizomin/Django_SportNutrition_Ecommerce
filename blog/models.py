from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


# Create your models here.
def picture_dimesions_validation(width=None, height=None):
    from PIL import Image

    def validator(image):
        img = Image.open(image)
        fw, fh = img.size
        if fw > width or fh > height or fw < width or fh < height:
            raise ValidationError(
                "Height or Width is larger/lower than what is allowed picture must have 256 x 256 dimensions")

    return validator


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

    article = models.CharField(max_length=60, default='Article text', validators=[MinLengthValidator(25)], )
    slug = models.SlugField(max_length=30)
    keywords = models.CharField(max_length=100, )
    text = RichTextUploadingField(blank=True, null=True)
    trainer = models.ForeignKey(UserTrainer, on_delete=models.CASCADE, null=False, default=0)
    preview_image = models.ImageField(upload_to='media/stuff_images/post_previews', null=False, default=0,
                                      validators=[picture_dimesions_validation(256, 256)])
    is_published = models.BooleanField(null=True, default=True)

    #

    def __str__(self):
        return self.article

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
