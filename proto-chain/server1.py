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
    # 始原のCoreノードとして起動する
    my_p2p_server = ServerCore(50082, core_node_host=None, core_node_port=None)
    my_p2p_server.start()


if __name__ == '__main__':
    main()
