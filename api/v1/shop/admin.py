from django.contrib import admin
from .models import(
    About,
    Banner,
    Category,
    Client,
    File,
    Instruction,
    Member,
    Product,
    Result,
    Lesson
)
# Register your models here.

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "phone", "city", "address", "product_id")

@admin.register(File)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id","name", "file", "product_id", "banner_id", "result_id", "instruction_id", "about_id")

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ("id","product_id", "description")

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","full_name", "user_name", "telegram_id", "client_id")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name", "category_id", "description", "price", "qty")

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("id","product_id", "description")





