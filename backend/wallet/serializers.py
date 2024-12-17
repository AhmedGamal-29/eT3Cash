from rest_framework import serializers
from .models import Transaction, Wallet, CustomUser

class TransactionSerializer(serializers.ModelSerializer):
    symbol = serializers.CharField(required=False)  
    investment_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, read_only=True)  # Price at transaction, set by the view

    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'recipient', 'date', 'symbol', 'investment_price']

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)