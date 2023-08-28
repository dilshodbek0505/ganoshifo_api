from rest_framework import serializers
from api.v1.utils.serializers import CustomAbstractSerializer
from .models import (
    About,
    Banner,
    Category,
    Client,
    File,
    Instruction,
    Product,
    Result,
    Member,
    Lesson

)

class MemberSerializer(CustomAbstractSerializer):
    class Meta:
        model = Member
        fields = ("id","full_name","user_name", "telegram_id", "client_id")

    def create(self, validated_data):
        member, _ = Member.objects.get_or_create(**validated_data)
        member.save()
        return member


class ResultSerializer(CustomAbstractSerializer):
    class Meta:
        model = Result
        fields = ("id","product_id","description")

    def to_representation(self, instance):
        res = super().to_representation(instance)
        files = File.objects.select_related("banner_id", "product_id", "result_id", "instruction_id", "about_id").filter(result_id_id = instance.id)
        context = []
        for file in files:
            context.append(file.file.path)
        res.update({
            "file": context
        })
        return res
    
class AboutSerializer(CustomAbstractSerializer):
    class Meta:
        model = About
        fields = ("id", "name", "description")
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        files = File.objects.select_related("banner_id", "product_id", "result_id", "instruction_id", "about_id").filter(about_id_id = instance.id)
        context = []
        for file in files:
            context.append(file.file.path)
        res.update({
            "file": context
        })
        return res
    
class BannerSerializer(CustomAbstractSerializer):
    class Meta:
        model = Banner
        fields = ("id","name", "description")

    def to_representation(self, instance):
        res = super().to_representation(instance)
        files = File.objects.select_related("banner_id", "product_id", "result_id", "instruction_id", "about_id").filter(banner_id_id = instance.id)
        context = []
        for file in files:
            context.append(file.file.path)
        res.update({
            "file": context
        })
        return res

class CategorySerializer(CustomAbstractSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")

class ClientSerializer(CustomAbstractSerializer):
    class Meta:
        model = Client
        fields = ("id", "first_name", "last_name", "phone", "city", "address", "product_id")
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['product_id'] = {
            "id" : instance.product_id.id,
            "name" : instance.product_id.name,
            "category" : instance.product_id.category_id.name,
            "qty" : instance.product_id.qty
        }
        return res

class FileSerialize(CustomAbstractSerializer):
    class Meta:
        model = File
        fields = ("id", "name", "file", "banner_id", "product_id", "result_id", "instruction_id", "about_id", "lesson_id")
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['file'] = instance.file.path
        if instance.banner_id:
            res['banner_id'] = instance.banner_id.name
        if instance.product_id:
            res['product_id'] = instance.product_id.name
        if instance.result_id:
            res['result_id'] = instance.result_id.product_id.name
        if instance.instruction_id:
            res['instruction_id'] = instance.instruction_id.product_id.name
        if instance.about_id:
            res['about_id'] = instance.about_id.name
        if instance.lesson_id:
            res['lesson_id'] = instance.lesson_id.name
        return res

class LessonSerialize(CustomAbstractSerializer):
    file = FileSerialize(many = True, read_only = True)
    class Meta:
        model = Lesson
        fields = ("id", "name", "description","file")

class InstructionSerializer(CustomAbstractSerializer):
    file = FileSerialize(read_only = True, many = True)
    class Meta:
        model = Instruction
        fields = ("id", "product_id", "description",'file')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res

class ProductSerializer(CustomAbstractSerializer):
    file = FileSerialize(many = True, read_only = True)
    instruction = InstructionSerializer(many = True, read_only = True)
    class Meta:
        model = Product
        fields = ("id", "name", "category_id", "description", "price", "qty", 'file', 'instruction')
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['category_id'] = instance.category_id.name
        return res
