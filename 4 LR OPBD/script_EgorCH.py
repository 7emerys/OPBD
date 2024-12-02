from graphviz import Digraph

# Создаем новый граф
dot = Digraph(comment='Logical Model of Real Estate Rental Database')

# Таблица "Owner"
dot.node('Owner', '''Owner
PK  id
    last_name
    first_name
    patronymic
    passport_number
    ownership_document_number
    address
    phone''')

# Таблица "Property"
dot.node('Property', '''Property
PK  id
    type
    address
    phone
    total_area
    living_area
    rental_price
FK  owner_id''')

# Таблица "Client"
dot.node('Client', '''Client
PK  id
    client_type
    last_name
    first_name
    patronymic
    passport_number
    workplace
    position
    phone
    organization_name
    organization_address
    bank_details
    contact_last_name
    contact_first_name
    contact_patronymic''')

# Таблица "Rental Agreement"
dot.node('RentalAgreement', '''RentalAgreement
PK  id
    date_created
    start_date
    end_date
FK  property_id
FK  client_id''')

# Определяем связи между таблицами
dot.edge('Owner', 'Property', 'owns')
dot.edge('Property', 'RentalAgreement', 'rented in')
dot.edge('Client', 'RentalAgreement', 'enters into')

# Сохраняем граф в файл формата PNG
dot.render('real_estate_rental_db', format='png', cleanup=True)

# Выводим граф в формате текста
print(dot.source)
