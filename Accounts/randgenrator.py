import random
import string
def rand(length):
    letters=string.ascii_letters+'1234567890'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str