import sqlite3 as sq

connect = sq.connect('gas_station.db')
cur = connect.cursor()

def create_db():
    cur.execute(
        '''CREATE TABLE FuelTypes (
    FuelTypeID INT PRIMARY KEY,
    FuelName VARCHAR(50) NOT NULL,
    PricePerLiter DECIMAL(10, 2) NOT NULL,
    Stock INT NOT NULL
        );'''
    )

    cur.execute(
        '''CREATE TABLE Pumps (
    PumpID INT PRIMARY KEY,
    FuelTypeID INT,
    Location VARCHAR(50) NOT NULL,
    FOREIGN KEY (FuelTypeID) REFERENCES FuelTypes(FuelTypeID)
        );'''
    )

    cur.execute(
        '''CREATE TABLE Receipts (
    ReceiptID INT PRIMARY KEY,
    PumpID INT,
    Amount DECIMAL(10, 2) NOT NULL,
    PricePerLiter DECIMAL(10, 2) NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (PumpID) REFERENCES Pumps(PumpID)
        );'''
    )

    cur.execute(
        '''CREATE TABLE DiscountCards (
    CardID INT PRIMARY KEY,
    TotalFuelDispensed DECIMAL(10, 2) NOT NULL,
    DiscountPercentage DECIMAL(5, 2) NOT NULL
        );'''
    )

    cur.execute(
        '''CREATE TABLE FuelDispensed (
    DispensedID INT PRIMARY KEY,
    ReceiptID INT,
    CardID INT,
    Amount DECIMAL(10, 2) NOT NULL,
    DiscountApplied DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (ReceiptID) REFERENCES Receipts(ReceiptID),
    FOREIGN KEY (CardID) REFERENCES DiscountCards(CardID)
        );'''
    )

    connect.commit()
