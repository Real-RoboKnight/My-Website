
FROM node AS bootstrap

WORKDIR /app
RUN npm init -y
RUN npm install bootstrap
RUN npm install sass
ENV SASS_PATH=node_modules

COPY Bootstrap/custom.scss ./custom.scss

RUN npx sass --load-path=node_modules --quiet-deps ./custom.scss custom.css

FROM nginx:alpine

COPY ["[0-9]*.sh", "docker-entrypoint.d/"]

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY Files /app
COPY --from=bootstrap app/custom.css /app
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]