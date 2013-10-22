import random
from socket import *
from datetime import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect(('', 12000))
clientSocket.settimeout(1)
for x in range(1, 11):
    message = 'Ping '+str(x)+' '+date.today().isoformat()+' T '
    message += str(datetime.now().minute)+':'+str(datetime.now().second)+' UTC'
    #print 'Sending to Server: \'{0}\''.format(message)
    print message
    sent_time = time.time() * 1000
    try:
        clientSocket.send(message)
        message2, address = clientSocket.recvfrom(1024)
        recv_time = time.time() * 1000
        #print 'Received from Server: \'{0}\''.format(message2)
        print message2
        print 'RTT: {0}\n'.format(round(recv_time-sent_time, 3))
    except timeout:
        print 'Request timed out\n'
clientSocket.close()

