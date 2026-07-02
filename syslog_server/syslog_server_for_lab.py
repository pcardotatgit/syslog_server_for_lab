# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''
    description : syslog server for the secu lab
'''
import env as env
from crayons import *
from analyse_application_logs import loguer
import socketserver
from datetime import datetime, date, timedelta
import sys

dateTime = datetime.now()
HOST, PORT = "0.0.0.0", 514

# here under syslog server functions
class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        global use_webex_bot
        # get syslog message receive in the socket
        data = bytes.decode(self.request[0].strip())
        socket = self.request[1]
        syslog=str(data) # put it into the syslog variable
        print(yellow(syslog))
        # ##################################################################################################
        # MESSAGE FILTER HERE UNDER : SELECT Syslog messages to save into output files thanks to keyword searches
        # ##################################################################################################
        if '%FTD' in syslog:
            print(cyan('CAPTURED MESSAGE :\n',bold=True))
            print(cyan(syslog,bold=True))
            with open('./result/ftd_syslogs.txt','a+') as file:
                file.write(syslog+'\n')
        if 'CISE' in syslog:
            print(cyan('CAPTURED MESSAGE :\n',bold=True))        
            print(cyan(syslog,bold=True))
            with open('./result/ise_syslogs.txt','a+') as file:
                file.write(syslog+'\n')

                
if __name__=="__main__":
    print()
    print(env.level,white("MAIN FUNCTION ( the syslog server starts here ): >",bold=True))
    with open("./debug/log.txt","w") as file:
        pass
    loguer(env.level+" SYLOG SERVER STARTS")
    try:
        print('\n Let\'s start Syslog Server - listening on UDP 514')
        print(green(' All Good - listening on UDP 514 waiting for syslog messages',bold=True))
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)        
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")    
