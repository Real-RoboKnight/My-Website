FROM nginx:alpine

COPY ["[0-9]*.sh", "docker-entrypoint.d/"]

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]