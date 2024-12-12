from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_EgorCH import Base
from graphviz import Digraph

# Создаем соединение с базой данных
engine = create_engine('sqlite:///EgorCH.db')
Base.metadata.create_all(engine)

# Функция для создания графа
def create_graph(metadata):
    g = Digraph('G')

    # Добавляем узлы для каждой таблицы
    for table in metadata.tables.values():
        g.node(table.name)

    # Добавляем связи между таблицами
    for table in metadata.tables.values():
        for fk in table.foreign_keys:
            g.edge(fk.column.table.name, table.name, label=fk.parent.name)

    return g

# Создаем граф
g = create_graph(Base.metadata)

# Сохраняем граф в файл
g.render('model_diagram_EgorCH', format='png', cleanup=True)
