-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.

BEGIN;
CREATE TABLE IF NOT EXISTS public.Artist (
    Artist_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    Name CHAR(25) NOT NULL,
    Nationality VARCHAR(30) NOT NULL,
    Birth_date NUMERIC(4, 0) NOT NULL,
    Deceased_date NUMERIC(4, 0) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.Customer (
    Customer_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    Name CHAR(25) NOT NULL,
    Street CHAR(30) NOT NULL,
    City CHAR(35) NOT NULL,
    State CHAR(2) NOT NULL,
    Zip_postal_code CHAR(5) NOT NULL,
    Country VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS public.Transaction (
    Transaction_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    Date_acquired DATE NOT NULL,
    Acquisition_price NUMERIC(8, 2) NOT NULL,
    Purchase_date DATE NOT NULL,
    Sales_price NUMERIC(8, 2) NOT NULL,
    Asking_price NUMERIC(8, 2) NOT NULL,
    Customer_id INTEGER REFERENCES Customer(Customer_id),
    Work_id INTEGER REFERENCES Work(Work_id),
    Artist_id INTEGER REFERENCES Artist(Artist_id)
);

CREATE TABLE IF NOT EXISTS public.Work (
    Work_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    Title VARCHAR(25) NOT NULL,
    Description VARCHAR(1000) NOT NULL,
    Copy VARCHAR(8) NOT NULL,
    Artist_id INTEGER REFERENCES Artist(Artist_id)
);

CREATE TABLE IF NOT EXISTS public.Customer_Artist_INT (
    Artist_id INTEGER REFERENCES Artist(Artist_id),
    Customer_id INTEGER REFERENCES Customer(Customer_id)
);

END;