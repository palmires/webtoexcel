# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import session
from writer import *
app.secret_key = 'A3482hAWDhl^&23kjl124,iqP'

table1 = {"":["a","b","c"],u"Пакет":["","",""],"Pack":["","",""]}
table2 = {"":["d","e"],"PSDF":["",""]}
table3 = {"":["AS","ASD"],"QWE":["",""]}
tables = {"1":table1,"2":table2,"3":table3}
@app.route("/table/<username>/<password>/<ids>", methods=['GET'])
def show_start_table(ids,username,password):
	if valid_login(username,password):
		if ids in tables.keys():
			table = tables[ids]
			return render_template('index.html', table=table)
		return redirect(url_for('show_start_table',ids=1,username=username,password=password))
	return redirect(url_for('login'))

@app.route('/table/<username>/<password>/<ids>', methods=['POST'])
def accept_table_value(ids,username, password):
	json_table = request.get_json()
	print (json_table)
	print(username,password)
	json_to_excel(json_table,username+'.xlsx')
	return "Success"

@app.route("/", methods=['POST','GET'])
@app.route("/login", methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			#return log_the_user_in(request.form['username'])
			session['username'] = request.form['username']
			return redirect(url_for('show_start_table',ids=1,username=request.form['username'],password=request.form['password']))
		else:
			error = 'Invalid username/password'
	return render_template('login.html', error=error)

def valid_login(username, password):
	users = {"admin":"password","user":"qwerty"}
	if username in users.keys():
		if users[username] == password:
			return True
		else:
			return False
	else:
		return False