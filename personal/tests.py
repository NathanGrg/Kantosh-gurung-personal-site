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

                self.assertTemplateUsed(response, f'personal/{route_name}.html')
                self.assertContains(response, f'<title>{page_title}</title>')
                self.assertIn('KANTOSH GURUNG', response.content.decode().upper())
                self.assertContains(response, '<a class="navbar__brand" href="/">')
                self.assertContains(
                    response,
                    f'<a href="{reverse(route_name)}" aria-current="page">',
                )
                self.assertEqual(
                    response.content.decode().count('aria-current="page"'),
                    1,
                )

    def test_homepage_introduces_kantosh_and_his_work(self):
        response = self.client.get(reverse('base'))

        self.assertContains(response, 'Kantosh Gurung')
        self.assertContains(response, 'CMA')
        self.assertContains(response, 'Dental River Side Health Center')
        self.assertContains(response, 'Shyaulibazaar, Lamjung')
        self.assertContains(response, 'Program-in-charge at Drop Group Nepal')
        self.assertNotContains(response, '>About</a>')
        self.assertContains(
            response,
            f'<a href="{reverse("base")}" aria-current="page">Home</a>',
        )

    def test_about_page_is_removed(self):
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 404)

    def test_non_contact_pages_use_community_images(self):
        pages = ('base', 'program', 'objectives', 'contributions', 'health_news')

        for route_name in pages:
            with self.subTest(page=route_name):
                response = self.client.get(reverse(route_name))

                self.assertContains(response, '/static/images/wa')

    def test_team_page_keeps_placeholder_images(self):
        response = self.client.get(reverse('team'))

        self.assertContains(response, '/static/personal/team/coordinator.svg')
        self.assertContains(response, '/static/personal/team/editor.svg')
        self.assertContains(response, '/static/personal/team/volunteer.svg')
        self.assertContains(response, '/static/personal/team/advisor.svg')
