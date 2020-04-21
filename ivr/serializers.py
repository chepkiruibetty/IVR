from rest_framework import serializers
from .models import User,UserBankDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('user_id','first_name','last_name','phone_no')

class UserBankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserBankDetails
        fields=('user_id','account_number','deposit','withdrawal','account_balance')

