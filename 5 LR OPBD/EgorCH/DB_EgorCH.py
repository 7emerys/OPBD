import sqlite3, os.path, subprocess


connection = sqlite3.connect('store.db')
cursor = connection.cursor()

def create_db():
    cursor.execute('''
    CREATE TABLE Owners (
    owner_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    patronymic VARCHAR(50),
    passport_data VARCHAR(100) NOT NULL,
    ownership_document_number VARCHAR(50) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20)
);    ''')

    cursor.execute('''
CREATE TABLE Properties (
    property_id INT PRIMARY KEY AUTO_INCREMENT,
    property_type ENUM('квартира', 'дом') NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    total_area DECIMAL(10, 2) NOT NULL,
    living_area DECIMAL(10, 2) NOT NULL,
    rental_price DECIMAL(10, 2) NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id)
);    ''')

    cursor.execute('''
CREATE TABLE IndividualTenants (
    tenant_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    patronymic VARCHAR(50),
    passport_data VARCHAR(100) NOT NULL,
    workplace VARCHAR(100),
    position VARCHAR(50),
    phone VARCHAR(20)
);    ''')

    cursor.execute('''
CREATE TABLE LegalEntityTenants (
    tenant_id INT PRIMARY KEY AUTO_INCREMENT,
    organization_name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    bank_details VARCHAR(100),
    phone VARCHAR(20),
    contact_first_name VARCHAR(50) NOT NULL,
    contact_last_name VARCHAR(50) NOT NULL,
    contact_patronymic VARCHAR(50)
);''')

    cursor.execute('''
CREATE TABLE Leases (
    lease_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT,
    tenant_id INT,
    lease_date DATE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id),
    CONSTRAINT unique_current_lease UNIQUE (property_id) -- Объект может быть сдан в аренду только одному арендатору
);''')

