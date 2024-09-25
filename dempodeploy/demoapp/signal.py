from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Employee

@receiver(post_delete,sender=Employee)
def delete_media_image(sender,instance,**kwargs):
    if instance.image:
        instance.image.delete(save=False) # This deletes the image from S3