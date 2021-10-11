from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import time
from func import xd
from connect_server import User5,User6,session,money_history,buy_history

def clean(input):
    error = xd.xacdinh(input) #read file func.py
    ans=[] #ketqua 
    list_record=[]
    if error==[]:  
        request_from_ws = request.get_json()  #input request follow input  on RestClient or HTML
        choose_table = request_from_ws['table'] #get value in key table
        keep_record = request_from_ws['keep']  #get value in key keep
        if choose_table == 'historybuy':
            for user in buy_history:
                list_record.append(user.nno)
            if len(list_record)>keep_record:
                num=len(list_record)-keep_record
                for j in range(num):
                    record=list_record[j]
                    session.execute(delete(User5).where(User5.nno==record)) #see file testSQLA.py
                session.commit()
                ans.append("Completed clean up table history_buy")
            if len(list_record)==keep_record:
                ans.append("Table history_buy only has {} records, cant clean up".format(keep_record))
            elif len(list_record)<keep_record:
                ans.append("Cant clean up table history_buy - dont enough data")
        elif choose_table == 'historymoney':
            for user in money_history:
                list_record.append(user.nno)
            if len(list_record)>keep_record:
                num=len(list_record)-keep_record
                for j in range(num):
                    record=list_record[j]
                    session.execute(delete(User6).where(User6.nno==record))
                session.commit()
                ans.append("Completed clean up table history_money")
            elif len(list_record)==keep_record:
                ans.append("Table history_money only has {} records, cant clean up".format(keep_record))
            elif len(list_record)<keep_record: 
                ans.append("Cant clean up table history_money - Dont enough data")
        return jsonify(ans)
    else:
        return str(error)
