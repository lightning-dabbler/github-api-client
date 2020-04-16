# Bundle files to dist

FROM node:12.16.1-slim as build-stage

WORKDIR /client

COPY . .
 
ENV GITHUB_API_NET http://github_api_prod:2067
ENV GITHUB_API_WEB http://localhost:5067
ENV REDIS_URL_NET redis://redis_prod:6379
ENV WEB_URL http://localhost:80

RUN npm install -g npm \
    && npm install -g --force yarn \
    && yarn install \
    && yarn build

# Serve dist with NGINX

FROM nginx as production-stage

RUN apt-get update \
    && apt-get install nginx-extras -y

COPY --from=build-stage /client/dist /usr/share/nginx/html
COPY --from=build-stage /client/nginx-conf/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD nginx -g 'daemon off;'