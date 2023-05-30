import random
import string
import time


while True:
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
    print(f'{timestamp} {random_string}')
    time.sleep(5)