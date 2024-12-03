from graphviz import Digraph

# Создаем объект для графа
dot = Digraph(comment='IDEF1X Model for Database Structure with Foreign Keys')

# Определяем стиль IDEF1X для сущностей
def create_entity(dot, entity_name, attributes, pk):
    with dot.subgraph(name='cluster_' + entity_name) as c:
        c.attr(style='filled', color='lightgrey')
        c.node(entity_name, shape='plaintext', label=f'<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
                                                     f'<TR><TD COLSPAN="2" BGCOLOR="black"><FONT COLOR="white">'
                                                     f'<B>{entity_name}</B></FONT></TD></TR>'
                                                     + ''.join([f'<TR><TD ALIGN="LEFT">{attr}</TD>'
                                                                f'<TD ALIGN="LEFT">{("PK" if attr == pk else "FK" if "ID" in attr else "")}</TD></TR>'
                                                                for attr in attributes])
                                                     + '</TABLE>>')

# Определяем сущности и их атрибуты
create_entity(dot, 'Categories', ['CategoryID', 'CategoryName', 'Description'], 'CategoryID')
create_entity(dot, 'Products', ['ProductID', 'ProductName', 'Description', 'Price', 'CategoryID', 'StockQuantity'], 'ProductID')
create_entity(dot, 'Sellers', ['SellerID', 'LastName', 'FirstName', 'MiddleName', 'Position', 'HomeAddress', 'Phone'], 'SellerID')
create_entity(dot, 'Customers', ['CustomerID', 'LastName', 'FirstName', 'MiddleName', 'PassportData', 'HomeAddress', 'Phone'], 'CustomerID')
create_entity(dot, 'Purchases', ['PurchaseID', 'PurchaseDate', 'CustomerID', 'SellerID'], 'PurchaseID')
create_entity(dot, 'PurchaseItems', ['PurchaseItemID', 'PurchaseID', 'ProductID', 'Quantity'], 'PurchaseItemID')

# Определяем связи между сущностями
dot.edge('Categories', 'Products', label='1:M')
dot.edge('Customers', 'Purchases', label='1:M')
dot.edge('Sellers', 'Purchases', label='1:M')
dot.edge('Purchases', 'PurchaseItems', label='1:M')
dot.edge('Products', 'PurchaseItems', label='1:M')



# Сохраняем и отображаем граф
dot.render('db_structure', format='png', cleanup=True)
dot.view()
