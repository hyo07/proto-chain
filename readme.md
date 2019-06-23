**このプログラムは、[ゼロから創る暗号通貨](https://peaks.cc/books/cryptocurrency)さんのプログラムを元にしています。**

ブロック作成の難易度: 3桁（bc03-parallel/04/blockchain/block.py）  
正当性チェックの難易度: 2桁（bc03-parallel/04/blockchain/blockchain_manager.py）


## プログラム実行手順

```commandline
git clone https://github.com/hyo07/proto-chain.git
cd proto-chain
```

```commandline
docker build -t {image_name} .
docker run -it {image_name} python {file_name} {接続先IP} {接続先port}
```
`server1.py`を起動するときのみ、IPやportなどの引数はいらない。  
引数に関することは後述。  
<br>
また、
```commandline
docker-compose up --build
```
で、server３種を一括で起動。このとき、環境によってはIPアドレスが変わってしまうため、  
その場合は`docker-compose.yaml`のENDPOINTを書き換える。  

docker-composeで一括起動をした場合、は、
```commandline
docker network ls
docker run -it --net={network_name} {image_name} python {file_name} {接続先IP} {接続先port}
```
以上のように、ネットワークを指定すると、別ターミナルから接続できる。もちろんcomposeを書き換えるのもあり。  

## 実行時の引数
`server1.py`以外のserver, clientのプログラムには引数を与えることが可能。
- 第１引数: 接続先IPアドレス
- 第２引数: 接続先ポート

なにも引数を与えない場合、デフォルトで`server1.py`のノードに接続される設定にされている（ip: 172.17.0.2, port: 50082）。  
デフォルトの接続先を変えたい場合は、`core/client_core.py, server_core.py`の各コンストラクタの第２・第３引数を変更してください。


## 課題
- edgeノードからトランザクションを送信したとき、漏れが発生して、coreノードが受けれていないときがある
    - 各トランザクションを送るときに、sleep(2)を入れたら、今の所漏れはなくなっている
    - sleep(1)だと漏れることある
    - 違う設計やデータを扱うときには、2秒じゃ無くなる可能性あるから困る
# **上の課題について**
ローカルで同じ処理を行うと、60トランザクションをsleep(0)で行っても漏れがなかった。  
dockerの問題な模様？

# 更新
- observer周り
    - ブロックチェーンをsqliteに保存する周り。DB設計とかsqilte使ってることとかは仮置き