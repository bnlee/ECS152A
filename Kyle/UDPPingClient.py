import random
from socket import *
from datetime import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect(('', 12000))
clientSocket.settimeout(1)
for x in range(1, 10):
  message = 'Ping '+str(x)+' '+date.today().isoformat()+' T '
  message += datetime.now().time().isoformat()+' UTC'
  print message
  clientSocket.send(message)
  message2, address = clientSocket.recvfrom(1024)
  print message2
  print 'RTT: \n'
clientSocket.close()

