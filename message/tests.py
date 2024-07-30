from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class MassagePageTests(SimpleTestCase):
    def test_massage_page_status_code(self):
        response = self.client.get('/message/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response, 'home.html')
        
    def test_template_content(self):
        response = self.client.get('/message/')
        self.assertContains(response, '<h1>Welcome to the Message Board!</h1>')
