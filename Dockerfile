FROM python:latest

RUN pip install pycrypto
COPY ./proto-chain /proto-chain


#WORKDIR /proto-chain

#ENTRYPOINT ["python", "server1.py"]
