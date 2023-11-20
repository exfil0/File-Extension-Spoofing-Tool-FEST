import argparse
from pathlib import Path
import sys

def is_valid_file(file_path):
    """Check if the file exists."""
    return file_path.is_file()

def get_spoofed_filename(original_path, extension):
    """Create a spoofed filename with a given extension."""
    spoofer = '\u202e'  # Unicode code for left-to-right override
    original_name = original_path.stem
    original_ext = original_path.suffix
    return f"{original_name}{extension[::-1]}{original_ext}{spoofer}"

def create_spoofed_file(original_path, spoofed_name):
    """Create a spoofed file."""
    with open(original_path, "rb") as source_file:
        with open(spoofed_name, "wb") as spoofed_file:
            spoofed_file.write(source_file.read())

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="File Extension Spoofing Tool")
    parser.add_argument("path", help="Path to the file")
    parser.add_argument("extension", help="Extension to spoof")
    return parser.parse_args()

def main():
    args = parse_args()

    path = Path(args.path)
    if not is_valid_file(path):
        print("[X] Invalid file path or file does not exist!")
        sys.exit(1)

    if len(args.extension) > 5 or args.extension.isdigit():
        print("[X] Please enter a valid extension!")
        sys.exit(1)

    spoofed_name = get_spoofed_filename(path, args.extension)
    create_spoofed_file(path, spoofed_name)

    print(f"[V] Extension spoofed with success. Spoofed file: {spoofed_name}")

if __name__ == "__main__":
    main()
