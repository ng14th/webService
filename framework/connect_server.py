from dict import dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import  Column
from sqlalchemy.sql.sqltypes import BIGINT, CHAR, INT, Integer
from configparser import ConfigParser
config = ConfigParser()
config.read("store.ini")
link_server = config['link_server']['link']  #You can edit you url of server Postgres SQL in store.ini

# connet to server
Base = declarative_base()
conn = create_engine(link_server)
Session = sessionmaker(bind=conn)
Base.metadata.create_all(bind=conn)
session = Session()

# list TABLE in server
class User3(Base):
    __tablename__ = "salary"
    rank = Column('rank',CHAR, primary_key=True)
    salary = Column('salary',CHAR,unique=True)
    timework = Column('timework',CHAR,unique=True)
    ids = Column('ids',INT,unique=True)
class User4(Base):
    __tablename__ = "fruit"
    idf = Column('idf',INT, primary_key=True)
    fruit = Column('fruit',CHAR,unique=True)
    price = Column('price',INT,unique=True)
class User5(Base):
    __tablename__ = "history"
    nno = Column('nno',Integer,primary_key=True)
    username = Column('username',CHAR,unique=False)
    purchase = Column('purchase',CHAR)
    change = Column('change',CHAR)
    date_time = Column('date_time',CHAR)
class User6(Base):
    __tablename__ = "historymoney"
    nno = Column('nno',Integer,primary_key=True)
    username = Column('username',CHAR,unique=False)
    money = Column('money_add',CHAR)
    date_time = Column('date_time',CHAR)

#call all data in table to query with example ("salary_table.rank" => query all data in rank column , or for user in money_history)
salary_table = session.query(User3).all() 
frui_table = session.query(User4).all()
buy_history = session.query(User5).all()
money_history = session.query(User6).all() 

# get price of fruit
def get_price():
    list_fruit=[]
    list_price=[]
    for i in session.query(User4):
            list_fruit.append(i.fruit)
            list_price.append(i.price)
            session.commit()
            conct=zip(list_fruit,list_price)
            dict_fruit_price=dict(conct)
    return dict_fruit_price


# get salary from table salary
def get_salary():
    list_ranks = []
    list_salary = []
    for i in session.query(User3):
        list_ranks.append(i.rank)
        list_salary.append(i.salary)
        session.commit()
        conct=zip(list_ranks,list_salary)
        dict_ranks_salary=dict(conct)
    return dict_ranks_salary

