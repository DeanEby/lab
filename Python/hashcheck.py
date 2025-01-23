import hashlib

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


passwords = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
count = 1
for i in passwords:
    print(count)
    print(hash_pw(i))
    count = count + 1