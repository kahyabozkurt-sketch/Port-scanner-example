import socket

print("Port scanner example")

target_url = "scanme.nmap.org"
target_ip = socket.gethostbyname(target_url)

critic_ports = [21,22,25,80,443,8080]
for port in critic_ports:
    try: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                answer = s.connect_ex((target_ip, port))

                if answer == 0:
                    print(f"Port {port} is open")
                else:
                    print(f"Port {port} is closed or filtered")

    except socket.error:
        print("connection error")



    
