from RESTSChrome.models import User,ImageBook,Image,ImageText,ImageFile
from RESTSChrome.serializers import UserSerializer,ImageBookSerializer,ImageSerializer,ImageTextSerializer
from RESTSChrome.serializers import ImageFileSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserListView(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

class ImageBookListView(generics.ListCreateAPIView):
    model = ImageBook
    serializer_class = ImageBookSerializer

class ImageBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = ImageBook
    serializer_class = ImageBookSerializer

class ImageListView(generics.ListCreateAPIView):
    model = Image
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Image
    serializer_class = ImageSerializer

class ImageTextListView(generics.ListCreateAPIView):
    model = ImageText
    serializer_class = ImageTextSerializer

class ImageTextDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = ImageText
    serializer_class = ImageTextSerializer

@api_view(['GET','POST'])
def upload_form(request):
    if request.method == 'POST':
        instance = ImageFile(file=request.FILES['file'], title=request.DATA['title'])
        instance.save()
        return Response('uploaded')
    elif request.method == 'GET':
        files = ImageFile.objects.all()
        serializer = ImageFileSerializer(files)
        return Response(serializer.data)

@api_view(['POST','GET'])
def upload_serializers(request):
    if request.method == 'POST':
        serializer = ImageFileSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        files = ImageFile.objects.all()
        serializer = ImageFileSerializer(files)
        return Response(serializer.data)
