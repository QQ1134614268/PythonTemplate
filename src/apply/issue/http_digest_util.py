import hashlib


def get_response(username, realm, password, method, uri, nonce, nc, qop, cnonce):
    # response = MD5(MD5(username:realm:password):nonce:nc:cnonce:qop:MD5(<request-method>:url))
    ha1 = hashlib.md5(f'{username}:{realm}:{password}'.encode('utf-8')).hexdigest()
    ha2 = hashlib.md5(f'{method}:{uri}'.encode('utf-8')).hexdigest()
    return hashlib.md5(f'{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}'.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    res = get_response("aaa", "no auth", "123", "GET", "/BootDemo/login", "rULh6M3A6O2N8jjzxr6vJg==", "00000001",
                       "auth", "2ba7cc66c38cb785")
    print(res == "488d501c80ff7ac9a02bdf0b78125b6e")
