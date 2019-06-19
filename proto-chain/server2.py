import signal
import sys

from core.server_core import ServerCore


args = sys.argv
my_p2p_server = None


def signal_handler(signal, frame):
    shutdown_server()


def shutdown_server():
    global my_p2p_server
    my_p2p_server.shutdown()


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_server

    # my_p2p_server = ServerCore(50090, connect_ip, core_port=50082)
    try:
        if args[2]:
            my_p2p_server = ServerCore(50090, args[1], int(args[2]))
        elif args[1]:
            my_p2p_server = ServerCore(50090, args[1])
    except IndexError:
        my_p2p_server = ServerCore(50090)

    my_p2p_server.start()
    my_p2p_server.join_network()


if __name__ == '__main__':
    main()
