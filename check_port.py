import telnetlib

def check_port(host, port):
    try:
        tn = telnetlib.Telnet(host, port)
        print(f"Port {port} is open on {host}")
        tn.close()
    except ConnectionRefusedError:
        print(f"Port {port} is closed on {host}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = input("Enter the host IP address or hostname: ")
    port = input("Enter the port number: ")
    check_port(host, int(port))