from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=256, blank=True, null=True, help_text="just photo url")
    website = models.URLField(blank=True)
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

# auto Create Profile object whenever a new User object created.
# and use 'User' model instead 'Profile' model in all place.
# we have to use user's Profile object via 'User' object.
# so forget Profile model and use user.profile object anywhere!
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()