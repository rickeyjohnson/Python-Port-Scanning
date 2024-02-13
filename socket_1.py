# imported socket & time
from socket import *
import time
startTime = time.time()

if __name__ = '__main__':
    # target gets the hostname from user
    target = input('Enter the host to be scanned: ')
    # gethostname() acquires IP address from hostname inputed
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    # runs loop from port 0 to port 65535
    for i in range(0, 65535):
        # initiliazes socket class
        s = socket(AF_INET, SOCK_STREAM)

        # connect uses TCP connect scan to connect and find open ports -- returns 0 of if port is open
        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
    print('Time taken:', time.time() - startTime) # displays time it took to run program