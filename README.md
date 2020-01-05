# velvet-crawler

指定したはてなブログのトップページ URL のドメイン内記事をクロールして、はてなブックマーク数を取得するクローラです。

クロールされたデータは PostgreSQL に保存します。

実装の大部分は、[こちら](https://github.com/Chanmoro/blog_crawler)を参考にしています。

## 実行方法

### はてなブログトップページの指定

１行に1つのトップページを記載したテキストファイルを作成します。例として `crawler/urls.txt.sample` を用意しているので、コピーして用途に合わせて変更してください。

```bash
$ cp crawler/urls.txt.sample crawler/urls.txt
```

### 起動

docker-compose を使用して、アプリケーションを実行します。

```bash
$ docker-compose up -d

# フォアグラウンドで実行したい場合
$ docker-compose up
```

### クロールデータの確認

psql で確認します。

```bash
$ docker-compose exec postgres psql -U docker -d crawler

# psql のコンソールで SQL を実行できます
# crawler=# select * from articles limit 10;
# ...
```
