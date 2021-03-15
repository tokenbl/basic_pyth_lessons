
with open('nginx_logs.txt', 'r', encoding='utf-8') as logs_list:

    for i in logs_list:
        content = logs_list.readline().replace('"', ' ').split(' ')
        remote_addr = content[0]
        request_type = content[6]
        requested_resource = content[7]
        list_1 = [remote_addr, request_type, requested_resource]
        print(tuple(list_1))


#pycharm не выводит всё содержимое файла, пришлось запускать код через консоль bash
#с выводом содержимого в отдельный *.txt файл.