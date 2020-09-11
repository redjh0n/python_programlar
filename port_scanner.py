import socket 
import sys

print("""***********PORT SCANNER TOOL***********""")


if len(sys.argv) < 2:
    print("Type 'python3 port_scanner.py --help' to find out how the program works.")

elif sys.argv[1] == "--help":
    print("""
"python3 port_scanner.py ip first_range last_range"

ip: ip address to scan
first_range: first port to scan
last_range: last port to scan 
""")

else:
     
    soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = sys.argv[1]

    range_port1 = sys.argv[2]
    range_port2 = sys.argv[3]

    remoteServerIP  = socket.gethostbyname(host)    
    
    for port in range(int(range_port1),int(range_port2)):
        connect = soket.connect_ex((remoteServerIP,port))
    
        if connect == 0:
            print("open:",port)
    
        else:
            continue
        soket.close()
    
    
    