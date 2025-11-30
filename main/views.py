from django.shortcuts import render, redirect


def index(request):
    # Данные для команды
    team_members_top = [
        {
            "name": "Zane Sorell",
            "position": "CEO",
            "image": "smile-face.png",
            "social": {"facebook": "#", "github": "#", "linkedin": "#"},
        },
        {
            "name": "Maya Mathy",
            "position": "Founder",
            "image": "smile-face2.png",
            "social": {"facebook": "#", "github": "#", "linkedin": "#"},
        },
        {
            "name": "Alexis Jensen",
            "position": "CTO",
            "image": "smile-face3.png",
            "social": {"facebook": "#", "github": "#", "linkedin": "#"},
        },
    ]

    # Можно повторить верхних, а можно сделать других людей
    team_members_bottom = team_members_top

    # Логотипы партнёров
    partner_logos = [
        "logo.png",
        "logo (1).png",
        "logo (2).png",
        "logo (3).png",
        "logo (4).png",
        "logo (5).png",
    ]

    return render(
        request,
        "pages/index.html",
        {
            "team_members_top": team_members_top,
            "team_members_bottom": team_members_bottom,
            "partner_logos": partner_logos,
        },
    )


def story(request):
    return render(request, "pages/story.html")


def vision(request):
    return render(request, "pages/vision.html")


def parents(request):
    return render(request, "pages/parents.html")


def contact(request):
    return render(request, "pages/contact.html")


def join_community(request):
    """
    Если где-то в шаблонах есть {% url 'join_community' %},
    логично отправлять пользователя на регистрацию.
    """
    return redirect("signup")  # имя url из accounts/urls.py
