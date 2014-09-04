from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=30)
    join_date = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'user_name'

    def __unicode__(self):
        return self.user_name

class ImageBook(models.Model):
    note_name = models.CharField(max_length=50)
    USERNAME_FIELD = 'note_name'

    def __unicode__(self):
        return self.note_name

class Image(models.Model):
    image_id = models.CharField(max_length=30)
    user_name = models.ForeignKey(User, related_name='+')
    note_name = models.ForeignKey(ImageBook, related_name='+')
    save_date = models.DateField(auto_now_add=True)
    tag = models.TextField()
    is_search = models.BooleanField(default=True)
    image_path = models.CharField(max_length=250)

    def __unicode__(self):
        return self.image_id

class ImageText(models.Model):
    image_id = models.ForeignKey(Image, related_name='+')
    user_name = models.ForeignKey(User, related_name='+')
    note_name = models.ForeignKey(ImageBook, related_name='+')
    text = models.TextField()

    def __unicode__(self):
        return "%s's text : %s" % (self.image_id, self.text)
