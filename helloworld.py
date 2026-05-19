#!/usr/bin/env python3
import argparse
import os
import sys

def greet(name: str, times: int = 1) -> None:
    """Print a greeting `times` times.

    Args:
        name: Name to greet.
        times: Number of repetitions.
    """
    for _ in range(times):
        print(f"Hello, {name}!")

def main() -> None:
    parser = argparse.ArgumentParser(description="Print a greeting with optional repetitions.")
    parser.add_argument("-n", "--name", default=os.getenv("GREETING_NAME", "World"),
                        help="Name to greet (default: env GREETING_NAME or 'World')")
    parser.add_argument("-r", "--repeat", type=int, default=1,
                        help="How many times to repeat the greeting (default: 1)")
    parser.add_argument("--shout", action="store_true",
                        help="Convert greeting to uppercase")
    args = parser.parse_args()

    name = args.name.upper() if args.shout else args.name
    greet(name, args.repeat)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
