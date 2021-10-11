from sqlalchemy import create_engine, engine,or_
from sqlalchemy.orm import query, relationship, sessionmaker
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import select,delete, table
from sqlalchemy.sql.functions import char_length, user
from sqlalchemy.sql.schema import CheckConstraint, Column,ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint,Table
from sqlalchemy.sql.sqltypes import BIGINT, BigInteger, CHAR, INT, SMALLINT


Base = declarative_base()

## khai bao bang trong dtb
class User(Base):
    __tablename__ = "infor"
    id = Column('id',BIGINT,primary_key=True)
    username = Column('username',CHAR,unique=True)
    password = Column('password',CHAR,unique=True)
    email = Column ('email',CHAR,unique=True)
    ip = Column('ip',CHAR, unique=True)

class User2(Base):
    __tablename__ = "onfor"
    ip = Column('ip',CHAR, primary_key=True)
    realname = Column('realname',CHAR,unique=True)
    phone = Column('phone',CHAR,unique=True)
    id = Column('id', INT,ForeignKey("infor.id"))

class User3(Base):
    __tablename__ = "salary"
    rank = Column('rank',CHAR, primary_key=True)
    salary = Column('salary',CHAR,unique=True)
    timework = Column('timework',CHAR,unique=True)
    ids = Column('ids',INT,ForeignKey("infor.id"))
   

class User4(Base):
    __tablename__ = "fruit"
    idf = Column('idf',INT, primary_key=True)
    fruit = Column('fruit',CHAR,unique=True)
    price = Column('price',INT,unique=True)

class User6(Base):
    __tablename__ = "historymoney"
    nno = Column('nno',INT,primary_key=True)
    username = Column('username',CHAR,unique=False)
    money = Column('money_add',CHAR)
    date_time = Column('date_time',CHAR)


    
## ket noi server sql
conn = create_engine('postgresql://postgres:postgres#@localhost/server')
Session = sessionmaker(bind=conn)
Base.metadata.create_all(bind=conn)
session = Session() 
server = session.query(User).all()
server2 = session.query(User2).all()
server3 = session.query(User3).all()
server4 = session.query(User4).all()
server6 = session.query(User6).all()
# them data
addtest = User6(username='saler61',money=1000,date_time='00:00:00 30-08-2021')
session.add(addtest) #cu phap add datad

# them nhieu data
# session.add_all([
#     User3(rank='manager1' ,salary='5000',timework="7"),
# # #     User3(ids=7,rank='product_mmger' ,salary='4000',timework="6"),
# # #     User3(ids=9,rank='saler' ,salary='1000',timework="4"),
# # #     User3(ids=10,rank='saler1' ,salary='1000',timework="4"),
# #     # User4(idf=1,fruit="cam",price=10),
# #     # User4(idf=2,fruit="xoai",price=15),
# #     # User4(idf=3,fruit="tao",price=5),
# #     # User4(idf=4,fruit="vai",price=20)
#     User(username=usernames,password=passwords,ip=ips),
   

# ])

# cap nhat data
# user9= session.execute(select(User6).filter_by(nno=1)).scalar_one() 
# user9.date_time = "16:41:29 29-08-2021"

# xoa data

# session.execute(delete(User).where(User.username=="user37"))
# session.execute(delete(User).where(User.username=="user38"))

# session.execute(delete(User3).where(User3.rank=="manager4"))
# session.execute(delete(User).where(User.username=="user5"))

# session.execute(delete(User).where(User.email=="user4@gmail.com"))
# de = session.query(User).filter_by(id=5).first()
# session.delete(de)

#truy xuat hang loat
# for a in range (7,19,1):
# for i in session.query(User6).filter_by(id =7):
#     print(i.id, i.username, i.password, i.email, i.ip)

# for i in session.query(User3).where(User3.salary < 1000):
#         print(i.id, i.username, i.password, i.email, i.ip)

# user12 =session.execute(select(User).fil=ter(User.ip =="1.1.12.3").where(User.username=="use10"))
# print(user12.ip)

#truy xuat nhieu dieu kien  
# for user in session.query(User).filter(User.id=='10').filter(User.username=='use10'):
#     print(user.id,user.username)

# for user in session.query(User).filter_by(username = 'use10', id = 10):
#     print(user.id,user.username)
session.commit()
list1=[]
for user in server6:
    list1.append(user.nno)
if len(list1)>15:
    a=len(list1)-15
    for j in range(a):
        b = list1[j]
        session.execute(delete(User6).where(User6.nno==b))
session.commit()
# # #in bang
# print("///////////////database////////////////")
# for user in server:
#     print(user.id, user.username, user.password, user.email, user.ip)
# print("///////////////database////////////////")
# for user2 in server2:
#     print(user2.ip, user2.realname, user2.phone, user2.id)
