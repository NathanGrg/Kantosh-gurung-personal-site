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
        self.assertContains(response, 'src="/static/images/wa.jpeg"')
        self.assertContains(response, 'class="personal-hero__portrait"')
        self.assertNotContains(response, '>About</a>')
        self.assertContains(
            response,
            f'<a href="{reverse("base")}" aria-current="page">Home</a>',
        )

    def test_homepage_does_not_include_the_photo_gallery(self):
        response = self.client.get(reverse('base'))

        self.assertNotContains(response, 'data-carousel-track')
        self.assertNotContains(response, 'data-carousel-next')

    def test_contributions_page_includes_all_gallery_photos(self):
        response = self.client.get(reverse('contributions'))

        self.assertContains(response, 'Make a difference')
        self.assertContains(response, 'data-carousel-track')
        self.assertContains(response, 'data-carousel-next')
        self.assertNotContains(response, 'src="/static/images/wa.jpeg"')
        for image in [f'images/wa{number}.jpeg' for number in range(2, 29)]:
            with self.subTest(image=image):
                self.assertContains(response, f'/static/{image}')

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

        years = (
            2026, 2025, 2024, 2021, 2020, 2019, 2018, 2017, 2016, 2015,
            2014, 2013, 2012, 2011, 2010, 2009, 2007, 2006, 2003, 2002,
        )
        for year in years:
            with self.subTest(year=year):
                self.assertContains(response, f'<h4>{year}</h4>')

        self.assertIn('Medical camp and relief-material distribution for earthquake victims', content)
        self.assertIn('Buddha Dahal School for the Deaf', content)
        self.assertIn('Janajyoti Ma. Vi., Baglung Pani, Lamjung', content)
        new_activities = (
            'Lekhnath Basic School, Arupata, Lekhnath',
            'Buddha Dahal School for the Deaf, Damauli, Tanahun',
            'Swamisadananda Gurukulam, Danda Nak, Lekhnath',
            'Child Welfare and Education, Lakeside, Pokhara',
            'Namaste Foundation, Lakeside, Pokhara',
            'Chhunhup Primary School, Mustang',
            'Shrijana School for the Deaf, Lekhnath, Kaski',
            'Laxmi Primary School, Laxmi Bazaar, Lamjung',
            'Rainbow Children Home, Lakeside, Pokhara',
            'Saileswari Primary School, Laxmi Bazaar, Lamjung',
            'Bindeswori Primary School, Shyaulibazaar, Lamjung',
        )
        for activity in new_activities:
            with self.subTest(activity=activity):
                self.assertIn(activity, content)
        self.assertIn('/static/images/wa28.jpeg', content)

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
