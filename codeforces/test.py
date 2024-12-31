import sys


def res(word):
    return word if len(word) <= 10 else word[0] + str(len(word)-2) + word[-1]


def main():
    # Reading input
    n = int(sys.stdin.readline().strip())
    words = [sys.stdin.readline().strip() for _ in range(n)]

    # Processing each word
    results = [res(word) for word in words]

    # Writing output
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
