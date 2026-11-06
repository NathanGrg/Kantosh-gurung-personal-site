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
            'programme': 'Programme',
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
        self.assertContains(response, 'River Side Health Center')
        self.assertContains(response, 'Dental Health Worker')
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
        pages = ('base', 'programme', 'objectives', 'contributions', 'health_news')

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

    def test_objectives_page_includes_objectives_and_goals(self):
        response = self.client.get(reverse('objectives'))

        self.assertContains(response, 'high school students')
        self.assertContains(response, 'safe maternity and childbirth')
        self.assertContains(response, 'Prevent dental caries')
        self.assertContains(response, 'mobile dental unit')
        self.assertContains(response, 'healthy, satisfying lives')

    def test_contributions_page_lists_ways_to_support_dgn(self):
        response = self.client.get(reverse('contributions'))

        self.assertContains(response, 'Become a friend of DGN')
        self.assertContains(response, 'Become a DGN family member')
        self.assertContains(response, 'Donate to dental camps')
        self.assertContains(response, 'Volunteer in the community')

    def test_health_news_page_lists_historical_activities_by_year(self):
        response = self.client.get(reverse('health_news'))
        content = response.content.decode()

        for year in (2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2007, 2006, 2003, 2002):
            with self.subTest(year=year):
                self.assertContains(response, f'<h4>{year}</h4>')

        self.assertIn('Medical camp and relief-material distribution for earthquake victims', content)
        self.assertIn('Buddha Dahal School for the Deaf', content)
        self.assertIn('Janajyoti Ma. Vi., Baglung Pani, Lamjung', content)

    def test_programme_page_shows_dgn_services_and_activities(self):
        response = self.client.get(reverse('programme'))

        self.assertContains(response, 'economically disadvantaged families')
        self.assertContains(response, 'Now we are')
        self.assertContains(response, 'Free dental camps')
        self.assertContains(response, 'Free advice, treatment, and medication')
        self.assertContains(response, 'GIC and amalgam fillings')
        self.assertContains(response, 'Health education')
        self.assertContains(response, 'Community participation')
        self.assertContains(response, 'Other school activities')
        self.assertNotContains(response, 'These sample programs')
        self.assertNotContains(response, 'Dental Team Learning')
