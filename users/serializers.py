from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'full_name', 'phone', 'address', 'role', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        errors = {}

        if not email:
            errors['email'] = ["This field is required."]
        if not password:
            errors['password'] = ["This field is required."]

        if errors:
            raise serializers.ValidationError(errors)

        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError({"non_field_errors": ["Invalid credentials"]})

        if not user.is_active:
            raise serializers.ValidationError({"non_field_errors": ["User is inactive"]})

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'full_name', 'phone', 'address', 'role']
