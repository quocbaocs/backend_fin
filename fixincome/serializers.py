from rest_framework import serializers
from .models import Treasury_Yield
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TreasuryYieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasury_Yield
        fields = ('id','asset_code','maturity','issuedate','couponrate','price','yeild')
        #fields = ('id', 'bondName', 'couponRate', 'bondPrice', 'bondYield')