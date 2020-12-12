from django.core.exceptions import ValidationError
from django.db import models
from accounts.models import UserProfile

#  validator jpg and jpeg files allowed.
def is_jpg_or_jpeg_validator(value):
    if not str(value).endswith('.jpg'):
        raise ValidationError('Only .jpg or .jpeg images allowed.')


class Painting(models.Model):
    REALISM = 'Realism'
    PHOTOREALISM = 'Photorealism'
    IMPRESSIONISM = 'Impressionism'
    ABSTRACT = 'Abstract'
    SURREALISM = 'Surrealism'
    POP = 'Pop'
    UNKNOWN = 'Unknown'

    PAINTING_TYPES = (
        (REALISM, 'Realism'),
        (PHOTOREALISM, 'Photorealism'),
        (IMPRESSIONISM, 'Impressionism'),
        (ABSTRACT, 'Abstract'),
        (SURREALISM, 'Surrealism'),
        (POP, 'Pop'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=13, choices=PAINTING_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=20, blank=False)
    size = models.CharField(max_length=12, blank = False)
    artist = models.CharField(max_length=20, blank=False)
    # year = models.CharField(max_length=4, blank=False)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=False)

    image = models.ImageField(
        upload_to='paintings',
        validators = (is_jpg_or_jpeg_validator, )
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.name}; {self.artist}'


class Like(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.painting}; {self.user}'