from cyscript2 import (
    cfind_user_agent,
    cyfind_user_agent,
)
from sample_headers import HEADERS

if __name__ == "__main__":
    import timeit

    print("Header: %s" % cyfind_user_agent(HEADERS))
    print("timeit: %f" % timeit.timeit("cyfind_user_agent(HEADERS)", globals=globals()))

    print("Header: %s" % cfind_user_agent(HEADERS))
    print("timeit: %f" % timeit.timeit("cfind_user_agent(HEADERS)", globals=globals()))
