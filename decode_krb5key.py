#!/usr/bin/python3
# -*- coding: utf-8 -*-

import binascii
import heimdal
import base64
import argparse

krb5_keytype__des_cbc_crc = 1
krb5_keytype__des_cbc_md4 = 2
krb5_keytype__des_cbc_md5 = 3
krb5_keytype__des3_cbc_sha1 = 16
krb5_keytype__aes128_cts_hmac_sha1_96 = 17
krb5_keytype__aes256_cts_hmac_sha1_96 = 18
krb5_keytype__arcfour_hmac_md5 = 23

def extract_NThash_from_krb5key(ucs_krb5key):

    NThash = None

    keyblock,salt,kvno = heimdal.asn1_decode_key(base64.b64decode(ucs_krb5key))

    if keyblock.keytype().toint() == krb5_keytype__arcfour_hmac_md5:
        NThash = binascii.hexlify(keyblock.keyvalue()).decode('utf-8')
    else:
        print(f'Keytype is: ', keyblock.keytype().toint())

    return NThash


def main():
    parser = argparse.ArgumentParser(
            prog='decode_krb5key.py',
                    description='Simple tool to extract ntlm hash out of the arcfour_hmac_md5 krb5key used by univention ucs')
    parser.add_argument('-d', help="put your base64 encoded krb5key value here", required=True)
    args = parser.parse_args()
    nt_hash = extract_NThash_from_krb5key(args.d)
    print("NThash: ",nt_hash)


if __name__ == '__main__':
    main()

