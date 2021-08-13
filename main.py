# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

# goldfish
cracked_password = password_cracker.crack_sha1_hash(
    "fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
print(cracked_password)

# sammy123
cracked_password = password_cracker.crack_sha1_hash(
    "b305921a3723cd5d70a375cd21a61e60aabb84ec")
print(cracked_password)

# password
cracked_password = password_cracker.crack_sha1_hash(
    "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
print(cracked_password)

# letmein
cracked_password = password_cracker.crack_sha1_hash(
    "dcc466796201f7232b22a03781110a8871fd038c", use_salts=True)
print(cracked_password)

# superman
cracked_password = password_cracker.crack_sha1_hash(
    "53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)
print(cracked_password)

# q1w2e3r4t5
cracked_password = password_cracker.crack_sha1_hash(
    "da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)
print(cracked_password)

# Run unit tests automatically
main(module='test_module', exit=False)
