from django.test import TestCase
from search.forms import SearchForm


class TestViews(TestCase):
    def test_search_view_loads(self):
        """test if there is search page following current link"""

        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_if_form_is_valid(self):
        """test if there is form on the search page is valid"""
        form_data = {"name":"name"}
        name_form = SearchForm(data=form_data)
        self.assertTrue(name_form.is_valid)





