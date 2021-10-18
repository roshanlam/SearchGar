import time
import traceback
import cv2
from build.module_name import *

def call_and_print_exc(fn):
    try:
        fn()
    except Exception:
        traceback.print_exc()
    
start = time.time()
print(f"Threaded fun took {time.time() - start} seconds")
