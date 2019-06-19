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


def input_transaction():
    """
    好きなトランザクションを書き込む（上限３つまで）
    """

    print("トランザクションを３つまで登録できます\n"
          "中断する場合は、'Ctlr + C'を入力してください\n")
    transaction1 = input_set()
    select_num = check_continue_input()
    if select_num != 1:
        print("5秒後、トランザクションを送信します\n"
              "中断する場合は、'Ctlr + C'を入力してください")
        sleep(5)
        return transaction1, None, None

    transaction2 = input_set()
    select_num = check_continue_input()
    if select_num != 1:
        print("5秒後、トランザクションを送信します\n"
              "中断する場合は、'Ctlr + C'を入力してください")
        sleep(5)
        return transaction1, transaction2, None

    transaction3 = input_set()
    print("5秒後、トランザクションを送信します\n"
          "中断する場合は、'Ctlr + C'を入力してください")
    sleep(5)
    return transaction1, transaction2, transaction3


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
    select_num = int(input(""" 
    1: トランザクションの登録を続ける
    2: 登録したトランザクションを送信する
    >>>>> """))
    return select_num


def main():

    transaction1, transaction2, transaction3 = input_transaction()
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

    if transaction1:
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(transaction1))

    if transaction2:
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(transaction2))

    if transaction3:
        sleep(10)
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, json.dumps(transaction3))


if __name__ == '__main__':
    main()
    # transaction1, transaction2, transaction3 = input_transaction()
    # print(transaction1)
    # print(transaction2)
    # print(transaction3)
