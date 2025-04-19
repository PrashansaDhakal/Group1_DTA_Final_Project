# Data Classification

## E-Commerce Dataset

| **Column Name**   | **Dataset**   | **Classification**     | **Note**                                              |
|-------------------|---------------|------------------------|------------------------------------------------------|
| `InvoiceNo`       | E-Commerce    | Public                 | No protection needed, but may be used for tracking transactions |
| `StockCode`       | E-Commerce    | Public                 | Public, but could be confidential if the code is associated with proprietary products |
| `Description`     | E-Commerce    | Public                 | No protection needed, typically used for identifying products |
| `Quantity`        | E-Commerce    | Public                 | No protection needed, related to sales data          |
| `InvoiceDate`     | E-Commerce    | Public                 | No protection needed, typically used for transaction tracking |
| `UnitPrice`       | E-Commerce    | Public                 | No protection needed, related to sales data          |
| `CustomerID`      | E-Commerce    | Confidential (PII)     | Should be encrypted in storage, personal identifier for the customer |
| `Country`         | E-Commerce    | Public                 | No protection needed, although some countries might have specific data protection laws |

## Yelp Academic Dataset

| **Column Name**    | **Dataset**       | **Classification**     | **Note**                                              |
|--------------------|-------------------|------------------------|------------------------------------------------------|
| `Store Name`       | Business Data     | Public                 | Public, identifies the store name, no protection needed |
| `Address`          | Business Data     | Confidential (PII)     | Could be used to identify an individual or a business location; should be protected |
| `City`             | Business Data     | Public                 | Public, location information, but not sensitive |
| `Postal Code`      | Business Data     | Confidential (PII)     | Could be used to identify locations or specific areas within cities; sensitive in some contexts |
| `Latitude`         | Business Data     | Public                 | Geolocation data, public unless tied to a specific individual or PII |
| `Longitude`        | Business Data     | Public                 | Geolocation data, public unless tied to a specific individual or PII |
| `Price`            | Business Data     | Public                 | Public, relates to the business operations (pricing) |
| `Category`         | Business Data     | Public                 | Public, defines the category or type of business/product |

# Data Retention & Archival Policy

## E-Commerce Dataset

- **How long will you keep raw, processed, or sensitive data?**
  - Raw data: 30 days
  - Processed data: 1 year
  - Sensitive data (e.g., `CustomerID`): Archived after 1 year for 5 years

- **When and how will you archive or delete old data?**
  - Archive after 1 year, stored in encrypted external storage or cloud services
  - Delete using secure data destruction methods

- **Where will archived data be stored?**
  - Archived data will be stored in secure, encrypted cloud storage (e.g., AWS S3) or encrypted external hard drives

## Yelp Academic Dataset

- **How long will you keep raw, processed, or sensitive data?**
  - Raw data: 30 days
  - Processed data: 1 year
  - Sensitive data (e.g., `Address`, `Postal Code`): Archived after 1 year for 5 years

- **When and how will you archive or delete old data?**
  - Archive after 1 year, stored in encrypted external storage or cloud services
  - Delete using secure data destruction methods

- **Where will archived data be stored?**
  - Archived data will be stored in secure, encrypted cloud storage services like AWS S3 or on encrypted external hard drives

# Audit & Monitoring Strategy

## E-Commerce Dataset

- **Data Access:**
  - Access to sensitive data like `CustomerID` will be monitored through access logs and Airflow.
  - Only authorized personnel will have access to sensitive columns.

- **Changes Made to Data or Pipeline Configurations:**
  - Changes will be tracked via version control (e.g., Git) and logged using tools like Airflow.
  - Logs will be reviewed periodically for compliance.

## Yelp Academic Dataset

- **Data Access:**
  - Access to sensitive columns like `Address` and `Postal Code` will be monitored using audit logs.
  - Access control lists will ensure that only authorized personnel can view or modify these fields.

- **Changes Made to Data or Pipeline Configurations:**
  - All changes to data or pipeline configurations will be tracked using version control (e.g., Git).
  - Airflow logs will capture all changes, and logs will be reviewed periodically.
