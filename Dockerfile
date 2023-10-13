FROM debian:buster
WORKDIR /root/
COPY python3-univention-heimdal_10.0.1-1A~5.0.0.202302031914_amd64.deb /root/
COPY decode_krb5key.py /root/
RUN apt-get update \
    && apt-get install -y python3 libasn1-8-heimdal libhdb9-heimdal libkrb5-26-heimdal \
    && dpkg -i /root/python3-univention-heimdal_10.0.1-1A~5.0.0.202302031914_amd64.deb
ENTRYPOINT ["python3","/root/decode_krb5key.py"]
