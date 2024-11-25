from graphviz import Digraph

# Создаем объект для графа
dot = Digraph(comment='IDEF1X Model for Pet Visit Database')

# Определяем стиль IDEF1X для сущностей
def create_entity(dot, entity_name, attributes, pk):
    with dot.subgraph(name='cluster_' + entity_name) as c:
        c.attr(style='filled', color='lightgrey')
        c.node(entity_name, shape='plaintext', label=f'<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
                                                     f'<TR><TD COLSPAN="2" BGCOLOR="black"><FONT COLOR="white">'
                                                     f'<B>{entity_name}</B></FONT></TD></TR>'
                                                     + ''.join([f'<TR><TD ALIGN="LEFT">{attr}</TD>'
                                                                f'<TD ALIGN="LEFT">{("PK" if attr == pk else "")}</TD></TR>'
                                                                for attr in attributes])
                                                     + '</TABLE>>')

# Определяем сущности и их атрибуты
create_entity(dot, 'Routes', ['Code and route name ', 'Duration', 'Type of transport'], 'Routes')
create_entity(dot, 'Cost', ['Route code', 'Cost', 'Availability of seats'], 'Cost')

# Определяем связи между сущностями
dot.edge('Routes', 'Cost', label='1:M')

# Сохраняем и отображаем граф
dot.render('Model.png')

