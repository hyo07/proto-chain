import signal
from time import sleep
import json
import call_api

from core.client_core import ClientCore
from p2p.message_manager import MSG_NEW_TRANSACTION

my_p2p_client = None


def signal_handler(signal, frame):
    shutdown_client()


def shutdown_client():
    global my_p2p_client
    my_p2p_client.shutdown()


def main():
    """
    一生API回し、それをトランザクションとして送り続ける。おくりびと。
    """

    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client
    my_p2p_client = ClientCore(50097, '10.97.74.93', 50082)

    while True:
        my_p2p_client.start()
        sleep(10)
        tran_list = call_api.call_api()
        for tran in tran_list:
            my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(tran))
        try:
            shutdown_client()
        except ConnectionRefusedError:
            sleep(5)
            continue
        sleep(4.5)


if __name__ == '__main__':
    main()
