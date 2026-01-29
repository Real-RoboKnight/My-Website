FROM nginx:alpine

RUN mkdir -p /app/log

COPY 50-test-config.sh docker-entrypoint.d

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY Files /app
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]