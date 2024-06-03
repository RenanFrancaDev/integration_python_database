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


    account = relationship("Account", back_populates='account')

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))


    account = relationship("User", back_populates='user')

    def __repr__(self):
        return f"Account(id={self.id}, number={self.number}, type={self.type})"
    
print(User.__tablename__)
print(User.__repr__)
print(Account.__tablename__)
