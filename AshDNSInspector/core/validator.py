import socket
def domain_validate():
 while True:

    try:

        domain = input("Enter Domain : ")
        host = socket.gethostbyname(domain)
        break

    except Exception as e:

        print("validation failure", e)
        continue

 return domain