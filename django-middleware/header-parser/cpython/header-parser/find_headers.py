valid_user_agent_header_formats = (
    "useragent",
    "user_agent",
    "http_user_agent",
    "request_user_agent",
    "http_request_user_agent",
)


def get_user_agent(headers):
    for k, v in headers.items():
        for user_agent_format in valid_user_agent_header_formats:
            if k.lower().replace("-", "_") == user_agent_format:
                return v
    return None
