from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a Profile when a new User is created.
    """
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save the Profile whenever the User is saved.
    """
    if hasattr(instance, 'profile'):  # Ensure the user has a profile
        instance.profile.save()
