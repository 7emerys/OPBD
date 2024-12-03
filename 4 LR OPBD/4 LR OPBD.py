import sqlite3

connection = sqlite3.connect('store.db')
cursor = connection.cursor()

def create_db():
    cursor.execute('''
    CREATE TABLE Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT NOT NULL,
        Description TEXT,
        ParentCategoryID INTEGER,
        FOREIGN KEY (ParentCategoryID) REFERENCES Categories(CategoryID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT NOT NULL,
        Description TEXT,
        Price REAL NOT NULL,
        CategoryID INTEGER NOT NULL,
        StockQuantity INTEGER NOT NULL,
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Sellers (
        SellerID INTEGER PRIMARY KEY AUTOINCREMENT,
        LastName TEXT NOT NULL,
        FirstName TEXT NOT NULL,
        MiddleName TEXT,
        Position TEXT NOT NULL,
        HomeAddress TEXT,
        Phone TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE Customers (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
        LastName TEXT NOT NULL,
        FirstName TEXT NOT NULL,
        MiddleName TEXT,
        PassportData TEXT NOT NULL,
        HomeAddress TEXT,
        Phone TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE Purchases (
        PurchaseID INTEGER PRIMARY KEY AUTOINCREMENT,
        PurchaseDate DATETIME NOT NULL,
        CustomerID INTEGER NOT NULL,
        SellerID INTEGER NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (SellerID) REFERENCES Sellers(SellerID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE PurchaseItems (
        PurchaseItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        PurchaseID INTEGER NOT NULL,
        ProductID INTEGER NOT NULL,
        Quantity INTEGER NOT NULL,
        FOREIGN KEY (PurchaseID) REFERENCES Purchases(PurchaseID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
    ''')

    connection.commit()