#!/usr/bin/env python3

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <input name="user_input0">
         <input name="user_input1">
         <input name="user_input2">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text0 = request.form.get("user_input0", "")
    input_text1 = request.form.get("user_input1", "")
    input_text2 = request.form.get("user_input2", "")
    return "You entered: " + input_text0 + " " + input_text1 + " " + input_text2


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    '''
    Get the value of 1 USD to GBP
    '''
    def _get_exchange_rate(self):
        response = requests.get("https://api.frankfurter.app/latest?from=USD&to=GBP")
        return response.json()['rates']['GBP']
    
    '''
    Do the conversion
    '''
    def usd_to_gbp(self, amt_in_usd):
        exchange_rate = self._get_exchange_rate()
        return amt_in_usd * exchange_rate

