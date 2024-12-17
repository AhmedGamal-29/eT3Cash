from .extract import extract_csv
from .transform import clean_customers, clean_wallets, clean_transactions
from .load import load_customers, load_wallets, load_transactions

def run_etl():
    # Extract
    customers = extract_csv("data/DimCustomer.csv")
    wallets = extract_csv("data/DimWallet.csv")
    transactions = extract_csv("data/FactTransactions.csv")
    
    # Transform
    if customers is not None:
        customers = clean_customers(customers)
    if wallets is not None:
        wallets = clean_wallets(wallets)
    if transactions is not None:
        transactions = clean_transactions(transactions)
    
    # Load
    if customers is not None:
        load_customers(customers)
    if wallets is not None:
        load_wallets(wallets)
    if transactions is not None:
        load_transactions(transactions)

    print("ETL pipeline executed successfully!")
