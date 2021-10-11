import re
from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request,render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history

get = get_price()     # get value of fruit in fruit table
for key,value in get.items():
    if 'cam' in key:
            p_cam = value
    if 'xoai' in key:
            p_xoai = value
    if 'tao' in key:
            p_tao = value
    if 'vai' in key:
            p_vai = value

def buyfruit(input):
    if request.method== 'POST':
        error = xd.xacdinh_m(input) #read file func.py
        salary_in_table = get_salary()
        pri=[]
        purchases=[]
        ans=[]
        if error == []:
            request_from_ws = request.get_json()  #input request follow input  on RestClient or HTML
            for item in request_from_ws:
                for key,value in item.items():
                    if 'cam' in key:
                        a_cam=int(value)*p_cam
                        if a_cam !=0:
                            purchase2=item['cam']
                            purchases.append('cam:{}'.format(purchase2))
                            pri.append(a_cam)
                    if 'xoai' in key:
                        a_xoai=int(value)*p_xoai
                        if a_xoai !=0:
                            purchase4=item['xoai']
                            purchases.append('xoai:{}'.format(purchase4))
                            pri.append(a_xoai)
                    if 'tao' in key:
                        a_tao=int(value)*p_tao
                        if a_tao !=0:
                            purchase1=item['tao']
                            purchases.append('tao:{}'.format(purchase1))
                            pri.append(a_tao)
                    if 'vai' in key:
                        a_vai=int(value)*p_vai
                        if a_vai !=0:
                            purchase3=item['vai']
                            purchases.append('vai:{}'.format(purchase3))
                            pri.append(a_vai)
                sum_of_purchase =sum(pri)
                usernames=item['username']
                for key,value in salary_in_table.items():
                    if usernames == key:
                        budget = value
                        m_change = budget - sum_of_purchase
                        if sum_of_purchase !=0:
                            if sum_of_purchase<=budget: #if they enough money to buy
                                now = datetime.datetime.now()
                                times = now.strftime("%H:%M:%S %d-%m-%Y")
                                purchases_final=str(purchases).replace("[","").replace("]","")
                                adduser=User5(username=usernames,purchase=purchases_final,change=m_change,date_time=times) #see file testSQLA.py
                                session.add(adduser) #see file testSQLA.py
                                update_salary = session.execute(select(User3).filter_by(rank=usernames)).scalar_one() #see file testSQLA.py
                                update_salary.salary = m_change #see file testSQLA.py
                                session.commit()
                                ans.append("{} buy compelete {}, total : {}, budget : {}, change : {}, time : {} ".format(usernames,purchases_final,sum_of_purchase,budget,m_change,times))
                            if sum_of_purchase>budget:
                                ans.append ("{} not enough money, missing {}".format(usernames,-m_change))
                        else:
                            ans.append("{} not buy anything".format(usernames))
                        return jsonify(ans)
                return "Not found user"
                
        else : 
            return error
 