import sqlite3, os.path, subprocess


connection = sqlite3.connect('store.db')
cursor = connection.cursor()

def create_db():
    cursor.execute('''
    CREATE TABLE Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT NOT NULL,
        Description TEXT,
        ParentCategoryID INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT NOT NULL,
        Description TEXT,
        Price REAL NOT NULL,
        CategoryID INTEGER NOT NULL,
        StockQuantity INTEGER NOT NULL
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
        SellerID INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE PurchaseItems (
        PurchaseItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        PurchaseID INTEGER NOT NULL,
        ProductID INTEGER NOT NULL,
        Quantity INTEGER NOT NULL
    )
    ''')

    connection.commit()



if not os.path.exists('EgorCH.db'):
    create_db()
subprocess.run(['C:/Users/arsen/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/Scripts/sqlacodegen', 'sqlite:///EgorCH.db', '--outfile', 'model_EgorCH.py'])

