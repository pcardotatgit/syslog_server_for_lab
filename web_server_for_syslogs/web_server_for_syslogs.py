# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''
    description : expose syslog message thru flask web server
'''
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
import sys
from crayons import *
from werkzeug.utils import secure_filename
import random
from datetime import datetime, timedelta
import socket
import webbrowser
import threading
import time
import glob
import signal
import requests
import json
import hashlib
from pathlib import Path
from inspect import currentframe
import subprocess
import shutil
import env as env
#import sqlalchemy
#from sqlalchemy.orm import sessionmaker
#from tabledef import *
#import sqlite3
#import struct
#import csv
#import pandas as pd
#from pandas import DataFrame

app = Flask(__name__)

#  def_loguer***
def loguer(log):
    '''
    MODIFIED : 2025-06-19T15:52:21.000Z

    description : log when a function or a route is called with start date
    '''
    time = datetime.now().isoformat()
    #print(time)
    log=log+' at '+ time
    with open(f'./debug/log.txt','a+') as file:
          file.write(log+'\n')
    return 1
    



# def_open_browser_tab***
def open_browser_tab(host, port):
    env.level+='-'
    '''
        open web browser on login page
    '''
    print()
    print(env.level,white('def open_browser_tab() : > in app.py  : >\n',bold=True))
    loguer(env.level+' def open_browser_tab() : > in app.py  : > ')
    print()
    url = 'http://%s:%s/' % (host, port)

    def _open_tab(url):
        time.sleep(1.5)
        webbrowser.open_new_tab(url)

    thread = threading.Thread(target=_open_tab, args=(url,))
    thread.daemon = True
    thread.start() 
    env.level=env.level[:-1]
    return 1   

#  def_ise***
@app.route('/ise', methods=['GET'])
def ise():
    '''
    MODIFIED : 2026-07-02T16:35:42.000Z

    description : return ise syslogs
    '''
    route="/ise"
    env.level+='-'
    print('\n'+env.level,white('route ise() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route ise() in ***app.py*** : >')
    with open('./result/ise_syslogs.txt') as file:
        txt_content=file.read()
    env.level=env.level[:-1]
    return txt_content
        

#  def_fmc***
@app.route('/fmc', methods=['GET'])
def fmc():
    '''
    MODIFIED : 2026-07-02T16:35:42.000Z

    description : return fmc syslogs
    '''
    route="/fmc"
    env.level+='-'
    print('\n'+env.level,white('route fmc() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route fmc() in ***app.py*** : >')

    with open('./result/fmc_syslogs.txt') as file:
        txt_content=file.read()
    env.level=env.level[:-1]
    return txt_content
        

#  def_ise_failed_attempts***
@app.route('/ise_failed_attempts', methods=['GET'])
def ise_failed_attempts():
    '''
    MODIFIED : 2026-07-07T09:36:58.000Z

    description : read and return ise_failed_attempts logs
    '''
    route="/ise_failed_attempts"
    env.level+='-'
    print('\n'+env.level,white('route ise_failed_attempts() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route ise_failed_attempts() in ***app.py*** : >')
    with open('./result/ise_failed_attempts_syslogs.txt') as file:
        txt_content=file.read()
    env.level=env.level[:-1]
    return txt_content
        


@app.route('/', methods=['GET'])
def index():
    '''
    version:

    description : index page
    '''
    route="/index"
    env.level+='-'
    print('\n'+env.level,white('route index() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route index() in ***app.py*** : >')
    # ===================================================================
    env.level=env.level[:-1]
    return render_template('index.html')
  
    
if __name__=="__main__":
    print(env.level,white("MAIN FUNCTION ( the application starts here ): >",bold=True))
    with open("./debug/log.txt","w") as file:
        pass
    loguer(env.level+" APPLICATION STARTS")
    host="127.0.0.1"
    #open_browser_tab(host,4000)
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=4000)
    
