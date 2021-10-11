from re import A
from flask.templating import render_template
from sqlalchemy.sql.expression import delete, select
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from func import xd
from connect_server import User3,User4,User5,User6,session,get_price,get_salary,money_history
from buy_fruit import buyfruit
from history_money import historymoney
from history_buy import historybuy
from add_money import addmoney
from detele_user import deleteuser
from delete_hm import detelehistory
from clean_up import clean
from find_user import find
from schema import *



app = Flask(__name__)



# list(distinct_combinations(e5,3))
now = datetime.datetime.now()
times = now.strftime("%H:%M:%S %d-%m-%Y")
print(times)

@app.route('/buyfruit', methods=['POST','GET'])
def buy():
    return(buyfruit(traicay))

@app.route('/historybuy', methods=['POST'])
def history_buy():
    return(historybuy(username))

@app.route('/historymoney', methods=['POST'])
def history_money():
    return(historymoney(username))

@app.route('/addmoney', methods=['POST','GET'])
def add_money():
    return(addmoney(money_add))

@app.route('/delete', methods=['POST','GET'])
def delete_user():
    return(deleteuser(username))

@app.route('/deletehistory', methods=['POST','GET'])
def delete_history():
    return(detelehistory(date))

@app.route('/cleanup', methods=['POST','GET'])
def clean_up():
    return(clean(table))

@app.route('/find', methods=['POST','GET'])
def find_out():
    return(find(date_money))

if __name__ == "__main__":
    app.run(host='your.ip',port=port of your.ip, debug=True)
     