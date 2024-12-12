from sqlalchemy import Column, DateTime, Float, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Categories'

    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(Text, nullable=False)
    Description = Column(Text)

    # Связи
    parent_category = relationship("Category", remote_side=[CategoryID], backref="subcategories")

class Customer(Base):
    __tablename__ = 'Customers'

    CustomerID = Column(Integer, primary_key=True)
    LastName = Column(Text, nullable=False)
    FirstName = Column(Text, nullable=False)
    MiddleName = Column(Text)
    PassportData = Column(Text, nullable=False)
    HomeAddress = Column(Text)
    Phone = Column(Text)

class Product(Base):
    __tablename__ = 'Products'

    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(Text, nullable=False)
    Description = Column(Text)
    Price = Column(Float, nullable=False)
    CategoryID = Column(Integer, ForeignKey('Categories.CategoryID'), nullable=False)  # Внешний ключ на Categories
    StockQuantity = Column(Integer, nullable=False)

    # Связи
    category = relationship("Category")

class PurchaseItem(Base):
    __tablename__ = 'PurchaseItems'

    PurchaseItemID = Column(Integer, primary_key=True)
    PurchaseID = Column(Integer, ForeignKey('Purchases.PurchaseID'), nullable=False)  # Внешний ключ на Purchases
    ProductID = Column(Integer, ForeignKey('Products.ProductID'), nullable=False)  # Внешний ключ на Products
    Quantity = Column(Integer, nullable=False)

    # Связи
    purchase = relationship("Purchase", backref="items")
    product = relationship("Product")

class Purchase(Base):
    __tablename__ = 'Purchases'

    PurchaseID = Column(Integer, primary_key=True)
    PurchaseDate = Column(DateTime, nullable=False)
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'), nullable=False)  # Внешний ключ на Customers
    SellerID = Column(Integer, ForeignKey('Sellers.SellerID'), nullable=False)  # Внешний ключ на Sellers

    # Связи
    customer = relationship("Customer")
    seller = relationship("Seller")

class Seller(Base):
    __tablename__ = 'Sellers'

    SellerID = Column(Integer, primary_key=True)
    LastName = Column(Text, nullable=False)
    FirstName = Column(Text, nullable=False)
    MiddleName = Column(Text)
    Position = Column(Text, nullable=False)
    HomeAddress = Column(Text)
    Phone = Column(Text)

# Объявление дополнительной таблицы для SQLite
sqlite_sequence = Table(
    'sqlite_sequence', Base.metadata,
    Column('name', Text),  # Используем Text для имени таблицы
    Column('seq', Integer)  # Используем Integer для последовательности
)
