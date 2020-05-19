FROM redis:6.0-rc2

# Needed for envsubst
RUN apt-get update && \
    apt-get install -y gettext-base && \
    apt-get autoremove -y

COPY redis.conf /source-dir/template.conf
COPY entrypoint.sh /source-dir/entrypoint.sh

ENTRYPOINT [ "sh","/source-dir/entrypoint.sh" ]