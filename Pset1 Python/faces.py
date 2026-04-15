def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    print(convert(input()))


if __name__ == "__main__":
    main()

# or just one line
# print(input().replace(":)", "🙂").replace(":(", "🙁"))
