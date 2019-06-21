FROM python:latest

RUN pip install pycrypto
RUN pip install requests
COPY ./proto-chain /proto-chain


#WORKDIR /proto-chain

#ENTRYPOINT ["python", "server1.py"]
