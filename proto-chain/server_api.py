import signal
from time import sleep

from core.api_core import APICore

my_p2p_server = None


def signal_handler(signal, frame):
    shutdown_server()


def shutdown_server():
    global my_p2p_server
    my_p2p_server.shutdown()


def get_now_bc():
    re_bc = []

    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_server
    my_p2p_server = APICore(50075, '192.168.11.32', 50082)
    my_p2p_server.start()
    my_p2p_server.join_network()
    sleep(3)
    my_p2p_server.get_all_chains_for_resolve_conflict()

    while len(re_bc) < 2:
        re_bc = my_p2p_server.return_current_blockchain()
        sleep(1)

    shutdown_server()

    return re_bc


if __name__ == '__main__':
    print(get_now_bc())
