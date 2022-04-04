with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('G'):line.find(' /')]
        requested_resource = line[line.find('/d'):line.find(' HTTP')]
        new_log = (remote_addr, request_type, requested_resource)
        print(type(new_log), new_log)






    # remote_addr = line.split(' - - ')[0].split(' ')
    # request_type = line.split(' H')
