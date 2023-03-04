from ClientLibrary import Client

client = Client()

while True:
    func = input('>> ')
    splitted_func = func.split(' ')

    if splitted_func[0] == 'add_node':
        answer = client.add_node(splitted_func[1])
        print(answer)
    elif splitted_func[0] == 'remove_node':
        answer = client.remove_node(splitted_func[1])
        print(answer)
    elif splitted_func[0] == 'push_message':
        answer = client.push_message(func.replace('push_message ', ''))
        print(answer)
        if client.get_count() == 5:
            print('Status: ')
            print(client.get_status())
            client.reset_count()
    elif splitted_func[0] == 'get_message':
        answer = client.get_message()
        print(answer)
    elif splitted_func[0] == 'get_status':
        answer = client.get_status()
        print(answer)
    elif splitted_func[0] == 'exit':
        exit(0)
    else:
        print('ERROR INPUT')
