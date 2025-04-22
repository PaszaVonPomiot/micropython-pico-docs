"""
Test how many elements can fit into memory.
"""

import gc

memory_element = "1609459201;23.77;980.30"


def test_memory_limit():
    gc.collect()
    print("Free mem before:", gc.mem_free())

    blocks = []
    try:
        while True:
            blocks.append(memory_element)
            print(len(blocks))
    except MemoryError:
        print("MemoryError reached.")
        print("Free mem after:", gc.mem_free())


test_memory_limit()
