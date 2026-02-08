# regex_hunting.py
import re
from datetime import datetime


# datatime for log timestamps and potential time-based regex patterns


# ==============================
# Malware signatures (hex)
# ==============================


def find_hex_signatures(text: str):
    """
    Find hex malware signatures of the form 0x[0-9A-Fa-f]+.
    """
    return re.findall(r"\b0x[a-fA-F0-9]+\b", text)


# b0x[a-fA-F0-9]+b ensures we match whole hex signatures and not parts of larger strings.


# ==============================
# Device ID hunting
# ==============================


def find_r15_devices(devices_str: str):
    """
    Find device IDs that start with 'r15'.
    """
    target_pattern = r"r15\w+"
    return re.findall(target_pattern, devices_str)


# ==============================
# IP address extraction + flagging
# ==============================

IP_PATTERN_ANY = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# regex give pattern for any IP address, even if not valid (e.g. 999.999.999.999 would match)


def extract_ips(log_text: str):
    """
    Extract IP-like patterns of the form xxx.xxx.xxx.xxx.
    """
    return re.findall(IP_PATTERN_ANY, log_text)


# log_text is the string containing the log entries, and the function uses the regex pattern to find all occurrences of IP-like patterns in the text.


def flag_ips(ip_list, flagged_addresses):
    """
    Print whether each IP is flagged, including investigation date/time.
    """
    investigation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for address in ip_list:
        if address in flagged_addresses:
            print(f"🚨 MALICIOUS: {address}")
            print(f"   📅 Investigated at: {investigation_time}")
            print("   ⚠️ Needs further investigation by SOC team\n")
        else:
            print(f"✅ CLEAN: {address}")
            print(f"   📅 Investigated at: {investigation_time}")
            print("   🔍 No further investigation required\n")


# ==============================
# Interactive IP investigation
# ==============================


def interactive_ip_check():
    """
    Ask user to enter IP addresses, then check against known malicious IPs.
    """
    known_malicious_ips = [
        "192.168.190.178",
        "192.168.96.200",
        "192.168.174.117",
        "192.168.168.144",
    ]

    ip_str = input("Enter IP addresses to check (comma-separated): ")
    user_ips = [ip.strip() for ip in ip_str.split(",") if ip.strip()]

    if not user_ips:
        print("No IPs entered.")
        return

    investigation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nIP Analysis Results")
    print("-" * 40)

    for ip in user_ips:
        if ip in known_malicious_ips:
            print(f"🚨 MALICIOUS: {ip}")
            print(f"   📅 Investigated at: {investigation_time}")
            print("   ⚠️ Needs further investigation by SOC team")
            print("   📌 Rule: Investigate failed login attempts if more than 100\n")
        else:
            print(f"✅ CLEAN: {ip}")
            print(f"   📅 Investigated at: {investigation_time}")
            print("   📌 Failed login attempts below threshold (100)\n")


# ==============================
# Main
# ==============================


def main():
    # Demo for hex signatures
    data = "The malware signature is 0x9ACDAB and needs analysis."
    print("Hex signatures:", find_hex_signatures(data))

    # Demo for device IDs
    devices = (
        "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i "
        "r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l "
        "ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q "
        "081qc9t r159r1u"
    )
    print("r15 devices:", find_r15_devices(devices))

    # Demo log file
    log_file = (
        "eraab 2022-05-10 06:03:41 192.168.152.148\n"
        "smartell 2022-05-09 19:30:32 192.168.190.178\n"
        "asundara 2022-05-11 18:38:07 192.168.96.200\n"
        "jclark 2022-05-10 10:48:02 192.168.174.117\n"
        "daquino 2022-05-08 07:02:35 192.168.168.144"
    )

    ips = extract_ips(log_file)
    flagged_addresses = [
        "192.168.190.178",
        "192.168.96.200",
        "192.168.174.117",
        "192.168.168.144",
    ]

    print("\nExtracted IPs:", ips)
    print("\nInvestigation Results:")
    flag_ips(ips, flagged_addresses)

    print("\n" + "=" * 50)
    interactive_ip_check()


if __name__ == "__main__":
    main()
