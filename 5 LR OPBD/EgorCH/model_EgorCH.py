from sqlalchemy import Column, Date, Enum, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'Owners'

    owner_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    passport_data = Column(String(100), nullable=False)
    ownership_document_number = Column(String(50), nullable=False)
    address = Column(String(255))
    phone = Column(String(20))

class Property(Base):
    __tablename__ = 'Properties'

    property_id = Column(Integer, primary_key=True)
    property_type = Column(Enum('квартира', 'дом'), nullable=False)  # ENUM поле
    address = Column(String(255), nullable=False)
    phone = Column(String(20))
    total_area = Column(Float(10, 2), nullable=False)
    living_area = Column(Float(10, 2), nullable=False)
    rental_price = Column(Float(10, 2), nullable=False)
    owner_id = Column(Integer, ForeignKey('Owners.owner_id'), nullable=True)  # Внешний ключ на Owners

    # Связи
    owner = relationship("Owner", backref="properties")

class IndividualTenant(Base):
    __tablename__ = 'IndividualTenants'

    tenant_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    passport_data = Column(String(100), nullable=False)
    workplace = Column(String(100))
    position = Column(String(50))
    phone = Column(String(20))

class LegalEntityTenant(Base):
    __tablename__ = 'LegalEntityTenants'

    tenant_id = Column(Integer, primary_key=True)
    organization_name = Column(String(100), nullable=False)
    address = Column(String(255))
    bank_details = Column(String(100))
    phone = Column(String(20))
    contact_first_name = Column(String(50), nullable=False)
    contact_last_name = Column(String(50), nullable=False)
    contact_patronymic = Column(String(50))

class Lease(Base):
    __tablename__ = 'Leases'

    lease_id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('Properties.property_id'), nullable=False)  # Внешний ключ на Properties
    tenant_id = Column(Integer, ForeignKey('IndividualTenants.tenant_id'), nullable=True)  # Внешний ключ на IndividualTenants
