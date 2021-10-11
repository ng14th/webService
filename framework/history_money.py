from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history

def historymoney(input):
    error = xd.xacdinh(input)
    ans=[] #ketqua
    if error==[]:
        request_from_ws = request.get_json() #input request follow input  on RestClient or HTML
        usernames = request_from_ws['username'] #get value of username in input
        if usernames =="":
            ans.append("Please Input Username") 
        for user in session.query(User6).filter(User6.username==usernames):  #see testSQLA.py
            ans.append('Username: {} , moneyadd: {} , time: {}'.format(user.username,user.money,user.date_time))
        if ans !=[]:
            return jsonify(ans)
        else :
            return "No found user"
    else:
        return str(error) 