import hashlib

def crack_sha1_hash(hash, **use_salts):
    with open("top-10000-passwords.txt") as file1:
        passwords = file1.read().splitlines()
    
    if use_salts:
        with open("known-salts.txt") as file2:
            salts = file2.read().splitlines()
        for salt in salts:
            for password in passwords:
                salted_password_pre = str(salt) + str(password)
                if hash == hashlib.sha1(str(salted_password_pre).encode('utf-8')).hexdigest():
                    return password
                salted_password_post = str(password) + str(salt)
                if hash == hashlib.sha1(str(salted_password_post).encode('utf-8')).hexdigest():
                    return password
    else:
        for password in passwords:
            if hash == hashlib.sha1(str(password).encode('utf-8')).hexdigest():
                return password

    return "PASSWORD NOT IN DATABASE"