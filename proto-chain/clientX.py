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


def make_transaction():
    """
    好きなトランザクションを書き込む
    """

    transaction_list = []
    print("トランザクションを登録できます\n"
          "中断する場合は、'Ctlr + C'を入力してください\n")

    while True:
        transaction = input_set()
        transaction_list.append(transaction)
        select_num = check_continue_input()
        if select_num is 1:
            pass
        elif select_num is 2:
            print("5秒後、トランザクションを送信します\n"
                  "中断する場合は、'Ctlr + C'を入力してください")
            sleep(5)
            break

    return transaction_list


def input_set():
    """
    値受け取り部分
    """

    print("-------------------------\n"
          "トランザクション登録")
    sender = input("sender: ")
    recipient = input("recipient: ")
    value = input("value: ")

    return {'sender': sender, 'recipient': recipient, 'value': value}


def check_continue_input():
    """
    登録を続行か、送信かの選択
    """

    print("続く操作を選択してください")
    while True:
        select_num = input(""" 
        1: トランザクションの登録を続ける
        2: 登録したトランザクションを送信する
        >>>>> """)
        if (select_num == "1") or (select_num == "2"):
            break
        else:
            print("正しい値を入力してください（1 or 2）")
    return int(select_num)


def main():

    transaction_list = make_transaction()
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
        sleep(3)

    sleep(10)
    shutdown_client()


if __name__ == '__main__':
    main()

