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
docker run -it {image_name} bash
```
コンテナを起動し、２番目のコマンドで起動してあるコンテナにbashで入れます。  
その後、
```commandline
root@hoge:/{image_name}# python server1.py
```
とすれば、そのコンテナで`server1.py`を起動できます。  
あとは同じ手順を複数回行い、実行するプログラムを変えれば、仮想敵に別端末を用意し、通信を行わせることができます。  
<br>
かなり酷い使い方だとdocker触りたての私でも分かるため、なるべく早くdocker-composeなりで動くようにしたいと思っています。


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
