import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False)


    account = relationship("Account", back_populates='user')

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


    user = relationship("User", back_populates="account") 

    def __repr__(self):
        return f"Acount(id={self.id}, number={self.number}, type={self.type})"
    
# Database Connection


engine = create_engine('sqlite://')

# Creating classes as tables into database
Base.metadata.create_all(engine)

inspect_engine = inspect(engine)
# print(inspect_engine.get_table_names())

with Session(engine) as session:
    renan = User(
        name='renan',
        email='renan@email.com',
        cpf='12345678900',
        account=[Account(number='001', type='corrente')]
    )

    joao = User(
        name='joao',
        email='joao@email.com',
        cpf='12345678900',
        account=[Account(number='002', type='corrente'),
                 Account(number='003', type='corrente')]
    )

    # Send to Database

    session.add_all([renan, joao])

    session.commit()

stmt = select(User).where(User.name.in_(['renan']))
for user in session.scalars(stmt):
    print(user)

# Query by connection

connection = engine.connect()
results = connection.execute(stmt).fetchall()

for result in results:
    print(result)

