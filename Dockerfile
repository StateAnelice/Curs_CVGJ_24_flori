FROM python:3.8-alpine
ENV FLASK_APP trandafir
RUN adduser -D trandafir
USER trandafir
WORKDIR /home/proiect/Curs_CVGJ_24_flori
COPY app app
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r app/quickrequirements.txt
WORKDIR /home/proiect/Curs_CVGJ_24_flori/app
EXPOSE 5000
ENTRYPOINT ["./dockerstart.sh"]