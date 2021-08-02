# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:32:57 2021

@author: nsp27
"""

from flask import Flask, render_template , request
import pickle

model = pickle.load(open("body.pkl",'rb'))


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/guest', methods = ["POST"])
def guest():
  sc = request.form["sc"]
  m = request.form["m"]
  cb = request.form["cb"]
  hos = request.form["hos"]
  boa = request.form["boa"]
  wk = request.form["wk"]
  data = [[int(sc),int(m),int(cb),int(hos),int(boa),int(wk)]]
  prediction = model.predict(data)
    
  return render_template("index.html",y = "For The Body Fitness Prediction Could Be  : " + str(prediction))
app.run(debug = True) 