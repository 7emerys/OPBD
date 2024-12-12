from eralchemy import render_er
from dbdb import create_db

#create_db()

render_er("sqlite:///gas_station.db", 'erd_Egor1.png')
