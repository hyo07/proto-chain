FROM python:latest

COPY ./ /
RUN pip install pycrypto

WORKDIR /proto-chain

CMD echo "plesec command 'docker run -it {REPOSITORY} bash'"
