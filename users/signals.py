from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         myrole = role.objects.get(rolename="vendor head")
#         profile.objects.create(user=instance)
#         instance.profile.roles.add(myrole)  # for many to many field use add
#         print("Profile Created!")


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if created:
    attr_needed = ['_role']
    if all(hasattr(instance, attr) for attr in attr_needed):
        myrole = role.objects.get(rolename=instance._role)
        print("----------------------vendorhead is: ",
              instance._vendorhead, "------------------------------------")
        vendorhead = User.objects.get(username=instance._vendorhead)
        profile.objects.create(user=instance, head=vendorhead)
        # for many to many field use add
        instance.profile.roles.add(myrole)
        print("Profile Created!")


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print("Profile saved!")
