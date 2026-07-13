# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''
    description : read a log file and send it to syslog server
'''
import env as env
import socket
import time
from crayons import *
from analyse_application_logs import loguer
from datetime import datetime, date, timedelta
import sys
import ijson

syslog_server_ip='localhost'
syslog_file='./syslog_files/ise.txt'

#  def send_syslogs***
def send_syslogs(message,syslog_server_ip):
    """
    MODIFIED : 2026-07-01T13:22:18.000Z

    description : send the message to the syslog server
    
    how to call it :
    """
    route="/send_syslogs"
    env.level+="-"
    print("\n"+env.level,white("def send_syslogs() in syslog_message_generator.py : >\n",bold=True))
    #loguer(env.level+" def send_syslogs() in syslog_message_generator.py : >")
    # ===================================================================    
    host=syslog_server_ip
    port=514
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect((host,port))
    b = bytes(message, 'utf-8')
    s.sendall(b)
    s.close()
    # ===================================================================
    #loguer(env.level+" def END OF send_syslogs() in syslog_message_generator.py : >")    
    env.level=env.level[:-1]
    return 1
if __name__=="__main__":
    print(env.level,white("MAIN FUNCTION ( the application starts here ): >",bold=True))
    with open("./debug/log.txt","w") as file:
        pass
    loguer(env.level+" APPLICATION STARTS")
    print(cyan(f'let\'s send syslog messages to {syslog_server_ip} \nSyslog File to send is : '+syslog_file,bold=True))
    a = input('\n Press Enter to Start')
    with open(syslog_file) as file:
        txt_content=file.read()
    lines=txt_content.split('\n')
    for line in lines:
        line=line.strip()
        if line!='':
            print(line)
            send_syslogs(line,syslog_server_ip)
            #time.sleep(0.5)
    print('\nOK ALL DONE\n')
