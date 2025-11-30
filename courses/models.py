from django.db import models
from django.conf import settings
from django.utils.text import slugify


# ---------------------------------------
# COURSE
# ---------------------------------------
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="courses/")
    created_at = models.DateTimeField(auto_now_add=True)

    learning_points = models.TextField(blank=True)

    instructor = models.ForeignKey(
        "Instructor",
        on_delete=models.SET_NULL,
        null=True,
        related_name="courses"
    )

    def learning_points_list(self):
        return [p.strip() for p in self.learning_points.split("\n") if p.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ---------------------------------------
# CATEGORY
# ---------------------------------------
class Category(models.Model):
    course = models.ForeignKey(
        Course,
        related_name="categories",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.course.title} – {self.title}"


# ---------------------------------------
# LESSON (ВТОРОЙ УРОВЕНЬ)
# ---------------------------------------
class Lesson(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="lessons",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# ---------------------------------------
# SUBLESSON (ТРЕТИЙ УРОВЕНЬ)
# ---------------------------------------
class SubLesson(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        related_name="sublessons",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)

    # универсальный контент-блок:
    video = models.FileField(upload_to="sublesson/videos/", null=True, blank=True)
    text = models.TextField(blank=True)
    file = models.FileField(upload_to="sublesson/files/", null=True, blank=True)

    def __str__(self):
        return self.title


# ---------------------------------------
# COURSE PURCHASE
# ---------------------------------------
class CoursePurchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="purchases"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="purchases"
    )
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} owns {self.course.title}"


# ---------------------------------------
# REVIEW
# ---------------------------------------
class Review(models.Model):
    course = models.ForeignKey(
        Course,
        related_name="reviews",
        on_delete=models.CASCADE
    )
    reviewer_name = models.CharField(max_length=120)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} — {self.rating}"


# ---------------------------------------
# INSTRUCTOR
# ---------------------------------------
class Instructor(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to="instructors/", blank=True, null=True)
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=1)
    courses_count = models.PositiveIntegerField(default=0)
    students_count = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)

    skills = models.TextField(blank=True)

    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def skills_list(self):
        return [s.strip() for s in self.skills.split(",") if s.strip()]

    def __str__(self):
        return self.name
