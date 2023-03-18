FROM nginx:1.23.3-alpine

RUN apk update && \
    apk add git && \
    apk add hugo && \
    apk add make && \
    git clone https://github.com/chazapis/hy548 && \
    cd hy548 && \
    make all && \
    cd .. && \
    cp hy548/html/public/index.html /usr/share/nginx/html && \
    rm -rf /var/lib/apt/lists/*