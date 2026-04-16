import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)

    if not match:
        return False

    for part in match.groups():
        # reject leading zeros (except single "0")
        if len(part) > 1 and part.startswith("0"):
            return False

        # range check
        if not 0 <= int(part) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
