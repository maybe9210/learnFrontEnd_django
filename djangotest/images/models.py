from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangotest.users import models as user_models

# Create your models here.

@python_2_unicode_compatible
class TimeStampeModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =  True

@python_2_unicode_compatible
class Image(TimeStampeModel):
    """ Image Model """
    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, related_name='images')
    @property
    def like_count(self):
        return self.likes.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']

@python_2_unicode_compatible
class Comment(TimeStampeModel):
    """ Commment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True, related_name='comments')

    def __str__(self):
        return self.message

@python_2_unicode_compatible
class Like(TimeStampeModel):
    """  Like Model """
    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True, related_name='likes')

    def __str__(self):
        return 'User: {} -  ImageCaption: {}'.format(self.creator.username, self.image.caption)