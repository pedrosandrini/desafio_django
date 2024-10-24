from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    user = get_user_model()
    if not user.objects.filter(username='admin').exists():
        user.objects.create_superuser('admin', 'admin@example.com', 'admin')