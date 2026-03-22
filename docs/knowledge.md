# ナレッジ

- alembic
  - alembicはDBの変更をコードで管理できるようにし、バージョン管理できるようにしたもの。
  - alembicの設定
    - compose.ymlにdbのコンテナを書いてweb用のコンテナと繋げるようにする。
    - requirements.txtにalembicを書く。
    - models.pyに最初のDBの構成を書く、今回はSQLAlchemyで定義した。
    - devcontainerやdocker compose execなりでweb用のコンテナに入り、alembic initする。生成されたenv.pyとalembic.iniを変更する。
    - alemmbic revisionを実行する。その後alembic upgradeする。


webコンテナとdbコンテナの接続
- dbコンテナの立ち上がりが完了する前に接続しに行って繋がらなくて終了ということがある。
- compose.ymlにhealthcheckを書くで対応できそう。