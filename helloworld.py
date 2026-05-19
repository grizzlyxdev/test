#!/usr/bin/env python3
import argparse
import os
import sys
import time

def greet(name: str, times: int = 1, delay: float = 0.0, shout: bool = False, message: str = "Hello") -> None:
    """Print a greeting `times` times with optional delay and custom message.

    Args:
        name: Name to greet.
        times: Number of repetitions.
        delay: Seconds to wait between each greeting.
        shout: Convert greeting to uppercase if True.
        message: Custom greeting word (default "Hello").
    """
    for _ in range(times):
        greeting = f"{message}, {name}!"
        if shout:
            greeting = greeting.upper()
        print(greeting)
        if delay > 0:
            time.sleep(delay)

def main() -> None:
    parser = argparse.ArgumentParser(description="Print a greeting with optional repetitions, delay, and custom message.")
    parser.add_argument("-n", "--name", default=os.getenv("GREETING_NAME", "World"),
                        help="Name to greet (default: env GREETING_NAME or 'World')")
    parser.add_argument("-r", "--repeat", type=int, default=1,
                        help="How many times to repeat the greeting (default: 1)")
    parser.add_argument("-d", "--delay", type=float, default=0.0,
                        help="Delay in seconds between greetings (default: 0)")
    parser.add_argument("-m", "--message", default="Hello",
                        help="Custom greeting word (default: 'Hello')")
    parser.add_argument("--shout", action="store_true",
                        help="Convert greeting to uppercase")
    parser.add_argument("-v", "--version", action="store_true",
                        help="Show script version and exit")
    args = parser.parse_args()

    if args.version:
        print("helloworld.py version 2.0")
        sys.exit(0)

    greet(name=args.name, times=args.repeat, delay=args.delay, shout=args.shout, message=args.message)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
