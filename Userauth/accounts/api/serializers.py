from rest_framework import serializers 
from accounts.models import Account


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'})

    class Meta:
        model = Account
        fields = ['email','username','password','password2']

        extra_kwargs = {
            'password': {'write_only':True},
            'password2': {'write_only':True}
        }

    def save(self):
        
        account = Account(email=self.validated_data['email'],username=self.validated_data['username'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password:"Passwords should match"})

        account.set_password(password)
        account.save()
        return account