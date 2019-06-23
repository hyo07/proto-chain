import signal

from core.observer import ObserverCore

my_p2p_server = None


def signal_handler(signal, frame):
    shutdown_server()


def shutdown_server():
    global my_p2p_server
    my_p2p_server.shutdown()


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_server
    my_p2p_server = ObserverCore(50077, '192.168.11.32', 50082)
    my_p2p_server.start()
    my_p2p_server.join_network()
    my_p2p_server.get_all_chains_for_resolve_conflict()


if __name__ == '__main__':
    main()
