# eT3Cash

## Overview

eT3Cash is a financial management application designed to streamline transactions, manage user balances, and offer data insights. It combines modern web and mobile technologies with a robust backend to deliver a comprehensive solution.

---

## Features

1. **Frontend (Vue.js)**
   - Interactive user interfaces with reusable components for functionalities like:
     - **Cash In & Out**
     - **Transfer**
     - **Donations**
     - **Investments**
     - **Transactions History**
     - **Balance Inquiry**
   - Screenshots of UI components for these features.

2. **Backend (Django)**
   - APIs for handling requests related to:
     - User authentication and wallet management
     - Transactions processing (cash in, cash out, transfer, donations, investments)
     - Balance checks and history
   - Modular and scalable architecture.

3. **Database**
   - **SQL Schema**:
     - Tables for `users`, `wallets`, `transactions`, `investments`, and more.
   - **Data Warehouse Schema**:
     - Designed for analytics with dimensions (e.g., `time`, `user`) and fact tables (e.g., `transaction_facts`).

4. **ETL Pipeline**
   - Loads mock data from CSV files into the data warehouse.
   - Steps:
     - Extract: Reads data from CSV files.
     - Transform: Cleans and formats data for compatibility.
     - Load: Inserts processed data into the data warehouse.

5. **Mobile App (Flutter)**
   - Connected to Django APIs for real-time operations.
   - Reusable cards for features like:
     - Displaying transaction details
     - Balance summaries
     - Notifications
   - Screenshots of mobile interfaces.

---

## Installation

### Prerequisites

- **Frontend:**
  - Node.js and npm installed.
  - Vue.js CLI.
- **Backend:**
  - Python (3.8+), pip, and Django.
- **Database:**
  - MySQL.
- **Mobile App:**
  - Flutter SDK.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/username/eT3Cash.git
   ```

2. **Frontend Setup:**
   ```bash
   cd eT3Cash/frontend
   npm install
   npm run serve
   ```

3. **Backend Setup:**
   ```bash
   cd eT3Cash/backend
   pip install -r requirements.txt
   python manage.py runserver
   ```

4. **Database Setup:**
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```
   - Load mock data into the SQL database:
     ```bash
     python manage.py loaddata mock_data.json
     ```

5. **ETL Pipeline:**
   ```bash
   cd eT3Cash/etl
   python run_etl.py
   ```

6. **Mobile App Setup:**
   ```bash
   cd eT3Cash/mobile
   flutter pub get
   flutter run
   ```

---

## Project Structure

```
├── frontend/       # Vue.js frontend application
├── backend/        # Django backend APIs
├── database/       # SQL schema and data warehouse schema
├── etl/            # ETL scripts to load data from CSV files
├── mobile/         # Flutter mobile application
└── README.md       # Project documentation
```

---

## Screenshots

![Screenshot from 2024-12-11 17-40-08](https://github.com/user-attachments/assets/254d8109-480e-491d-82b0-ef6c25abce92)
![Screenshot from 2024-12-11 17-33-01](https://github.com/user-attachments/assets/7808082d-875d-4053-9c91-b67e9e0db984)
![Screenshot from 2024-12-12 16-08-34](https://github.com/user-attachments/assets/f1f35b68-96d1-49b0-aee2-93a0130f12fc)
![Screenshot from 2024-12-12 16-08-28](https://github.com/user-attachments/assets/5ef6dcc1-709b-44b4-855c-bbcc65b9bf4a)
![Screenshot from 2024-12-12 16-04-42](https://github.com/user-attachments/assets/6f3e8bd9-98c4-418e-9bfd-5fbad83a0e8c)
![Screenshot from 2024-12-13 17-21-12](https://github.com/user-attachments/assets/18518153-9f17-42fe-9405-46ed50f2396c)
![Screenshot from 2024-12-12 16-48-25](https://github.com/user-attachments/assets/455d20bd-890f-4bc1-a77c-14421e25a376)
![Screenshot from 2024-12-12 16-47-39](https://github.com/user-attachments/assets/e3e0c73c-1265-4822-a8a0-5a85cffe8872)


