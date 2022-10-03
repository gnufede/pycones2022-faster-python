cdef tuple valid_user_agent_header_formats = (
    "useragent",
    "user_agent",
    "http_user_agent",
    "request_user_agent",
    "http_request_user_agent",
)

cdef str find_user_agent_header(dict headers):
    cdef unsigned char[:] k
    #cdef char* v
    cdef str user_agent_format
    for m, v in headers.items():
        # k = m.encode('utf-8') + b'\x00'
        k = bytearray(str(m), encoding='ascii')
        # k = bytes(m, encoding='ascii')
        for user_agent_format in valid_user_agent_header_formats:
            # lower(k)
            shift(k, k.itemsize, k.shape[0], 45, 95)
            # print(<bytes>k))
            if bytes(k) == user_agent_format:
                return v
    return None


cpdef str find_user_agent_10k(headers):
    cdef int i
    cdef str res = None
    for i in range(1, 10000):
        res = find_user_agent_header(headers)
    return res


def calculate_total():
    cdef int total = 0
    cdef int i, j
    for i in range(1, 10000):
        for j in range(1, 10000):
            total += i + j
    return total



cdef int shift(unsigned char[:] data, int itemsize, int shape, int replace_from, int replace_to):
    cdef int i
    cdef int num
    # cdef int loc
    # for i in range(shape * itemsize):
    for i in range(itemsize):
        num = data[i]
        # print(num)
        if num == replace_from:
            data[i] = replace_to
        num = data[i]
        if 65 <= num <= 90:
            data[i] +=32

# cdef lower(unsigned char[:] inp):
#     # cdef char *inp
#     # inp = arr.data
#     shift(inp, inp.itemsize, inp.shape[0], 45, 95)
#     #return 0

# std::transform(data.begin(), data.end(), data.begin(),
#     [](unsigned char c){ return std::tolower(c); });
