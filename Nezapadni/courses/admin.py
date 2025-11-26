from django.contrib import admin
from .models import Course, Instructor, Category, Lesson, SubLesson, Review


# ---------------------------------------
# SUBLESSON INLINE (подуроки)
# ---------------------------------------
class SubLessonInline(admin.StackedInline):
    model = SubLesson
    extra = 1
    fields = ("title", "video", "text", "file")
    verbose_name = "SubLesson"
    verbose_name_plural = "SubLessons"


# ---------------------------------------
# LESSON ADMIN (содержит SubLessons)
# ---------------------------------------
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "duration")
    search_fields = ("title",)
    list_filter = ("category",)
    inlines = [SubLessonInline]


# ---------------------------------------
# LESSON INLINE (вставляется в Category)
# ---------------------------------------
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1
    show_change_link = True
    fields = ("title", "duration")
    verbose_name = "Lesson"
    verbose_name_plural = "Lessons"


# ---------------------------------------
# CATEGORY ADMIN
# ---------------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    list_filter = ("course",)
    search_fields = ("title",)
    inlines = [LessonInline]


# ---------------------------------------
# CATEGORY INLINE (вставляется в Course)
# ---------------------------------------
class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1
    show_change_link = True
    verbose_name = "Category"
    verbose_name_plural = "Categories"


# ---------------------------------------
# COURSE ADMIN
# ---------------------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "created_at")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CategoryInline]


# ---------------------------------------
# INSTRUCTOR ADMIN
# ---------------------------------------
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "rating", "students_count")
    search_fields = ("name",)
    list_filter = ("rating",)


# ---------------------------------------
# REVIEW ADMIN
# ---------------------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer_name", "rating", "course", "created_at")
    search_fields = ("reviewer_name", "text")
    list_filter = ("rating", "created_at")
