from rest_framework import serializers

class CustomAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['created'] = instance.created.strftime("%d - %b, %Y")
        res['update'] = instance.update.strftime("%d - %b, %Y")
        return res
