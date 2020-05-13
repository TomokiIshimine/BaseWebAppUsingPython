from flask import Flask, render_template, request, redirect, url_for

from main import app

# トップページにアクセスしたとき
@app.route('/')
def index():
  return render_template('index.html')

# /analyzeにアクセスしたとき
@app.route('/analyze', methods=['POST'])
def analyze():
  account_name = request.form['name']
  return render_template('analyze.html', name=account_name)