FROM nginx:alpine

RUN mkdir -p /app/log


RUN rm /etc/nginx/conf.d/default.conf
COPY ngenx.conf /etc/nginx/nginx.conf

# Test Nginx config and abort build if invalid
RUN nginx -t

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]