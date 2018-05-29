from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
# choices for the image category section 
CATEGORY_CHOICES  = (
    ('PRIVATE', 'private'),
    ('PUBLIC', 'public')
)
# user model
class User_prof(models.Model):
    """ model that hold infomation on the user """
    username = models.CharField(max_length =30)
    prof_photo = models.ImageField(upload_to ='profiles/', blank = True)
    bio = models.TextField(null = True, blank = True)
    user = models.OneToOneField(User, on_delete =models.CASCADE,null = True, related_name = 'profile')
    following = models.ManyToManyField(User, blank = True, related_name= 'followers')
    mail_confirm = models.BooleanField(default = False)
    def __str__(self):
        return self.username

    # methods
    def save_prof(self):
        """ saves user instance """
        self.save()

    def delete_prof(self):
        """ deletes user instance """
        self.delete()
    # class methods

    @classmethod
    def update_user(cls,id,name,_bio):
        """ updates user infomation by username """
        user = cls.objects.get(pk = id)
        user.username = name
        user.bio = _bio

    
    @classmethod
    def find_profile(cls,name):
        "allows retrieval of user profile by name"
        user = cls.objects.filter(username = name)
        return user

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        User_prof.objects.create(user=instance)
    instance.profile.save()

# comments model
class Comments(models.Model):
    """ class that stores informatrion the comments of an image"""
    comment = models.TextField()
    user = models.ForeignKey(User_prof, null = True)

    #methods
    def save(self):
        "save the comment"
        self.save()
    def delete(self):
        "deletes a comment"
        self.delete()
    
    @classmethod
    def update_comment(cls):
        """allows comment alteration """
        pass

    # image model
class Image(models.Model):
    """ model that saves detials on the photos """
    image = models.ImageField(upload_to = "images/",blank = True)
    image_name = models.CharField(max_length = 30, null = True)
    image_caption = models.TextField(null = True , blank = True)
    prof = models.ForeignKey(User_prof, null = True)
    likes = models.ManyToManyField(User_prof,related_name='who_liked', blank= True)
    comments = models.ForeignKey(Comments, null = True)
    uploaded_at = models.DateField( default = timezone.now)
    category  = models.CharField(max_length = 30, choices = CATEGORY_CHOICES, default = 'PRIVATE')
    # methods 
    def save_image(self):
        """ saves the image and its details """
        pass
    
    def delete_image(self):
        """ deletes image from the database """
        pass


    @classmethod
    def update_caption(cls):
        """ allows user to change image caption"""
        pass
    @classmethod
    def query_by_ids(cls):
        """ retrieves data by the image id """
        pass