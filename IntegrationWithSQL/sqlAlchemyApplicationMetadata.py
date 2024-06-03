from sqlalchemy import Column, MetaData, Table, Integer, String, ForeignKey, create_engine, inspect, select, func, text

engine = create_engine('sqlite:///:memory:')

metadata_obj = MetaData()


user = Table(
    'user',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(60), nullable=False),
    Column('email', String(60), unique=True, nullable=False),
    Column('cpf', String(11), unique=True, nullable=False)
)


user = Table(
    'account',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('type', String(60), nullable=False),
    Column('number', String(60)),
    Column('user_id', String(11), ForeignKey('user.id'))
)

for table in metadata_obj.sorted_tables:
    print(table)


metadata_obj.create_all(engine)

sql_insert_user = text("insert into user values(2,'maria', 'maria@email.com.br', '12345678901')")
engine.connect().execute(sql_insert_user)

sql_insert_account = text("insert into account values(2,'corrente', 002, 2)")  
engine.connect().execute(sql_insert_account)

sql_consult = text('select * from user')
result = engine.connect().execute(sql_consult)
for row in result:
    print (row)