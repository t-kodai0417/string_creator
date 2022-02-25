import random,string
def create(l):
    return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l)))
