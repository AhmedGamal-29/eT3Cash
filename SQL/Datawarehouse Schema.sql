CREATE TABLE DimCustomer (
  `customer_id` int NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
)


CREATE TABLE DimWallet (
    wallet_id INT PRIMARY KEY,
    customer_id INT,
    balance DECIMAL(15, 2),
    created_at TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES DimCustomer(customer_id)
);

CREATE TABLE FactTransactions (
  `transaction_id` int NOT NULL,
  `transaction_date` timestamp NULL DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `transaction_type` varchar(50) DEFAULT NULL,
  `amount` decimal(15,2) DEFAULT NULL,
  `wallet_id` int DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `customer_id` (`customer_id`),
  KEY `wallet_id` (`wallet_id`),
  CONSTRAINT `FactTransactions_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `eT3Cash`.`Customer` (`customer_id`),
  CONSTRAINT `FactTransactions_ibfk_2` FOREIGN KEY (`wallet_id`) REFERENCES `eT3Cash`.`Wallet` (`wallet_id`)
)

CREATE TABLE DimTransactionType(
  `transaction_type_id` int NOT NULL,
  `transaction_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`transaction_type_id`)
)

CREATE TABLE DimTime (
  `time_id` int NOT NULL,
  `year` int DEFAULT NULL,
  `month` int DEFAULT NULL,
  `day` int DEFAULT NULL,
  PRIMARY KEY (`time_id`)
)
