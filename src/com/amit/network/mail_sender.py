'''
Created on 8 Mar. 2018

@author: Amit.Kumar1
'''
import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('amit.kumar1@health.telstra.com', 'amit.kumar1@health.telstra.com', 'Hello, test')
server.quit()


