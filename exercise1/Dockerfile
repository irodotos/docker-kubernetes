FROM nginx:1.23.3-alpine


RUN apk update && \
    apk add git && \
    apk add hugo && \
    apk add make && \
    git clone https://github.com/chazapis/hy548 && \
    cd hy548 && \
    git submodule update --init --recursive && \
    make all && \
    cp -r html/public/* /usr/share/nginx/html && \
    rm -rf /var/lib/apt/lists/*
