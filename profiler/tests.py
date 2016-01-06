from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):

    def test_call_login_view_loads(self):
        """test if there is login page following current link"""

        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


