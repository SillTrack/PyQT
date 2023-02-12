import subprocess


def ping_ip_addresses(ip_list : list):
    reachable = []
    unreachable = []

    for ip in ip_list:
        result = subprocess.run(
                ["ping", '-n', '3' , ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return {'Reachable': reachable, 'Unreachable': unreachable}

if __name__ == '__main__':
    
    print(ping_ip_addresses('sadasdsada'))
