# from rest_framework import serializers
#
# from . import models
#
#
# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Account
#         fields = ['id', 'email', 'username', 'password', 'profileImage']
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = models.Account(
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
