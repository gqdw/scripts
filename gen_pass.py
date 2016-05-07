import random
lt1='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print ''.join(random.choice(lt1) for i in range(10))
