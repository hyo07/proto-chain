import signal
from time import sleep
import json
import sys

from core.client_core import ClientCore
from p2p.message_manager import MSG_NEW_TRANSACTION


args = sys.argv
my_p2p_client = None


def signal_handler(signal, frame):
    shutdown_client()


def shutdown_client():
    global my_p2p_client
    my_p2p_client.shutdown()


def make_transaction(num=3):
    """
    好きなトランザクションを書き込む
    """

    transaction_list = []
    print("トランザクションを登録できます\n"
          "中断する場合は、'Ctlr + C'を入力してください\n")

    for i in range(1, num+1):
        transaction_list.append({'sender': i, 'recipient': i, 'value': i})

    return transaction_list


def main():

    tran_num = int(input("送信するトランザクションの数を入力（半角数字）： "))
    transaction_list = make_transaction(tran_num)
    print("------------------------------------------------------------\n")

    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client

    # my_p2p_client = ClientCore(50087, connect_ip, core_port=50082)
    try:
        if args[2]:
            my_p2p_client = ClientCore(50085, args[1], int(args[2]))
        elif args[1]:
            my_p2p_client = ClientCore(50085, args[1])
    except IndexError:
        my_p2p_client = ClientCore(50085)

    my_p2p_client.start()

    sleep(10)

    for transaction in transaction_list:
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(transaction))
        sleep(1)

    sleep(10)
    shutdown_client()


if __name__ == '__main__':
    main()

