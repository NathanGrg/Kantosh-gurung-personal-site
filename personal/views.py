from django.shortcuts import render


SECTION_CONTENT = {
    'program': {
        'title': 'Dental Health Programs',
        'intro': 'Practical ideas for building confident smiles through oral health education, prevention, and access to care.',
        'paragraphs': [
            'These sample programs highlight ways communities and dental professionals can work together. They are educational examples, not services or medical advice.',
        ],
        'programs': [
            {
                'title': 'Oral Health Education',
                'description': 'Share clear, age-appropriate information about daily brushing, flossing, and keeping up with routine dental visits.',
                'image': 'images/wa10.jpeg',
                'image_alt': 'Community members take part in an oral health program',
            },
            {
                'title': 'Children’s Dental Visits',
                'description': 'Help children feel comfortable at the dentist with welcoming visits, family guidance, and positive oral-health activities.',
                'image': 'images/wa7.jpeg',
                'image_alt': 'A health worker examines a child during a dental visit',
            },
            {
                'title': 'Community Dental Outreach',
                'description': 'Connect neighborhoods with oral-health information and guidance on finding local dental services.',
                'image': 'images/wa17.jpeg',
                'image_alt': 'A health worker shares resources during community outreach',
            },
            {
                'title': 'Prevention and Early Visits',
                'description': 'Encourage regular checkups so people can discuss concerns and preventive care with a qualified dental professional.',
                'image': 'images/wa19.jpeg',
                'image_alt': 'A close-up view during a dental examination',
            },
            {
                'title': 'Dental Team Learning',
                'description': 'Support continuing learning and collaboration among dental professionals to make care more welcoming and accessible.',
                'image': 'images/wa5.jpeg',
                'image_alt': 'Community members gather for a health workshop',
            },
        ],
    },
    'objectives': {
        'title': 'Objectives',
        'intro': 'Our goal is to make good oral-health information and dental care easier to understand and access.',
        'paragraphs': [
            'These sample objectives focus on prevention, education, and stronger connections with qualified dental professionals.',
        ],
        'image': 'images/wa11.jpeg',
        'image_alt': 'Students gather for a community oral health event',
        'items': [
            {
                'title': 'Build everyday knowledge',
                'description': 'Make clear, accessible oral-health information available to children, families, and community members.',
            },
            {
                'title': 'Encourage preventive care',
                'description': 'Promote regular dental checkups and conversations with qualified professionals about prevention.',
            },
            {
                'title': 'Improve connections to care',
                'description': 'Help people learn how to find local dental services and ask about available care options.',
            },
            {
                'title': 'Create welcoming experiences',
                'description': 'Support friendly, respectful dental visits where people feel comfortable raising questions.',
            },
        ],
    },
    'contributions': {
        'title': 'Contributions',
        'intro': 'Better oral health is a shared effort, and everyone can help make dental education more approachable.',
        'paragraphs': [
            'Families, educators, dental professionals, and community groups can all help spread reliable oral-health information.',
            'The ideas below are examples only; this website does not currently offer dental services, events, or volunteer opportunities.',
        ],
        'image': 'images/wa17.jpeg',
        'image_alt': 'A health worker shares information during community outreach',
        'items': [
            {
                'title': 'Share trusted resources',
                'description': 'Help families find easy-to-understand oral-health information from reputable dental and public-health sources.',
            },
            {
                'title': 'Support learning activities',
                'description': 'Help schools or community groups make oral-health education part of their learning events.',
            },
            {
                'title': 'Connect people with care',
                'description': 'Share information about local dental clinics and ways to ask providers about appointments and services.',
            },
            {
                'title': 'Listen and improve',
                'description': 'Offer feedback on what information would make dental visits and daily oral care easier to navigate.',
            },
        ],
    },
    'health_news': {
        'title': 'Dental Health News',
        'intro': 'Dental-health topics and practical reminders for healthier smiles.',
        'featured_story': {
            'category': 'ORAL HEALTH',
            'title': 'Making a dental visit feel more comfortable',
            'excerpt': 'A welcoming dental visit starts with open communication. Sharing questions and concerns with your dental team can help you understand what to expect.',
            'reading_time': '3 min read',
            'image': 'images/wa22.jpeg',
            'image_alt': 'A dental professional examines a patient',
        },
        'articles': [
            {
                'category': 'FAMILY DENTAL CARE',
                'title': 'Helping children feel at ease at the dentist',
                'excerpt': 'A calm, supportive conversation before an appointment can help children know what to expect. Dental teams can answer questions along the way.',
                'reading_time': '3 min read',
                'image': 'images/wa7.jpeg',
                'image_alt': 'A health worker examines a child during a dental visit',
            },
            {
                'category': 'COMMUNITY',
                'title': 'Taking oral-health learning into the community',
                'excerpt': 'Community events can create friendly opportunities to learn about oral health and find out where to seek professional dental care.',
                'reading_time': '2 min read',
                'image': 'images/wa10.jpeg',
                'image_alt': 'Community members take part in an oral health program',
            },
            {
                'category': 'PREVENTION',
                'title': 'Keep routine dental checkups on your calendar',
                'excerpt': 'Regular visits give you time to discuss your oral health and ask a dental professional what care is right for you.',
                'reading_time': '3 min read',
                'image': 'images/wa19.jpeg',
                'image_alt': 'A close-up view during a dental examination',
            },
        ],
        'disclaimer': 'General educational information only; it is not a diagnosis or a substitute for advice from your dentist. Ask a qualified dental professional about your individual needs.',
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
        'email': 'nathangrg30@gmail.com',
        'phone': '+9779819129536',
        'location': 'Pokhara, Nepal',
    },
}


def base(request):
    return render(request, 'personal/home.html')


def section(request, page):
    return render(request, f'personal/{page}.html', SECTION_CONTENT[page])
