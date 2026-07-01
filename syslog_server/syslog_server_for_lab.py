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
use_webex_bot=0

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
        # SELECT Syslog messages to save into file
        # #################################################################################################
        if '%FTD' in syslog and 'SID' in syslog and 'PROTOCOL-DNS SPOOF query response with TTL of 1 min. and no authority' not in syslog and 'PROTOCOL-DNS TMG Firewall Client long host entry exploit attempt' not in syslog and 'MALWARE-CNC DNS Fast Flux attempt' not in syslog:
            with open('./result/ftd_syslogs.txt','a+') as file:
                file.write(syslog+'\n')
        if 'CISE_Passed_Authentications' in syslog:
            print(cyan(syslog,bold=True))
            with open('./result/CISE_Passed_Authentications.txt','a+') as file:
                file.write(syslog+'\n')
                
if __name__=="__main__":
    print()
    print(env.level,white("MAIN FUNCTION ( the syslog server starts here ): >",bold=True))
    with open("./debug/log.txt","w") as file:
        pass
    loguer(env.level+" SYLOG SERVER STARTS")
    # set a default infected ip address
    with open('./bad_ip.txt','w') as file:
        file.write('0.0.0.0')    
    try:
        print('\n Let\'s start Syslog Server - listening on UDP 514')
        print(green(' All Good - listening on UDP 514 waiting for syslog messages',bold=True))
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)        
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")    
