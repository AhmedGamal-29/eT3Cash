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

### Frontend (Vue.js)
1. **Cash In/Out:**
   - Description and screenshot.
2. **Transfer:**
   - Description and screenshot.
3. **Donations:**
   - Description and screenshot.

### Mobile App (Flutter)
1. **Dashboard:**
   - Description and screenshot.
2. **Transaction History:**
   - Description and screenshot.
3. **Investment Overview:**
   - Description and screenshot.

---

## Contribution Guidelines

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Contact

For any inquiries or issues, contact us at [email@example.com](mailto:email@example.com).

