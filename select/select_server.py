# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select



def run_server(port):

    ready_set = {}
    addr = ('127.0.0.1', port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen()
    client, addr = s.accept()
    print('(\'127.0.0.1\', ' + str(port) + '): connected')


    while True:
        response = client.recv(port).decode()



        if len(response) <= 0:
            client.close()
            s.close()
            print("hi")
            break

        response = response.split(':')
        response = response[1]
        sent_data = '(\'127.0.0.1\', ' + str(port) + ') ' + str(len(response)) + 'bytes: b\'test1:' + response
        print(sent_data)



#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
