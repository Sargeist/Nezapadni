from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="list"),

    # Детальная страница курса
    path("<slug:slug>/", views.course_detail, name="detail"),

    # Покупка (Stripe Checkout)
    path("<slug:slug>/purchase/", views.purchase_course, name="purchase"),

    # Stripe success (завершение покупки)
    path("<slug:slug>/success/", views.checkout_success, name="checkout_success"),

    # Добавление отзыва
    path("<slug:slug>/review/add/", views.add_review, name="add_review"),
]
