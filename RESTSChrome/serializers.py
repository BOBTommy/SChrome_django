from RESTSChrome.models import User,ImageBook,Image,ImageText,Files
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from RESTSChrome.models import Base64Image

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','user_name','join_date')

class ImageBookSerializer(ModelSerializer):
    class Meta:
        model = ImageBook
        fields = ('id','note_name','user_name')

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','image_name','user_name','note_name','save_date','tag')

class ImageTextSerializer(ModelSerializer):

    class Meta:
        model = ImageText
        fields = ('id','image_name','user_name','note_name','text')

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('img_file', 'title')

class Base64ImageSerializer(ModelSerializer):

    class Meta:
        model = Base64Image
        fields = ('img_title', 'created', 'img_data')