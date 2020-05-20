# Bundle files to dist

FROM node:12.16.1-slim as build-stage

WORKDIR /client

COPY . .

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