import random
import string
def string_py(l):
    global data
    data=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l)))

