import argparse

def greet(name: str, times: int):
    for _ in range(times):
        print(f"Hello, {name}!")

def main():
    parser = argparse.ArgumentParser(description="Print a greeting multiple times.")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    parser.add_argument("--times", type=int, default=1, help="Number of times to greet")
    args = parser.parse_args()
    greet(args.name, args.times)

if __name__ == "__main__":
    main()
