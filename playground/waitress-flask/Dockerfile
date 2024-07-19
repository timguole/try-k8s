FROM ubuntu:24.04
RUN apt-get update && apt-get -y install curl dnsutils busybox python3 python3-flask python3-redis python3-waitress
WORKDIR /app
COPY wsgi.py wsgi.py
COPY README README
COPY entrypoint.sh /entrypoint.sh
COPY cmd.sh /cmd.sh
EXPOSE 80/tcp
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/cmd.sh"]
