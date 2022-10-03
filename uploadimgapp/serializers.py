from dataclasses import field
from rest_framework import serializers
from .models import profile

class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = "__all__"

    def validate_picture(self, value):
        # print(value.size)
        MAX_FILE_SIZE = 500000
        if value.size > MAX_FILE_SIZE:
            raise serializers.ValidationError(" Image Size is greater than 500kb ..")
        return value