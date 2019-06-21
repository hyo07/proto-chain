import signal
from time import sleep
import json
from libs import call_api
import sys

from core.client_core import ClientCore
from p2p.message_manager import MSG_NEW_TRANSACTION

my_p2p_client = None
args = sys.argv


def signal_handler(signal, frame):
    shutdown_client()


def shutdown_client():
    global my_p2p_client
    my_p2p_client.shutdown()


def main():
    tran_list = call_api.call_api(int(args[1]))
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client

    try:
        if args[3]:
            my_p2p_client = ClientCore(50095, args[1], int(args[2]))
        elif args[2]:
            my_p2p_client = ClientCore(50095, args[1])
        else:
            my_p2p_client = ClientCore(50095)
    except IndexError:
        my_p2p_client = ClientCore(50095)

    my_p2p_client.start()

    sleep(10)

    for tran in tran_list:
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(tran))
        sleep(2)


if __name__ == '__main__':
    main()
