import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Configurations
NUM_CUSTOMERS = 100000       # Number of customers
NUM_WALLETS = 100000         # Number of wallets
NUM_TRANSACTIONS = 500000    # Number of transactions
START_DATE = datetime(2023, 1, 1)  # Start date for transactions
END_DATE = datetime(2024, 1, 1)

# Generate DimCustomer.csv
def generate_customers():
    customers = []
    for i in range(1, NUM_CUSTOMERS + 1):
        customers.append({
            "customer_id": i,
            "username": fake.user_name(),
            "customer_name": fake.name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "created_at": fake.date_time_between(START_DATE, END_DATE)
        })
    return pd.DataFrame(customers)

# Generate DimWallet.csv
def generate_wallets():
    wallets = []
    for i in range(1, NUM_WALLETS + 1):
        wallets.append({
            "wallet_id": i,
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "balance": round(random.uniform(1000, 10000), 2),
            "created_at": fake.date_time_between(START_DATE, END_DATE)
        })
    return pd.DataFrame(wallets)

# Generate DimTransactionType.csv
def generate_transaction_types():
    transaction_types = [
        {"transaction_type_id": 1, "transaction_type": "cash_in"},
        {"transaction_type_id": 2, "transaction_type": "cash_out"},
        {"transaction_type_id": 3, "transaction_type": "transfer"},
        {"transaction_type_id": 4, "transaction_type": "donation"},
        {"transaction_type_id": 5, "transaction_type": "investment"},
    ]
    return pd.DataFrame(transaction_types)

# Generate FactTransactions.csv
def generate_transactions():
    transactions = []
    for i in range(1, NUM_TRANSACTIONS + 1):
        transactions.append({
            "transaction_id": i,
            "transaction_date": fake.date_time_between(START_DATE, END_DATE),
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "transaction_type": random.choice(["cash_in", "cash_out", "transfer", "donation", "investment"]),
            "amount": round(random.uniform(50, 5000), 2),
            "wallet_id": random.randint(1, NUM_WALLETS),
        })
    return pd.DataFrame(transactions)

# Generate DimTime.csv
def generate_time_table():
    dates = pd.date_range(START_DATE, END_DATE)
    time_table = []
    for date in dates:
        time_table.append({
            "date_key": date.date(),
            "year": date.year,
            "month": date.month,
            "day": date.day,
            "quarter": (date.month - 1) // 3 + 1,
            "weekday": date.weekday()
        })
    return pd.DataFrame(time_table)

# Generate CSV files
generate_customers().to_csv("data/DimCustomer.csv", index=False)
generate_wallets().to_csv("data/DimWallet.csv", index=False)
generate_transaction_types().to_csv("data/DimTransactionType.csv", index=False)
generate_transactions().to_csv("data/FactTransactions.csv", index=False)
generate_time_table().to_csv("data/DimTime.csv", index=False)

print("CSV files generated successfully!")
