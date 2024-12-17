from etl_app.models import DimCustomer, DimWallet, FactTransactions, DimTime, DimTransactionType

def load_customers(data):
    for _, row in data.iterrows():
        DimCustomer.objects.update_or_create(
            customer_id=row['customer_id'],
            defaults={
                'username': row['username'],
                'customer_name': row['customer_name'],
                'email': row['email'],
                'phone_number': row['phone_number'],
                'created_at': row['created_at'],
            }
        )
    print("Customers loaded successfully.")

def load_wallets(data):
    for _, row in data.iterrows():
        DimWallet.objects.update_or_create(
            wallet_id=row['wallet_id'],
            defaults={
                'customer_id': row['customer_id'],
                'balance': row['balance'],
                'created_at': row['created_at'],
            }
        )
    print("Wallets loaded successfully.")
    
def load_transactions(data):
    for _, row in data.iterrows():
        FactTransactions.objects.update_or_create(
            transaction_id=row['transaction_id'],
            defaults={
                'transaction_date': row['transaction_date'],
                'customer_id': row['customer_id'],
                'transaction_type': row['transaction_type'],
                'amount': row['amount'],
                'wallet_id': row['wallet_id'],
            }
        )
    print("Transactions loaded successfully.")
