-- Online Retail Table
CREATE TABLE IF NOT EXISTS online_retail (
    InvoiceNo TEXT,
    StockCode TEXT,
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate TEXT,
    UnitPrice FLOAT,
    CustomerID TEXT,
    Country TEXT
);

-- Annual Reports Table
CREATE TABLE IF NOT EXISTS annual_reports (
    id SERIAL PRIMARY KEY,
    report_text TEXT
);

-- Yelp Business Table (placeholder, confirm after JSON upload)
CREATE TABLE IF NOT EXISTS yelp_business (
    business_id TEXT PRIMARY KEY,
    name TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    latitude FLOAT,
    longitude FLOAT,
    stars FLOAT,
    review_count INT,
    is_open INT,
    categories TEXT
);
