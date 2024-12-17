CREATE TABLE `Wallet` (
  `wallet_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `balance` decimal(15,2) DEFAULT '0.00',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`wallet_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `Wallet_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `Customer` (`customer_id`) ON DELETE CASCADE
)

CREATE TABLE `Transactions` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `wallet_id` int NOT NULL,
  `transaction_type` enum('cashin','cashout','transfer','donate','invest') NOT NULL,
  `amount` decimal(15,2) NOT NULL,
  `recipient_wallet_id` int DEFAULT NULL,
  `transaction_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  KEY `wallet_id` (`wallet_id`),
  KEY `recipient_wallet_id` (`recipient_wallet_id`),
  KEY `transaction_date` (`transaction_date`),
  CONSTRAINT `Transactions_ibfk_1` FOREIGN KEY (`wallet_id`) REFERENCES `Wallet` (`wallet_id`) ON DELETE CASCADE,
  CONSTRAINT `Transactions_ibfk_2` FOREIGN KEY (`recipient_wallet_id`) REFERENCES `Wallet` (`wallet_id`) ON DELETE SET NULL
)

CREATE TABLE `Customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `customer_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`)
) 