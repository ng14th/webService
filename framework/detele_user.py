from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history,salary_table

# def deleteuser(todo_schema1):
#     error = xd.xacdinh(todo_schema1)
#     ans=[] #ketqua
#     if error==[]:
#         request_from_ws = request.get_json()
#         usernames = request_from_ws['username']
#         list_user=[]
#         for user in salary_table:
#             list_user.append(user.rank)
#         if usernames in list_user:
#             session.execute(delete(User3).where(User3.rank==usernames))
#             session.commit()
#             ans.append("successfully deleted {}".format(usernames))
#             return jsonify(ans)
#         else :
#             return jsonify("No found user")
#     else:
#         return jsonify(error) 

def deleteuser(input):
    error = xd.xacdinh(input) #read file func.py
    ans=[] #ketqua
    if error==[]:
        request_from_ws = request.get_json()  #input request follow input  on RestClient or HTML
        usernames = request_from_ws['username'] #get value of username in input
        list_user=[]
        for user in session.query(User3).filter_by(rank=usernames): #see file testSQLA.py// query all data in column rank if == usernames
            list_user.append(user.rank)
        if list_user != [] :
            session.execute(delete(User3).where(User3.rank==usernames))  #see file testSQLA.py/
            session.commit()
            ans.append("successfully deleted {}".format(usernames))
            return jsonify(ans)
        else :
            return "Not found user"
    else:
        return str(error) 