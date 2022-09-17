
from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map

cdef extern from "cystring.h" namespace "cystring":
    # string find_user_agent_10k(unordered_map[string, string] &headers);
    # string find_user_agent_header(unordered_map[string, string] &headers);
    char* cfind_user_agent_header(unordered_map[char*, char*] &headers);
