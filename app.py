import argparse
from os import path
from pathlib import Path

SUPPORTED_FORMATS = {"jpg", "jpeg", "png", "webp"}


# Function to find images in a directory
def find_image(input_dir: Path):
    for path in input_dir.rglob("*"):
        if path.suffix.lower() in SUPPORTED_FORMATS:
            yield path


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Simple CLI Tool: just list images and their paths"
    )

    parser.add_argument(
        "input_dir", type=str, help="Path to the input directory(containing images)"
    )
