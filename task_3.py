from tabulate import tabulate

from task_2 import convert_ranges_to_ip_list

from Task_1_1 import ping_ip_addresses


if __name__ == "__main__":
    ip_list = convert_ranges_to_ip_list(
        ['ya.ru', '217.69.128.44', 'dasdasdsadwa', '217.69.128.45-48'])

    print(ip_list)

    dict_of_ips = ping_ip_addresses(ip_list)

    print(dict_of_ips)

    print(tabulate(dict_of_ips, headers='keys',  tablefmt="grid"))
