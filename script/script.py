from sample_headers import HEADERS
from find_headers import find_user_agent_header


if __name__ == "__main__":
    import timeit

    print("Header: %s" % find_user_agent_header(HEADERS))
    print(
        "timeit: %f"
        % timeit.timeit("find_user_agent_header(HEADERS)", globals=globals())
    )
