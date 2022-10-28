from django.test import TestCase
from django.urls import reverse
from .settings import BASE_DIR
import os

class Testcases(TestCase):
    def test_homeview(self):
        """Test case to test homepage view"""
        response = self.client.get(reverse('homepage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed( 'home.html')
    
    def test_apiredirect(self):
        """Test case to test redirection with get request"""
        data = {'formFile1':"X","formFile2":"Y"}
        response = self.client.get(reverse("file_process"), data=data)
        self.assertEquals(response.status_code, 302)
    
    def test_fileprocessing(self):
        """Test case to validate txt file processing."""
        file1 = open(os.path.join(BASE_DIR,"DummyData","utc_test1.txt"),'rb')
        file2 = open(os.path.join(BASE_DIR,"DummyData","utc_test2.txt"),'rb')
        data = {'formFile1':file1,"formFile2":file2}
        response = self.client.post(reverse("file_process"), data=data)
        self.assertEquals(response.get('Content-Disposition'),'inline; filename="op.txt"')
