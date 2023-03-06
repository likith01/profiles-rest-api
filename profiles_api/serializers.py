from rest_framework import serializers

#from video 45
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name fiels for testing our APIView"""
    name = serializers.CharField(max_length=10)










#from video 45
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }


    def create(self, validated_data):
        """create and return a new user"""
                                        #this create_user function in models.py
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
