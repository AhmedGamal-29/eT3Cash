from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Wallet, Transaction
from .serializers import TransactionSerializer, UserLoginSerializer, UserRegisterSerializer,WalletSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login
from .models import CustomUser
from rest_framework.permissions import AllowAny
User = get_user_model()
from django.utils.html import format_html
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class APIListView(APIView):
    def get(self, request):
        # Define the API URLs including the new market data endpoint
        api_urls = {
            "User Registration": "/api/register/",
            "User Login": "/api/login/",
            "Check Balance": "/api/check-balance/",
            "Cash In": "/api/cash-in/",
            "Cash Out": "/api/cash-out/",
            "Transfer": "/api/transfer/",
            "Donate": "/api/donate/",
            "Invest": "/api/invest/",
            "Transaction History": "/api/transactions/",
            "Market Data": "/api/market-data/",  # New endpoint for market data
        }

        # Create an HTML representation of the API buttons
        html_content = '''
            <html>
                <head>
                    <title>API Endpoints</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            margin: 20px;
                        }
                        .button {
                            display: inline-block;
                            padding: 10px 20px;
                            margin: 5px;
                            font-size: 16px;
                            color: white;
                            background-color: #007BFF;
                            border: none;
                            border-radius: 5px;
                            text-decoration: none;
                        }
                        .button:hover {
                            background-color: #0056b3;
                        }
                    </style>
                </head>
                <body>
                    <h1>API Endpoints</h1>
                    <div>
        '''
        
        # Create buttons for each API URL
        for name, url in api_urls.items():
            html_content += f'<a class="button" href="{url}">{name}</a>'
        
        html_content += '''
                    </div>
                </body>
            </html>
        '''
        
        # Return the HTML response
        return HttpResponse(html_content)



class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            Wallet.objects.create(user=user)

            return Response({
                "message": "User registered successfully",
                "user_id": user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                token, created = Token.objects.get_or_create(user=user)  # Retrieve or create the token
                return Response({
                    "message": "Login successful",
                    "user_id": user.id,
                    "token": token.key 
                }, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckBalanceView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request, *args, **kwargs):
        wallet = Wallet.objects.get(user=request.user)
        serializer = WalletSerializer(wallet)
        return Response({'balance': serializer.data['balance']})

class CashInView(generics.CreateAPIView):
    
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            wallet = Wallet.objects.get(user=request.user)
            wallet.balance += serializer.validated_data['amount']
            wallet.save()
            Transaction.objects.create(wallet=wallet, transaction_type='cash_in', amount=serializer.validated_data['amount'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CashOutView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            wallet = Wallet.objects.get(user=request.user)
            if wallet.balance >= serializer.validated_data['amount']:
                wallet.balance -= serializer.validated_data['amount']
                wallet.save()
                Transaction.objects.create(wallet=wallet, transaction_type='cash_out', amount=serializer.validated_data['amount'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransferView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if the user's wallet exists
            try:
                wallet = Wallet.objects.get(user=request.user)
            except Wallet.DoesNotExist:
                return Response({'error': 'User does not have a wallet'}, status=status.HTTP_404_NOT_FOUND)


            # Extract recipient username
            recipient_full = str(serializer.validated_data['recipient'])
            recipient_username = recipient_full.split("'")[0]  

            # Retrieve recipient's CustomUser
            recipient_user = get_object_or_404(CustomUser, username=recipient_username)
            

            try:
                recipient_wallet = Wallet.objects.get(user=recipient_user)
            except Wallet.DoesNotExist:
                return Response({'error': f'No wallet found for recipient: {recipient_user}'}, status=status.HTTP_404_NOT_FOUND)

            # Check for sufficient balance
            if wallet.balance >= serializer.validated_data['amount']:
                wallet.balance -= serializer.validated_data['amount']
                recipient_wallet.balance += serializer.validated_data['amount']
                wallet.save()
                recipient_wallet.save()
                
                # Create transaction record
                Transaction.objects.create(
                    wallet=wallet,
                    transaction_type='transfer',
                    amount=serializer.validated_data['amount'],
                    recipient=recipient_wallet
                )
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            wallet = Wallet.objects.get(user=request.user)
            if wallet.balance >= serializer.validated_data['amount']:
                wallet.balance -= serializer.validated_data['amount']
                wallet.save()
                Transaction.objects.create(wallet=wallet, transaction_type='donation', amount=serializer.validated_data['amount'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mock data structure for available investments
mock_investments = {
    "AAPL": {"price": 150.0, "name": "Apple Inc."},
    "GOOGL": {"price": 2800.0, "name": "Alphabet Inc."},
    "TSLA": {"price": 700.0, "name": "Tesla, Inc."},
    "Gold": {"price": 3500, "name": "Jewellery, Inc."},
}

class InvestmentMarketView(APIView):
    """Fetch available investment options with mock data."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return mock investment data."""
        return Response(mock_investments)

class InvestView(generics.CreateAPIView):
    """Simulates an investment transaction."""
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            wallet = Wallet.objects.get(user=request.user)
            invest_user = get_object_or_404(User, username='invest')
            invest_wallet = get_object_or_404(Wallet, user=invest_user)
            amount = serializer.validated_data['amount']
            symbol = serializer.validated_data['symbol']  # e.g., "AAPL"
            
            # Validate if the investment symbol exists
            if symbol not in mock_investments:
                return Response({'error': 'Invalid investment symbol'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Get mock price for the investment
            investment_price = mock_investments[symbol]["price"]

            # Check if the user has sufficient balance
            if wallet.balance >= amount:
                # Deduct from user wallet and add to investment wallet
                wallet.balance -= amount
                invest_wallet.balance += amount
                wallet.save()
                invest_wallet.save()

                # Record transaction with investment details
                Transaction.objects.create(
                    wallet=wallet,
                    transaction_type='investment',
                    amount=amount,
                    investment_price=investment_price,
                    symbol=symbol,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        wallet = Wallet.objects.get(user=self.request.user)
        return Transaction.objects.filter(wallet=wallet)

