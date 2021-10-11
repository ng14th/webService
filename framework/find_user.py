from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history
from flask import json,render_template
import re
import sys
sys.setrecursionlimit(1500)

# result this file is find persons in table salary
#case1 : find by symbol in name
#case2 : find by salary in range from ... to ...
#case3 : find by 2 ways 
# result must be satisfy each case
def find(input):
    if request.method =='POST':
        ans=[]
        error = xd.xacdinh(input) #read file func.py
        string_input =""
        salary_start =""
        salary_end =""
        if error == []:
            get_request = request.get_json() #input request follow input  on RestClient or HTML
            print(get_request)
            for key,value in get_request.items():
                if 'string_input' in key:
                    string_input = get_request['string_input']
                if 'salary_start' in key:
                    salary_start = int(get_request['salary_start'])
                if 'salary_end' in key:
                    salary_end = int(get_request['salary_end'])
            for user in session.query(User3).all():  #query all data in table salary
                ranks = user.rank  # get data in column rank
                salarys = user.salary
                time_works = user.timework
                if string_input != "" and salary_start != "" and salary_end != "" :
                    if string_input in ranks:
                        if salarys >= salary_start and salarys <= salary_end :
                            result_str=('("Username": "{}", "Salary": {}, "Time_work": {})'.format(ranks,salarys,time_works).replace("(","{").replace(")","}"))
                            ans.append(json.loads(result_str))
                elif string_input != "":
                    if salary_start == "" and salary_end == "":
                        if string_input in ranks:
                            result_str=('("Username": "{}", "Salary": {}, "Time_work": {})'.format(ranks,salarys,time_works).replace("(","{").replace(")","}"))
                            ans.append(json.loads(result_str))
                elif string_input == "":
                    if salary_start != "" and salary_end !="":
                        if salarys >= salary_start and salarys <= salary_end:
                            result_str=('("Username": "{}", "Salary": {}, "Time_work": {})'.format(ranks,salarys,time_works).replace("(","{").replace(")","}"))
                            ans.append(json.loads(result_str))
            if ans ==[]: 
                return "Not found user"
            return jsonify(ans)
        else:
            return(str(error))
