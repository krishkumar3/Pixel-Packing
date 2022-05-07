from rest_framework import serializers

from ImageProcessingCore.models import Core
class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = "__all__"
