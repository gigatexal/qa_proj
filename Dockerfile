FROM ubuntu

WORKDIR /qa_app

COPY requirements.txt .
COPY db/*.py ./db/
COPY models/* ./models/
COPY models/Requests/* ./models/Requests/
COPY security/* ./security/
COPY srv/* ./srv/
COPY views/* ./views/
COPY server.py .

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install -r requirements.txt

ENV JWT_EXPIRY=1
ENV JWT_SECRET_KEY="superSecretKEY!!!"
ENV DB_URI="postgresql://postgres@database:5432/qa_db"

EXPOSE 8080

ENTRYPOINT [ "python3", "server.py"]

