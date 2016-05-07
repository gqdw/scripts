import random
import string
lt2=string.digits + string.ascii_letters
lt1='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print ''.join(random.choice(lt2) for i in range(10))
