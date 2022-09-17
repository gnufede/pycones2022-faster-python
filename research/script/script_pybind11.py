from pybind11string import (
    cfind_user_agent_header,
)
from sample_headers import HEADERS

if __name__ == "__main__":
    import timeit

    print("Header: %s" % cfind_user_agent_header(HEADERS))
    print(
        "timeit: %f"
        % timeit.timeit("cfind_user_agent_header(HEADERS)", globals=globals())
    )
