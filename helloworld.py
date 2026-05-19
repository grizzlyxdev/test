import sys
import argparse

def greet(name: str, upper: bool = False) -> str:
    """Return a greeting string.
    If `upper` is True, the greeting is returned in uppercase.
    """
    greeting = f"Hello, {name}!"
    return greeting.upper() if upper else greeting

def main():
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("name", nargs="*", default=["World"], help="Name(s) to greet")
    parser.add_argument("-r", "--repeat", type=int, default=1, help="Number of times to repeat the greeting")
    parser.add_argument("-u", "--upper", action="store_true", help="Convert greeting to uppercase")
    args = parser.parse_args()
    name = " ".join(args.name)
    for _ in range(args.repeat):
        print(greet(name, args.upper))

if __name__ == "__main__":
    main()
