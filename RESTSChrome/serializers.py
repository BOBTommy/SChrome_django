from RESTSChrome.models import User,ImageBook,Image,ImageText
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','user_name','join_date')

class ImageBookSerializer(ModelSerializer):
    class Meta:
        model = ImageBook
        fields = ('id','note_name')

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','user_name','note_name','save_date','image_path')

class ImageTextSerializer(ModelSerializer):
    class Meta:
        model = ImageText
        fields = ('id','user_name','note_name','text')