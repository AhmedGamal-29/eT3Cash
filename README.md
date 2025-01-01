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
     - 
   ![Screenshot from 2024-12-13 17-41-58](https://github.com/user-attachments/assets/79adbc85-d303-4c98-886b-b5ad1f004301)
![Screenshot from 2024-12-13 17-40-48](https://github.com/user-attachments/assets/ffabb535-49c0-4f58-9a8b-dbff0f329c3b)
![Screenshot from 2024-12-13 17-39-56](https://github.com/user-attachments/assets/c739d08f-74c2-40a8-9c55-41c1709db8d5)
![Screenshot from 2024-12-13 17-38-11](https://github.com/user-attachments/assets/33bef909-da66-4b7f-8582-21a650226a90)


2. **Backend (Django)**
   - APIs for handling requests related to:
     - User authentication and wallet management
     - Transactions processing (cash in, cash out, transfer, donations, investments)
     - Balance checks and history
       
3. **Database**
   - **SQL Schema**:
     - Tables for `users`, `wallets`, `transactions`, `investments`, and more.
   - **Data Warehouse Schema**:
     - Designed for analytics with dimensions (e.g., `time`, `user`) and fact tables (e.g., `transaction_facts`).
     - 
     - ![Screenshot from 2024-12-11 17-40-08](https://github.com/user-attachments/assets/f68eb155-f852-49fb-a7b4-70fbca062036)
![Screenshot from 2024-12-11 17-33-01](https://github.com/user-attachments/assets/923859da-dfde-4167-81fd-32c7acdd7264)


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
     - 
     ![Screenshot from 2024-12-12 16-08-43](https://github.com/user-attachments/assets/69193b79-567d-40c9-80d9-84714fdf6cda)
![Screenshot from 2024-12-12 16-08-34](https://github.com/user-attachments/assets/9eeadab9-5d08-4534-be3d-65003fd12085)
![Screenshot from 2024-12-12 16-08-28](https://github.com/user-attachments/assets/38d225be-d6b5-47f7-8626-c4d1895016eb)
![Screenshot from 2024-12-12 16-04-42](https://github.com/user-attachments/assets/8bfc1fc0-f5b0-4094-b2d2-5f631dd87fb9)

  

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
   npm run dev
   ```

3. **Backend Setup:**
   ```bash
   cd eT3Cash/backend
   pip install -r requirements.txt
   python manage.py runserver
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
├── SQL/       # SQL schema and data warehouse schema
├── etl/            # ETL scripts to load data from CSV files
├── mobile/         # Flutter mobile application
└── README.md       # Project documentation
```
