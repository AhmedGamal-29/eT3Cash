def clean_customers(data):
    """Clean customer data."""
    # Drop duplicates
    data = data.drop_duplicates()
    
    # Drop rows with missing essential values
    data = data.dropna(subset=['customer_id', 'username', 'email'])
    
    # Validate email format
    data = data[data['email'].str.contains('@')]
    
    print("Customer data cleaned successfully.")
    return data

def clean_wallets(data):
    """Clean wallet data."""
    # Replace negative balances with 0
    data['balance'] = data['balance'].apply(lambda x: max(x, 0))
    print("Wallet data cleaned successfully.")
    return data

def clean_transactions(data):
    """Clean transaction data."""
    # Ensure transaction amounts are positive
    data = data[data['amount'] > 0]
    
    print("Transaction data cleaned successfully.")
    return data
