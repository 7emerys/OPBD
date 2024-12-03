import ssl
import socket
from datetime import datetime

def get_ssl_expiration_date(hostname):
    """Получает дату окончания действия SSL-сертификата для указанного хоста."""
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiration_date = cert['notAfter']
            expiration_date = datetime.strptime(expiration_date, '%b %d %H:%M:%S %Y %Z')
            return expiration_date

def main():
    hostname = input("Введите адрес сайта (без http/https): ").strip()
    try:
        expiration_date = get_ssl_expiration_date(hostname)
        remaining_days = (expiration_date - datetime.utcnow()).days
        if remaining_days < 0:
            print("SSL-сертификат уже истёк!")
        else:
            print(f"До окончания срока действия SSL-сертификата осталось {remaining_days} дней! Не забудьте обновить сертификат!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
