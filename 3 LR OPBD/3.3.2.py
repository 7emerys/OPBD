from graphviz import Digraph

# Создаем объект для графа
dot = Digraph(comment='IDEF1X Model for Medical Database')

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
create_entity(dot, 'Doctors', ['doctor_id', 'full_name', 'address', 'date_of_birth', 'passport_data', 'specialty', 'category', 'experience'], 'doctor_id')
create_entity(dot, 'Patients', ['patient_id', 'full_name', 'date_of_birth', 'policy_number'], 'patient_id')
create_entity(dot, 'Clinics', ['clinic_id', 'clinic_name', 'address'], 'clinic_id')
create_entity(dot, 'Schedule', ['schedule_id', 'doctor_id (FK)', 'clinic_id (FK)', 'day_of_week', 'start_time', 'end_time'], 'schedule_id')
create_entity(dot, 'Visits', ['visit_id', 'visit_date', 'doctor_id (FK)', 'patient_id (FK)', 'diagnosis'], 'visit_id')
create_entity(dot, 'Rooms', ['room_id', 'clinic_id (FK)', 'doctor_id (FK)', 'room_number'], 'room_id')
create_entity(dot, 'MedicalCard', ['medical_card_id', 'patient_id (FK)', 'visit_date', 'doctor_full_name', 'treatment', 'diagnosis'], 'medical_card_id')

# Определяем связи между сущностями
dot.edge('Doctors', 'Schedule', label='1:M')
dot.edge('Doctors', 'Visits', label='1:M')
dot.edge('Doctors', 'Rooms', label='1:M')
dot.edge('Patients', 'Visits', label='1:M')
dot.edge('Patients', 'MedicalCard', label='1:M')
dot.edge('Clinics', 'Schedule', label='1:M')
dot.edge('Clinics', 'Rooms', label='1:M')

# Сохраняем и отображаем граф
dot.format = 'png'
dot.render('IDEF1 3.3.2')

print("Model saved as 'IDEF1X_Model.png'")
