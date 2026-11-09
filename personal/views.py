from django.shortcuts import render


SECTION_CONTENT = {
    'programme': {
        'title': 'Programme',
        'intro': 'The main aim is to help and support community members and school children by providing free advice, medication, and treatment for those suffering from poor oral hygiene and other communicable diseases. We also provide sports materials, books, pens, pencils, toothpaste, and toothbrushes to schoolchildren in remote villages. Our support is especially for children from economically disadvantaged families, including those in urban areas of Nepal who need help with health problems.',
        'paragraphs': [
        ],
        'activities': [
            {
                'title': 'Free dental camps',
                'description': 'School and community health programs that bring dental services closer to people.',
            },
            {
                'title': 'Free advice, treatment, and medication',
                'description': 'Oral-health guidance, treatment, and medication for community members in need.',
            },
            {
                'title': 'Fillings and extractions',
                'description': 'Dental filling and extraction services, including GIC and amalgam fillings.',
            },
            {
                'title': 'Scaling',
                'description': 'Dental scaling as part of oral health care.',
            },
            {
                'title': 'Health education',
                'description': 'Health education for community members and school children.',
            },
            {
                'title': 'Health awareness programs',
                'description': 'Programs that raise awareness of health and encourage healthy communities.',
            },
            {
                'title': 'Community participation',
                'description': 'Community participation programs that bring people together around local health needs.',
            },
            {
                'title': 'Other school activities',
                'description': 'School activities, including support with sports materials, books, pens, pencils, toothpaste, and toothbrushes.',
            },
        ],
    },
    'objectives': {
        'title': 'Objectives',
        'intro': 'We work with communities to improve oral health, expand health awareness, and create opportunities for children and families.',
        'paragraphs': [
        ],
        'image': 'images/wa11.jpeg',
        'image_alt': 'Students gather for a community oral health event',
        'items': [
            {
                'title': 'Promote oral health',
                'description': 'Promote oral health programs for community members and high school students.',
            },
            {
                'title': 'Build community awareness',
                'description': 'Promote health awareness programs and studies in different communities.',
            },
            {
                'title': 'Support children’s health',
                'description': 'Promote health programs for primary school children in different schools and places.',
            },
            {
                'title': 'Prevent tooth decay',
                'description': 'Prevent and control dental caries (tooth decay) across all life stages.',
            },
            {
                'title': 'Promote safe dental care',
                'description': 'Promote prevention of disease transmission in dental health care settings.',
            },
            {
                'title': 'Support safe maternity',
                'description': 'Promote health awareness about safe maternity and childbirth.',
            },
            {
                'title': 'Encourage physical and intellectual development',
                'description': 'Organize sports-goods programs and other useful activities for physical and intellectual development.',
            },
            {
                'title': 'Build skills and livelihoods',
                'description': 'Run skills-development training and livelihood-focused programs for marginalized women, including widows and people who are poor or otherwise in need.',
            },
        ],
        'goals_intro': 'Our goals combine access to care, prevention, community education, and practical support.',
        'goals': [
            {
                'title': 'Help people access treatment',
                'description': 'Provide free treatment to people with low incomes, particularly older people, children, and other community members in need.',
            },
            {
                'title': 'Prevent dental caries',
                'description': 'Prevent and control dental caries (tooth decay) across all life stages.',
            },
            {
                'title': 'Promote safe dental settings',
                'description': 'Promote prevention of disease transmission in dental health care settings.',
            },
            {
                'title': 'Strengthen oral health programs',
                'description': 'Increase oral health program capacity and effectiveness, and help programs improve their reach and impact.',
            },
            {
                'title': 'Bring dental camps to communities',
                'description': 'Organize dental camps with DGN’s mobile dental unit and team in needy parts of Nepal.',
            },
            {
                'title': 'Teach healthy oral care',
                'description': 'Provide community health-awareness education and programs about oral and dental health for healthy living.',
            },
            {
                'title': 'Support development',
                'description': 'Organize sports-goods programs and other useful activities for physical and intellectual development.',
            },
            {
                'title': 'Support women’s livelihoods',
                'description': 'Run skills-development training and livelihood-focused programs for marginalized women, including widows and people who are poor or otherwise in need.',
            },
        ],
        'goals_vision': 'We aim to help build a community where everyone can enjoy good oral health and lead healthy, satisfying lives. We work to strengthen awareness, prevent and control oral diseases and conditions, and support healthy behaviors through knowledge, tools, partnerships, school health, and effective public health programs.',
    },
    'contributions': {
        'title': 'Contributions',
        'intro': 'You can contribute in many ways.',
        'paragraphs': [
            'Become a friend or a member of the family.',
        ],
        'image': 'images/wa17.jpeg',
        'image_alt': 'A health worker shares information during community outreach',
        'items': [
            {
                'title': 'Become a friend',
                'description': 'Join the community.',
            },
            {
                'title': 'Become a family member',
                'description': 'Become a member and take part in supporting its work.',
            },
            {
                'title': 'Support older and low-income people',
                'description': 'Give support to older people and people with low incomes who are experiencing health problems.',
            },
            {
                'title': 'Donate to dental camps',
                'description': 'Make a financial donation to our general fund to help support dental camps.',
            },
            {
                'title': 'Organize a fundraiser',
                'description': 'Organize a fundraising event or another beneficial program in support of our work.',
            },
            {
                'title': 'Sponsor a program',
                'description': 'Sponsor an awareness program, dental camp, play and stationery material distribution, or toothbrush and toothpaste distribution program.',
            },
            {
                'title': 'Give a general donation',
                'description': 'Provide any kind of general donation or support for our work.',
            },
            {
                'title': 'Spread the word',
                'description': 'Help share work by publishing or sharing information within your network.',
            },
            {
                'title': 'Volunteer in the community',
                'description': 'Volunteer on a project and help serve people in the community.',
            },
            {
                'title': 'Connect with supporters',
                'description': 'Help find new sponsors and energetic volunteers who can contribute to serving people in need in Nepal.',
            },
        ],
    },
    'health_news': {
        'title': 'Dental Health News',
        'intro': 'A record of our community, school, child welfare, health camp, and relief activities.',
        'image': 'images/wa22.jpeg',
        'image_alt': 'Community health outreach activity',
        'activities_by_year': [
            {
                'year': 2026,
                'activities': [
                    'Lekhnath Basic School, Arupata, Lekhnath',
                ],
            },
            {
                'year': 2025,
                'activities': [
                    'Buddha Dahal School for the Deaf, Damauli, Tanahun',
                ],
            },
            {
                'year': 2024,
                'activities': [
                    'Swamisadananda Gurukulam, Danda Nak, Lekhnath',
                ],
            },
            {
                'year': 2021,
                'activities': [
                    'Child Welfare and Education, Lakeside, Pokhara',
                    'Namaste Foundation, Lakeside, Pokhara',
                ],
            },
            {
                'year': 2020,
                'activities': [
                    'Chhunhup Primary School, Mustang',
                ],
            },
            {
                'year': 2019,
                'activities': [
                    'Child Welfare and Education, Lakeside, Pokhara',
                    'Shrijana School for the Deaf, Lekhnath, Kaski',
                    'Buddha Dahal School for the Deaf, Damauli, Tanahun',
                    'Laxmi Primary School, Laxmi Bazaar, Lamjung',
                    'Chhunhup Primary School, Mustang',
                    'Namaste Foundation, Lakeside, Pokhara',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Saileswari Primary School, Laxmi Bazaar, Lamjung',
                    'Bindeswori Primary School, Shyaulibazaar, Lamjung',
                ],
            },
            {
                'year': 2018,
                'activities': [
                    'Child Welfare & Education (CWE), Lakeside, Pokhara',
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Buddha Dahal School for the Deaf, Damauli, Tanahun',
                    'Sirjana Higher Secondary School for the Deaf, Lekhnath, Pokhara',
                    'Bhalam Primary School, Bhalam, Kaski',
                    'Stationery and sports materials distributed at Buddha Dahal School for the Deaf',
                    'Laxmi Primary School, Laxmi Bazaar, Lamjung',
                    'Bendheswari Primary School, Shyauli Bazaar, Lamjung',
                ],
            },
            {
                'year': 2017,
                'activities': [
                    'Child Welfare & Education (CWE), Lakeside, Pokhara',
                    'Sirjana Higher Secondary School for the Deaf, Lekhnath, Pokhara',
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Bendheswari Primary School, Shyauli Bazaar, Lamjung',
                    'Laxmi Primary School, Laxmi Bazaar, Lamjung',
                    'Buddha Deaf School, Tanahun',
                ],
            },
            {
                'year': 2016,
                'activities': [
                    'Child Welfare & Education (CWE), Lakeside, Pokhara',
                    'Dibya Jyoti Secondary School, Nawalparasi',
                    'Jana Jyoti Secondary School, Gorkha',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Saraswati Mandir Higher Secondary School, Ghalechhap, Tanahun',
                    'Bhumeswari Primary School, Dordi, Lamjung',
                    'Saileswari Primary School, Chisankhu, Lamjung',
                    'Laxmi Primary School, Laxmi Bazaar, Lamjung',
                ],
            },
            {
                'year': 2015,
                'activities': [
                    'Child Welfare & Education (CWE), Lakeside, Pokhara',
                    'Medical camp and relief-material distribution for earthquake victims',
                    'Ghyachock VDC, Gorkha',
                    'Khangsang (Beshi) VDC, Sindhuli',
                    'Kunbu Kasthali VDC, Ramechhap',
                    'Landslide victims, Lumley, Kaski',
                    'Mahendra Primary School and Manakamana Primary School, Sundar Bazaar, Lamjung',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Namaste Community Foundation, Lakeside, Pokhara',
                    'Sarada Sadan Primary School, Handikhola, Lamjung',
                ],
            },
            {
                'year': 2014,
                'activities': [
                    'Child Welfare & Education (CWE), Lakeside, Pokhara',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Students and local people of Kumbu Kasthali, Ramechhap',
                ],
            },
            {
                'year': 2013,
                'activities': [
                    'Child Welfare & Education (CWE), Lakeside, Pokhara',
                    'Rainbow Children Home, Lakeside, Pokhara',
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Kathmandu College students',
                    'EUROD Nepal',
                    'Janata Secondary School, Kungbu Kasthali, Ramechhap',
                    'Community people of Kungbu Kasthali, Ramechhap',
                    'Shree Hom Raj Lohani Sarada Higher Secondary School, Bhanu, Tanahun',
                    'Shree Saraswati Mandir Higher Secondary School, Ghalechap, Tanahun',
                    'Shree Shiva Primary School, Chandrawati, Tanahun',
                ],
            },
            {
                'year': 2012,
                'activities': [
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Rainbow Children Home, Pokhara',
                    'Sree Satyawati Devi Lower Secondary School, Bhansar, Tanahun',
                    'Kathmandu College students',
                    'EUROD Nepal, Kathmandu',
                ],
            },
            {
                'year': 2011,
                'activities': [
                    'Community people, Mirlung, Tanahun',
                    'Rainbow Children Home, Pokhara',
                    'Child Welfare & Education, Lakeside, Pokhara',
                    'Bihya Nikunja Higher School, Mirlung, Tanahun',
                    'Pal Tashi Chyyoling Monastery, Pokhara',
                ],
            },
            {
                'year': 2010,
                'activities': [
                    'Community people, Mirlung, Tanahun',
                    'Quality of Life Nepal, Sarangkot',
                    'Namaste Children Home, Lakeside, Pokhara',
                    'Onni Children Home, Dam Side, Pokhara',
                    'Tahara, Nepal, Pokhara',
                ],
            },
            {
                'year': 2009,
                'activities': [
                    'Sewa Sadan Ma. Vi., Purankot, Lamjung',
                    'Siba Sakti Primary School, Nalma, Lamjung',
                    'Child Welfare & Education, Lakeside, Pokhara',
                ],
            },
            {
                'year': 2007,
                'activities': ['Daduwa Durcha Ma. Vi., Daduwa, Lamjung'],
            },
            {
                'year': 2006,
                'activities': ['Saraswati Sadan Ma. Vi., Sindure, Lamjung'],
            },
            {
                'year': 2003,
                'activities': [
                    'Ghaleutter Kanya Ma. Vi., Bagum, Lamjung',
                    'Tribhuwan Bidyasram Ma. Vi., Bhujung, Lamjung',
                    'Pas Gaun Thanti Ma. Vi., Pasgaun, Lamjung',
                    'Community people, Bhoje, Lamjung',
                    'Suryo Daya Lower Secondary School, Ghamrang, Lamjung',
                    'Buddodaya Ma. Vi., Gilung, Lamjung',
                ],
            },
            {
                'year': 2002,
                'activities': [
                    'Annapurna Ma. Vi., Nalma, Lamjung',
                    'Sarada Ma. Vi., Maling, Lamjung',
                    'Janajyoti Ma. Vi., Baglung Pani, Lamjung',
                ],
            },
        ],
    },
    'team': {
        'title': 'Our Team',
        'intro': 'A community-led effort benefits from many perspectives and skills.',
        'paragraphs': [
            'This sample team page describes example roles, not real people or staff members. A real initiative might include community organizers, volunteers, partner organizations, and qualified health professionals.',
        ],
        'team_members': [
            {
                'role': 'Community Coordinator',
                'image': 'personal/team/coordinator.svg',
            },
            {
                'role': 'Health Resource Editor',
                'image': 'personal/team/editor.svg',
            },
            {
                'role': 'Community Volunteer',
                'image': 'personal/team/volunteer.svg',
            },
            {
                'role': 'Health Advisor',
                'image': 'personal/team/advisor.svg',
            },
        ],
    },
    'contact': {
        'title': 'Contact',
        'intro': 'I’d be happy to hear from you. Reach out by email or phone, or find me in Pokhara, Nepal.',
        'email': 'kantgrg@gmail.com',
        'phone': '+9779846155858',
        'location': 'Pokhara, Nepal',
    },
}


def base(request):
    return render(request, 'personal/home.html')


def section(request, page):
    context = SECTION_CONTENT[page]
    if page == 'contributions':
        context = {
            **context,
            'carousel_images': [
                f'images/wa{number}.jpeg' for number in range(2, 29)
            ],
        }
    return render(request, f'personal/{page}.html', context)
