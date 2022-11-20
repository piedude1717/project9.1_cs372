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
    print(s)

    ready_set = {s}
    print("hi0")
    ready_to_read, _, _ = select.select(ready_set, {}, {})
    print('hi1')
    for s in ready_to_read:
        data = s.recv(port)
        print("this is data" + str(data))


    while True:
        response = client.recv(port).decode()

        print(len(response))

        if len(response) <= 0:
            client.close()
            s.close()
            print("hi")
            break

        print(response)



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
