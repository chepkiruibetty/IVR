from rest_framework import serializers
from .models import UserBankDetails

class UserBankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserBankDetails
        fields=('user_id','account_number','deposit','withdrawal','account_balance')