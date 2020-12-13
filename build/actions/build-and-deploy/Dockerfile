FROM klakegg/hugo:0.79.0-ext-alpine
RUN apk add --no-cache python3

# アクションのリポジトリからコードファイルをファイルシステムパスへコピー
# `/` of the container
COPY entrypoint.sh /entrypoint.sh

# dockerコンテナが起動する際に実行されるコードファイル (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]