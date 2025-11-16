from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

User = get_user_model()


@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        role = request.POST.get("role", "user")

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Проверка совпадения паролей
        if password1 != password2:
            return JsonResponse({"success": False, "error": "Пароли не совпадают."})

        # Проверка существующего email
        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "error": "Пользователь с таким email уже существует."})

        # Создание пользователя
        try:
            user = User.objects.create_user(
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
                role=role,
            )
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": f"Ошибка при создании пользователя: {str(e)}"})

    return render(request, "registration/signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # аутентификация по email (через кастомный backend / USERNAME_FIELD)
        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.error(request, "Invalid email or password")
            return redirect("login")

        login(request, user)
        messages.success(request, "Login successful")
        return redirect("home")   # у тебя в base.html используются url 'home'

    return render(request, "registration/login.html")
