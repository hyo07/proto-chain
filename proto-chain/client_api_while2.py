import signal
from time import sleep
import json
from libs import call_api2

from core.client_core import ClientCore
from p2p.message_manager import MSG_NEW_TRANSACTION

my_p2p_client = None


def signal_handler(signal, frame):
    shutdown_client()


def shutdown_client():
    global my_p2p_client
    my_p2p_client.shutdown()


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client
    my_p2p_client = ClientCore(50095, '10.97.74.93', 50090)

    # sleep(10)

    while True:
        try:
            my_p2p_client.start()
        except ConnectionRefusedError:
            sleep(5)
            continue
        sleep(10)
        tran_list = call_api2.call_api()
        for tran in tran_list:
            my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(tran))
        try:
            shutdown_client()
        except ConnectionRefusedError:
            sleep(19)
            continue
        sleep(19)


if __name__ == '__main__':
    main()
