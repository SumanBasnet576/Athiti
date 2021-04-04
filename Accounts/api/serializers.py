from rest_framework import serializers

from ..models import Account


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
