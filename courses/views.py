from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

from .models import Course, Category, Review, CoursePurchase

# Stripe (если установлен)
try:
    import stripe
except ImportError:
    stripe = None

if stripe and hasattr(settings, "STRIPE_SECRET_KEY"):
    stripe.api_key = settings.STRIPE_SECRET_KEY


# ---------------------------------------
# Проверка владения курсом
# ---------------------------------------
def user_owns_course(user, course):
    if not user.is_authenticated:
        return False
    return CoursePurchase.objects.filter(user=user, course=course).exists()


# ---------------------------------------
# Список курсов
# ---------------------------------------
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


# ---------------------------------------
# Детальная страница курса
# ---------------------------------------
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    owns = user_owns_course(request.user, course)

    categories = course.categories.prefetch_related("lessons")
    reviews = course.reviews.all().order_by("-created_at")

    avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"] or 0
    review_count = reviews.count()

    return render(request, "courses/course_detail.html", {
        "course": course,
        "categories": categories,
        "reviews": reviews,
        "avg_rating": avg_rating,
        "review_count": review_count,
        "learning_points": course.learning_points_list(),
        "owns": owns
    })


# ---------------------------------------
# Добавление отзыва (только владельцы)
# ---------------------------------------
@login_required
def add_review(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if not user_owns_course(request.user, course):
        return redirect("courses:detail", slug=slug)

    if request.method == "POST":
        Review.objects.create(
            course=course,
            reviewer_name=request.user.first_name or request.user.email,
            rating=request.POST.get("rating"),
            text=request.POST.get("text")
        )

    return redirect("courses:detail", slug=slug)


# ---------------------------------------
# Покупка курса
# ---------------------------------------
@login_required
def purchase_course(request, slug):
    course = get_object_or_404(Course, slug=slug)

    # Если курс уже куплен → просто открыть
    if user_owns_course(request.user, course):
        return redirect("courses:detail", slug=slug)

    # Stripe не установлен → имитация оплаты
    if not stripe or not getattr(settings, "STRIPE_SECRET_KEY", None):
        return redirect("courses:checkout_success", slug=slug)

    # Stripe checkout
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        customer_email=request.user.email,
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": course.title},
                "unit_amount": int(course.price * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=request.build_absolute_uri(
            reverse("courses:checkout_success", args=[course.slug])
        ),
        cancel_url=request.build_absolute_uri(
            reverse("courses:detail", args=[course.slug])
        ),
    )

    return redirect(checkout_session.url)


# ---------------------------------------
# Страница успешной покупки
# ---------------------------------------
@login_required
def checkout_success(request, slug):
    course = get_object_or_404(Course, slug=slug)

    purchase, created = CoursePurchase.objects.get_or_create(
        user=request.user,
        course=course
    )

    # Только если покупка была новая → отправляем письмо
    if created:
        try:
            send_mail(
                subject="Your Nezapadni Course Purchase",
                message=f"Thank you! You now have full access to: {course.title}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=True,
            )
        except:
            pass

    return render(request, "courses/checkout_success.html", {"course": course})
