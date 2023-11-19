from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy import create_engine, inspect

engine = create_engine('sqlite:///database.db')

meta = MetaData()
conn = engine.connect()

stations = Table(
    'stations', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)
meta.create_all(engine)

stat = stations.insert().values(
    station='USC00519397',
    latitude=21.2716,
    longitude=-157.8168,
    elevation=3,
    name='WAIKIKI 717.2',
    country='US',
    state='HI'
)
conn.execute(stat)

stat = stations.insert().values(
    station='USC00513117',
    latitude=21.4234,
    longitude=-157.8015,
    elevation=14.6,
    name='KANEOHE 838.1',
    country='US',
    state='HI'
)
conn.execute(stat)

result = conn.execute(stations.select().limit(5))
for res in result:
    print(res)

conn.close()