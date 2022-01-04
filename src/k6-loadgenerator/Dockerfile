FROM loadimpact/k6:latest

USER root
WORKDIR /load
COPY --chown=root:root ./loadgenerator.js /load


ENTRYPOINT ["k6","run", "/load/loadgenerator.js", "-u", "10", "-d", "24h"]