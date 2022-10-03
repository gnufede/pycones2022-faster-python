# cython: c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from _cystring cimport cfind_user_agent_header

cpdef str cfind_user_agent(dict headers):
    cdef str res = cfind_user_agent_header(headers)
    return res

cdef tuple valid_user_agent_header_formats = (
    "useragent",
    "user-agent",
    "http-user-agent",
    "request-user-agent",
    "http-request-user-agent",
)
cpdef str cyfind_user_agent(dict headers):
    cdef str m, v, user_agent_format
    for m, v in headers.items():
        for user_agent_format in valid_user_agent_header_formats:
            if m.lower().replace("_", "-") == user_agent_format:
                return v
    return None
