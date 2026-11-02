from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    STORAGES={
        'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
        },
    }
)
class SectionPageTitleTests(TestCase):
    def test_section_titles_show_the_current_page_name(self):
        pages = {
            'about': 'About Me',
            'program': 'Dental Health Programs',
            'objectives': 'Objectives',
            'contributions': 'Contributions',
            'health_news': 'Dental Health News',
            'team': 'Our Team',
            'contact': 'Contact',
        }

        for route_name, page_title in pages.items():
            with self.subTest(page=route_name):
                response = self.client.get(reverse(route_name))

                self.assertContains(response, f'<title>{page_title}</title>')
