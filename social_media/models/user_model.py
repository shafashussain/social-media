from django.db import models
from .common_info_model import CommonInfoModel


class UserModel(CommonInfoModel):
    """
    A table to store the users basic informations
    """
    full_name = models.CharField(max_length=100, null=True)
    mobile_number = models.PositiveBigIntegerField(unique=True, null=True)
    email_id = models.EmailField(blank=True, null=True)
    profile_image = models.FileField(upload_to="images/user_profile_image", null=True)
    followers = models.ManyToManyField('self', blank=True, related_name='followers')

    class Meta:
        db_table = "UserModel"
        ordering = ['-created_at']
