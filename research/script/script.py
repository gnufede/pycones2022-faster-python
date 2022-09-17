from sample_headers import HEADERS

valid_user_agent_header_formats = (
    "useragent",
    "user-agent",
    "http-user-agent",
    "request-user-agent",
    "http-request-user-agent",
)


def find_user_agent_header(headers):
    for k, v in headers.items():
        for user_agent_format in valid_user_agent_header_formats:
            if k.lower().replace("_", "-") == user_agent_format:
                return v
    return None


if __name__ == "__main__":
    import timeit

    print("Header: %s" % find_user_agent_header(HEADERS))
    print(
        "timeit: %f"
        % timeit.timeit("find_user_agent_header(HEADERS)", globals=globals())
    )
