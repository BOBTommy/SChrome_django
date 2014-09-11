from django.db import models
from django.forms import forms

class User(models.Model):
    user_name = models.CharField(max_length=30)
    join_date = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['user_name']

    def __unicode__(self):
        return self.user_name

class ImageBook(models.Model):
    note_name = models.CharField(max_length=50)
    user_name = models.ForeignKey(User, related_name='+')
    USERNAME_FIELD = 'note_name'
    REQUIRED_FIELDS = ['note_name', 'user_name']

    def __unicode__(self):
        return self.note_name

class Image(models.Model):
    user_name = models.ForeignKey(User, related_name='+')
    note_name = models.ForeignKey(ImageBook, related_name='+')
    image_name = models.CharField(max_length = 50)
    save_date = models.DateTimeField(auto_now_add=True)
    tag = models.TextField()
    is_search = models.BooleanField(default=True)
    image_path = models.CharField(max_length=250)

    REQUIRED_FIELDS = ['user_name', 'note_name', 'tag', 'image_path']

    def __unicode__(self):
        return self.image_name

class ImageText(models.Model):
    image_name = models.ForeignKey(Image, related_name='+')
    user_name = models.ForeignKey(User, related_name='+')
    note_name = models.ForeignKey(ImageBook, related_name='+')
    text = models.TextField()

    REQUIRED_FIELDS = ['image_name', 'user_name', 'note_name', 'text']

    def __unicode__(self):
        return "%s's text : %s" % (self.image_name, self.text)

class Files(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='default_value')
    img_file = models.FileField(upload_to='images/')

class Base64Image(models.Model):
    img_data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    img_title = models.CharField(max_length=100)