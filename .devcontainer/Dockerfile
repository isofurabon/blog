FROM klakegg/hugo:0.79.0-ext-alpine
# コンテナ上でgit管理するために，git, opensshを追加
# 参考: https://qiita.com/att55/items/045a479dbe06a5299805
RUN apk add --no-cache git openssh python3 py3-pip
RUN pip install pylint