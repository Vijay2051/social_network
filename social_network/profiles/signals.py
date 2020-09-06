from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, RelationShip


@receiver(post_save, sender=User)
def post_save_created(sender, instance, created, **kwargs):
    print("sender", sender)
    print("instance", instance)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=RelationShip)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print(instance.sender.first_name)
    sender_ = instance.sender
    reciever_ = instance.reciever
    if instance.status == 'accepted':
        sender_.friends.add(reciever_.user)
        reciever_.friends.add(sender_.user)
        sender_.save()
        reciever_.save()
