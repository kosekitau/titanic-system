FROM python:3.12-bookworm

# パッケージのインストール
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        ca-certificates curl fonts-ipafont-gothic gcc git locales sudo tmux tzdata vim zsh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 言語設定
RUN echo "ja_JP UTF-8" > /etc/locale.gen && \
    locale-gen ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LC_ALL=ja_JP.UTF-8
ENV TZ=Asia/Tokyo


WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt
