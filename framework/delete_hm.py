from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import time
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history,salary_table


def detelehistory(input):
    error = xd.xacdinh(input) #read file func.py
    ans=[] #ketqua
    list_date=[]
    if error==[]:   
        request_from_ws = request.get_json()  #input request follow input  on RestClient or HTML
        date1=request_from_ws['date_start']
        date2=request_from_ws['date_end']
        date_strat = time.strptime(date1, '%Y-%m-%d')
        date_end = time.strptime(date2, '%Y-%m-%d')
        for data in money_history:
            get_date_table=data.date_time[9:] #get data in colmun data_time
            cv_day = time.strptime(get_date_table,"%d-%m-%Y")
            if cv_day >= date_strat:
                if cv_day <= date_end:
                    get_date = data.date_time    
                    if get_date not in list_date:  
                        list_date.append(get_date)
        if list_date !=[]:
            for data in list_date:
                session.execute(delete(User6).where(User6.date_time==data))
                session.commit()
            ans.append("Delete Compeled") 
        elif list_date == []:
            ans.append("Not found data")
        return jsonify(ans)
    else:
        return str(error)
        

        

