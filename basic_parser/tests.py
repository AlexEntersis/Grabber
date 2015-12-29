from django.test import TestCase


# Create your tests here.


class TestViews(TestCase):

    def test_call_main_view_loads(self):
        """test if there is home page following current link"""

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_call_statistics_view_loads(self):
        """test if there is statistics page following current link"""

        response = self.client.get('/statistics/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statistics.html')

    def test_call_parse_view_loads(self):
        """test if there is parse page following current link"""
#ghghghhg
        response = self.client.get('/parse/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parse.html')


