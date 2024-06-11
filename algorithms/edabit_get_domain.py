import socket


def get_domain(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"


print(get_domain("8.8.8.8"))
print(get_domain("8.8.4.4"))
