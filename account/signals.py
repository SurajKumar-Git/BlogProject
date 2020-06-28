from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


@receiver(post_save, sender=get_user_model())
def set_default_group(sender, instance, created, **kwargs):
    if created:
        author = Group.objects.get(name="author")
        user = Group.objects.get(name="user")
        instance.groups.add(author, user)
        instance.save()
