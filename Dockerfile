# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster


WORKDIR "/app"

RUN pip install flask && mkdir -p /var/miniweb && touch /var/miniweb/chat

EXPOSE 8080

COPY ["./miniweb.py", "/app"]

CMD ["flask", "--app", "/app/miniweb", "run", "--host=0.0.0.0", "-p", "8080"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]
