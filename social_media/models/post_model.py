from django.db import models

from .common_info_model import CommonInfoModel
from .admin_model import AdminModel
from .user_model import UserModel


class PostModel(CommonInfoModel):
    """
    A table to store post related details
    """
    description = models.TextField()
    author = models.ForeignKey(AdminModel, on_delete=models.CASCADE)
    likes = models.ManyToManyField(UserModel, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(UserModel, blank=True, related_name='dislikes')
    image = models.ManyToManyField('ImageModel', blank=True)
    tags = models.ManyToManyField('TagsModel', blank=True)

    class Meta:
        db_table = "PostModel"
        ordering = ['-created_at']

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
    

class ImageModel(models.Model):
	image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)


class TagsModel(models.Model):
	name = models.CharField(max_length=255)
   
    class Meta:
        db_table = "TagsModel"
        ordering = ['-created_at']


# class PostImagesModel(CommonInfoModel):
#     """A Table to store images related to a post
#     """
#     gallery_id = models.ForeignKey(PostModel, on_delete=models.CASCADE)
#     gallery_image = models.FileField(upload_to="images/posts")

#     class Meta:
#         db_table = "PostImagesModel"
#         ordering = ['-created_at']
