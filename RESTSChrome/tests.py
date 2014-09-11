from django.test import TestCase
from django.test.client import Client
import base64

class FileUploadTest(TestCase):
    def test_file_upload(self):
        c = Client()
        file = open("/Users/riskkim/3.png", 'rb').read()
        b64img = base64.b64encode(file)
        #print(b64img[0:10])
        response = c.post("/base64_file/",{'img_data': b64img, 'img_title' : 'image1' })
        #response = c.post("/upload_form/",{'img_file': b64img, 'title' : 'image1'})
        print response
