from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history
from flask import json,Response

def addmoney(input):  # with input from schema (schema : add_money)
    if request.method == "POST":    
        error = xd.xacdinh_m(input)  #validator schema input with list of schema [{}:{}]
        salary_in_table = get_salary() #get salary from salary table in database
        total = []
        load_ans=[]
        now = datetime.datetime.now()
        times = now.strftime("%H:%M:%S %d-%m-%Y")   
        if error==[]:
            request_from_ws = request.get_json()  #input request follow input  on RestClient or HTML
            for get_value in request_from_ws:
                usernames = get_value['username']  #get value ( of key'username' of input )
                moneys = get_value['money']  #get value ( of key'username' of input )
                for user in session.query(User6).filter(User6.username==usernames): #get user in salary table
                    if times[9:] in user.date_time: 
                        total.append(int(user.money))
                user_in_tablesalary=[*salary_in_table.keys()] # get user
                if int(moneys)+sum(total) <= 1000:  
                    if usernames in user_in_tablesalary:
                        for key,value in salary_in_table.items():
                            if usernames == key:
                                budget = value
                                adduser=User6(username=usernames,money=moneys,date_time=times) #see file testSQLA.py
                                session.add(adduser) #see file testSQLA.py
                                update_salary = session.execute(select(User3).filter_by(rank=usernames)).scalar_one() #see file testSQLA.py update
                                update_salary.salary = moneys+budget 
                                session.flush()
                                session.commit()
                        load_ans.append("Successful recharge : {} for {}, budget : {}, at {} ".format(moneys,usernames,update_salary.salary,times))
                        list_record_notinday=[]
                        list_record_inday=[]
                        list_record_all=[]
                        for user in session.query(User6).all():
                            list_record_all.append(user.nno)
                            session.flush()
                            session.commit()
                            if user.date_time[9:] not in times[9:]:
                                list_record_notinday.append(user.nno)
                            else:
                                list_record_inday.append(user.nno)
                        if len(list_record_inday)+len(list_record_notinday) >20: # if table have 20 record , delete reocord not in  day but if dont have 20 after delete keep ones record not in day to enough 20
                            if list_record_notinday !=[]:
                                num=20-len(list_record_inday)
                                num1=len(list_record_notinday)-num
                                if num1 > len(list_record_notinday):
                                    for no in list_record_notinday:
                                        session.execute(delete(User6).where(User6.nno==no)) #see file testSQLA.py
                                else:
                                    for j in range(num1):
                                        nno =list_record_notinday[j]
                                        session.execute(delete(User6).where(User6.nno==nno)) #see file testSQLA.py
                        session.flush()
                        session.commit()
                    else:
                        load_ans.append("Not Found {}".format(usernames))
                else:
                        load_ans.append("{}'s amount has exceeded the limit for one day - limit 1000".format(usernames))            
            return jsonify(load_ans)
        else:
            return error
    