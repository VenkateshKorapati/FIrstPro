import time
import gc
class Test:
    def __init__(self):
        
        print('Object intialization...')

    def __del__(self):
        
        print('FullFilling last wish and performing Cleaning Activities...')

l=[Test(),Test(),Test()]
time.sleep(10)
l=None
time.sleep(10)
print('End of application..')
