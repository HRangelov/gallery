from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import UserProfile


@receiver(post_save, sender=User)
def use_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()