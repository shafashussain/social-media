from django.db import models
from .common_info_model import CommonInfoModel


class AdminModel(CommonInfoModel):
    """
    A table to store the admin basic informations
    """
    full_name = models.CharField(max_length=100, null=True)
    mobile_number = models.PositiveBigIntegerField(unique=True, null=True)
    email_id = models.EmailField(blank=True, null=True)
    profile_image = models.FileField(upload_to="images/admin_profile_image", null=True)

    class Meta:
        db_table = "AdminModel"
        ordering = ['-created_at']
