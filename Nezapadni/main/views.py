from django.shortcuts import render

def index(request):
    # Данные для команды
    team_members_top = [
        {"name": "Zane Sorell", "position": "CEO", "image": "smile-face.png",
         "social": {"facebook": "#", "github": "#", "linkedin": "#"}},
        {"name": "Maya Mathy", "position": "Founder", "image": "smile-face2.png",
         "social": {"facebook": "#", "github": "#", "linkedin": "#"}},
        {"name": "Alexis Jensen", "position": "CTO", "image": "smile-face3.png",
         "social": {"facebook": "#", "github": "#", "linkedin": "#"}},
    ]

    team_members_bottom = team_members_top  # можно повторить или другие

    # Логотипы партнёров
    partner_logos = [
        "logo.png",
        "logo (1).png",
        "logo (2).png",
        "logo (3).png",
        "logo (4).png",
        "logo (5).png",
    ]

    # Рендерим шаблон с контекстом
    return render(request, "pages/index.html", {
        "team_members_top": team_members_top,
        "team_members_bottom": team_members_bottom,
        "partner_logos": partner_logos,
    })


def story(request):
    return render(request, 'pages/story.html')


def vision(request):
    return render(request, 'pages/vision.html')


def parents(request):
    return render(request, 'pages/parents.html')


def courses(request):
    return render(request, 'pages/courses.html')


def display(request):
    return render(request, 'pages/display.html')


def contact(request):
    return render(request, 'pages/contact.html')


def login(request):
    return render(request, 'registration/login.html')


def sign_up(request):
    return render(request, 'registration/signup.html')


def course_detail(request):
    return render(request, 'pages/course_detail.html')


def join_community(request):
    return render(request, 'registration/signup.html')
