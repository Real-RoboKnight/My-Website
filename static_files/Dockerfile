
FROM node AS bootstrap

WORKDIR /app
RUN npm install sass bootstrap
# ENV SASS_PATH=node_modules 

COPY Bootstrap /app
RUN npx sass --load-path=node_modules --quiet-deps ./custom.scss custom.css

FROM node AS typescript-compiler

WORKDIR /app
COPY Typescript/package*.json ./
RUN npm install 

COPY Typescript/ ./
RUN npm run build

FROM nginx:alpine

COPY ["[0-9]*.sh", "docker-entrypoint.d/"]

WORKDIR /app

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=bootstrap /app/custom.css /app
COPY --from=bootstrap /app/custom.css.map /app
COPY --from=bootstrap /app/node_modules/bootstrap/dist/js/bootstrap.bundle.min.js /app
COPY --from=bootstrap /app/node_modules/bootstrap/dist/js/bootstrap.bundle.min.js.map /app

COPY --from=typescript-compiler /app/node_modules/katex/dist/ /app/katex

COPY --from=typescript-compiler /app/app.min.js /app
COPY --from=typescript-compiler /app/app.min.js.map /app

COPY Files/ /app/
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]