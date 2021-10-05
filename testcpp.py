import time
import traceback
import cv2
from build.module_name import *

from concurrent.futures import ThreadPoolExecutor

def call_and_print_exc(fn):
    try:
        fn()
    except Exception:
        traceback.print_exc()

print(PySomeClass)


m = some_class_factory(10)

m2 = PySomeClass(10)

print(m, m2)

print(m.multiply(20))

# print(m.multiply("20"))

arr = m.multiply_list([0.0, 1.0, 2.0, 3.0])

print(arr)

print(m.multiply_two(50, 200))

print(m.image)

print(m.image.shape)

cv2.imwrite("/tmp/test.png", m.image)

print(m.multiplier)

m.multiplier = 100

print(m.multiplier)

start = time.time()

with ThreadPoolExecutor(4) as ex:
    ex.map(lambda x: m.function_that_takes_a_while(), [None]*4)

print(f"Threaded fun took {time.time() - start} seconds")
