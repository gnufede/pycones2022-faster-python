import time
from cyscript import find_user_agent_10k, calculate_total


HEADERS = {
    "0IP-IP-II-P-PI-PIP": "10.0.0.1",
    "1-M-IM-IMMI-IMI-MIP": "10.0.0.1",
    "2A-IA-IA-AI-IA-I-A-I-P": "10.0.0.1",
    "2B-IB-IB-BI-IB-I-B-I-P": "10.0.0.1",
    "0C-IC-IC-CI-IC-I-C-I-P": "10.0.0.1",
    "1V-IV-IV-VI-IV-I-V-I-P": "10.0.0.1",
    "2A-MA-MA-AM-MA-M-A-M-IP": "10.0.0.1",
    "2A-AA-AA-AA-AA-A-A-A-IP": "10.0.0.1",
    "0A-BA-BA-AB-BA-B-A-B-IP": "10.0.0.1",
    "1A-CA-CA-AC-CA-C-A-C-IP": "10.0.0.1",
    "2A-VA-VA-AV-VA-V-A-V-IP": "10.0.0.1",
    "2I-PI-PI-IP-PI-P-I-P-": "10.0.0.1",
    "0M-IM-IM-MI-IM-I-M-I-P": "10.0.0.1",
    "1A-IA-IA-AI-IA-I-A-I-P": "10.0.0.1",
    "2B-IB-IB-BI-IB-I-B-I-P": "10.0.0.1",
    "2C-IC-IC-CI-IC-I-C-I-P": "10.0.0.1",
    "VI-0V-IV-VI-IV-I-V-I-P": "10.0.0.1",
    "0A-1M-AM-AA-MM-A-M-A-MIP": "10.0.0.1",
    "1A-2A-AA-AA-AA-A-A-A-AIP": "10.0.0.1",
    "2A-2B-AB-AA-BB-A-B-A-BIP": "10.0.0.1",
    "2A-0C-AC-AA-CC-A-C-A-CIP": "10.0.0.1",
    "AV-1A-VA-AV-VA-V-A-V-IP": "10.0.0.1",
    "IP-2I-PI-IP-PI-P-I-P-": "10.0.0.1",
    "MI-2M-0I-MM-II-M-I-M-IP": "10.0.0.1",
    "AI-AI-1A-AI-IA-I-A-I-P": "10.0.0.1",
    "BI-BI-2B-BI-IB-I-B-I-P": "10.0.0.1",
    "CI-0C-I2-CC-II-C-I-C-IP": "10.0.0.1",
    "VI-1V-IV-VI-IV-I-V-I-P": "10.0.0.1",
    "AM-2A-MA-AM-MA-M-A-M-IP": "10.0.0.1",
    b"Http-Request-User-Agent": "Firefox",
}


start_time = time.time()
total = calculate_total()
print(f"The result is {total}")
end_time = time.time()

print(f"It took {end_time-start_time:.2f} seconds to compute the first part")


start_time = time.time()
x = find_user_agent_10k(HEADERS)
print(f"found the header: {x}")

end_time = time.time()

print(f"It took {end_time-start_time:.2f} seconds to compute the second part")
