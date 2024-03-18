import random
import string

pass_len=10

ran_num = string.ascii_letters+string.punctuation+string.digits

password = ""

for i in range(pass_len):
    password += random.choice(ran_num)

print("Your random password was:",password)     