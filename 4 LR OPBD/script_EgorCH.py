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

create_entity(dot, 'Owners', ['OwnerID', 'FirstName', 'LastName', 'Patronymic', 'PassportData', 'OwnershipDocumentNumber', 'Address', 'Phone'], 'OwnerID')
create_entity(dot, 'Properties', ['PropertyID', 'PropertyType', 'Address', 'Phone', 'TotalArea', 'LivingArea', 'RentalPrice', 'OwnerID'], 'PropertyID')
create_entity(dot, 'IndividualTenants', ['TenantID', 'FirstName', 'LastName', 'Patronymic', 'PassportData', 'Workplace', 'Position', 'Phone'], 'TenantID')
create_entity(dot, 'LegalEntityTenants', ['TenantID', 'OrganizationName', 'Address', 'BankDetails', 'Phone', 'ContactFirstName', 'ContactLastName', 'ContactPatronymic'], 'TenantID')
create_entity(dot, 'Leases', ['LeaseID', 'PropertyID', 'TenantID', 'LeaseDate', 'StartDate', 'EndDate'], 'LeaseID')

# Определяем связи между сущностями
dot.edge('Owners', 'Properties', label='1:M')
dot.edge('Properties', 'Leases', label='1:1')
dot.edge('IndividualTenants', 'Leases', label='1:M')
dot.edge('LegalEntityTenants', 'Leases', label='1:M')




# Сохраняем и отображаем граф
dot.render('db_structure_Egor_CH', format='png', cleanup=True)
dot.view()
