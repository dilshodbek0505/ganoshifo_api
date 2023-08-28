from django.db import models
from api.v1.utils.models import CustomAbstractModel
# Create your models here.

class Lesson(CustomAbstractModel):
    name = models.CharField(max_length=255, help_text="Darslikning nomi")
    description= models.TextField(help_text="Darslik uchun qo'shimcha tarif")

    def __str__(self) -> str:
        return self.name

class Banner(CustomAbstractModel):
    name = models.CharField(max_length=255, help_text="Reklama sarlavhasi")
    description = models.TextField(help_text="Bu yerga reklama matni")

    def __str__(self) -> str:
        return self.name

class Category(CustomAbstractModel):
    name = models.CharField(max_length=255, help_text="Kategoriya nomi")

    def __str__(self) -> str:
        return self.name

class Product(CustomAbstractModel):
    name = models.CharField(max_length=255, help_text="Maxsulotning nomini kiriting")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Kategoriyani tanlang")
    description = models.TextField(help_text="Maxsulot haqida")
    price = models.PositiveBigIntegerField(default=0, help_text="Maxsulot narxini kiriting (so'mda)")
    qty = models.PositiveIntegerField(help_text="Maxsulotning miqdorini kiriting")
   
    def __str__(self) -> str:
        return self.name

class Result(CustomAbstractModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,  help_text="Maxsulotni tanlang")
    description = models.TextField(help_text="Natijaga tarif bering")

    def __str__(self) -> str:
        return self.product_id.name

class Instruction(CustomAbstractModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, help_text="Maxsulotning tanlang", related_name="instruction")
    description = models.TextField(help_text="Qo'llanma haqida matin kiriting")

    def __str__(self) -> str:
        return self.product_id.name

class About(CustomAbstractModel):
    name = models.CharField(max_length=255, help_text="Kampaniya nomini yozing")
    description = models.TextField(help_text="Kamnaiya haqida yozing")

    def __str__(self) -> str:
        return self.name

class File(CustomAbstractModel):
    name = models.CharField(max_length=255, help_text="File nomini kiriting")
    file = models.FileField(upload_to="files/", help_text="Rasim yoki video yuklang")
    banner_id = models.ForeignKey(Banner, on_delete=models.CASCADE, blank=True, null=True, related_name='file',help_text="Reklamani tanlang (ixtyoriy)")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True,related_name='file', help_text="Maxsulotning tanlang (ixtyoriy)")
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE, blank=True, null=True, related_name='file' ,help_text="Maxsulot natijasini tanlang (ixtyoriy)")
    instruction_id = models.ForeignKey(Instruction, on_delete=models.CASCADE, blank=True, null=True, related_name='file', help_text="Dorini ishlatish bo'yicha qo'llamani tanlang (ixtyoriy)")
    about_id = models.ForeignKey(About, on_delete=models.CASCADE, blank=True, null=True, related_name='file', help_text="Kampaniya nomini tanlang (ixtyoriy)")
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank = True, null = True, related_name='file',help_text="Darslikni tanlang (ixtyoriy)")

    def __str__(self) -> str:
        return self.name
    
class Client(CustomAbstractModel):
    CITY = (
        ("Toshkent shahar", "Toshkent shahar"),
        ("Toshkent viloyati", "Toshkent viloyati"),
        ("Andijon", "Andijon"),
        ("Buxoro", "Buxoro"),
        ("Farg'ona", "Farg'ona"),
        ("Jizzax", "Jizzax"),
        ("Xorazm", "Xorazm"),
        ("Namangan", "Namangan"),
        ("Navoiy", "Navoiy"),
        ("Qashqadaryo", "Qashqadaryo"),
        ("Surxandaryo", "Surxandaryo"),
        ("Sirdaryo", "Sirdaryo"),
        ("Samarqand", "Samarqand"),
        ("Qoraqalpog'istion Respublikasi", "Qoraqalpog'istion Respublikasi"),
    )
    first_name = models.CharField(max_length=255, help_text="Foydalanuvchining ismi")
    last_name = models.CharField(max_length=255, help_text="Foydalanuvchining familiyasi")
    phone = models.CharField(max_length=13, help_text="Foydalanuvchining telfon raqami")
    city = models.CharField(max_length=50, choices=CITY, help_text="Foydalanuvchining viloyatini tanlang")
    address = models.TextField(help_text="Foydalanuvchining aniq manzilini kiriting")
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, help_text="Maxsulotni tanlang")

class Member(CustomAbstractModel):
    full_name = models.CharField(max_length=255, help_text="Foydalanuvchining telegramdagi to'lq ismi")
    user_name = models.CharField(max_length=255, blank=True, null=True, help_text="Foydalanuvchining telegramdagi username")
    telegram_id = models.PositiveIntegerField(default=0, help_text="Foydalanuvchining telegram idsi")
    client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
