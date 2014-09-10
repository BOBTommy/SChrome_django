from django.test import TestCase
from django.test.client import Client

class FileUploadTest(TestCase):
    def test_file_upload(self):
        c = Client()
        response = c.post("/upload_serializers/",{'img_file': open("/Users/riskkim/1.jpg"), 'title' : 'image1' })
        print response
