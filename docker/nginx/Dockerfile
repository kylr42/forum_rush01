FROM nginx:1.21-alpine

WORKDIR /usr/src/app


RUN openssl req -newkey rsa:4096 -x509 -sha256 -days 1 -nodes \
    -out ssl.crt -keyout ssl.key \
    -subj "/C=RU/ST=Russia/L=Moscow/O=School 21/OU=Forum/CN=localhost" && \
    chmod 644 ssl.crt ssl.key && \
    mkdir -p /etc/ssl/certs /etc/ssl/private && \
    mv ssl.crt /etc/ssl/certs && \
    mv ssl.key /etc/ssl/private


RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

