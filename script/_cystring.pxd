from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map

cdef extern from "cystring.h" namespace "cystring":
    char* cfind_user_agent_header(unordered_map[char*, char*] &headers);
