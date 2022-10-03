#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <unordered_map>

namespace cystring {

inline char manipulate_char(unsigned char c) {
  if (c == '_')
    return '-';
  return std::tolower(c);
}
inline char *cmanipulate_string(const char *data) {
  const int length = strlen(data); // get the length of the text
  char *lower = (char *)malloc(
      length +
      1); // allocate 'length' bytes + 1 (for null terminator) and cast to char*
  lower[length] = 0; // set the last byte to a null terminator

  // copy all character bytes to the new buffer using tolower
  for (int i = 0; i < length; i++) {
    lower[i] = manipulate_char(data[i]);
  }
  return lower;
}

inline void manipulate_string(std::string *data) {
  std::transform(data->begin(), data->end(), data->begin(), manipulate_char);
}
std::string valid_user_agent_formats[5] = {
    "useragent", "user-agent", "http-user-agent", "request-user-agent",
    "http-request-user-agent"};

inline char *
cfind_user_agent_header(const std::unordered_map<char *, char *> &headers) {
  for (const auto &header : headers) {
    for (int i = 0; i < 5; i++) {
      const char *header_string = header.first;
      char *changed_header_string = cmanipulate_string(header_string);
      if (changed_header_string == valid_user_agent_formats[i]) {
        return (char *)header.second;
        // return res;
      }
    }
  }
  return NULL;
}

inline std::string find_user_agent_header(
    const std::unordered_map<std::string, std::string> &headers) {
  for (const auto &header : headers) {
    for (int i = 0; i < 5; i++) {
      std::string header_string = header.first;
      manipulate_string(&(header_string));
      if (header_string == valid_user_agent_formats[i]) {
        return (std::string)header.second;
        // return res;
      }
    }
  }
  return NULL;
}
inline std::string find_user_agent_10k(
    const std::unordered_map<std::string, std::string> &headers) {
  return find_user_agent_header(headers);

  std::string res;
  for (int i = 0; i < 10; i++) {
    res = find_user_agent_header(headers);
    // std::cout << res;
  }
  return res;
}

inline int main() {
  std::string data = "Ab-c";

  std::unordered_map<std::string, std::string> u = {
      {"RED", "#FF0000"}, {"GREEN", "#00FF00"}, {"user_agent", "#0000FF"}};

  manipulate_string(&data);
  std::cout << data;

  std::cout << find_user_agent_10k(u);

  return 0;
}

} // namespace cystring
