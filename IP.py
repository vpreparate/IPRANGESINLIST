import ipaddress

# Открываем файл с диапазонами IP-адресов для чтения
with open('ranges.txt', 'r') as f:
    # Читаем файл построчно
    for line in f:
        # Удаляем пробелы и символы переноса строки
        line = line.strip()

        # Разбиваем строку на два IP-адреса
        start_ip, end_ip = line.split('-')

        # Преобразуем IP-адреса в объекты типа ipaddress.IPv4Address
        start_ip = ipaddress.IPv4Address(start_ip)
        end_ip = ipaddress.IPv4Address(end_ip)

        # Вычисляем количество IP-адресов в диапазоне
        num_ips = int(end_ip) - int(start_ip) + 1

        # Создаем список IP-адресов в диапазоне
        ips = [str(start_ip + i) for i in range(num_ips)]

        # Записываем список IP-адресов в файл
        with open('ips.txt', 'a') as f1:
            f1.write('\n'.join(ips) + '\n')
