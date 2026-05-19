import sys

def main():
    """Print a greeting. Optionally accepts a name as a command‑line argument."""
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    else:
        name = "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
