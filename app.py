import argparse
from pathlib import Path
from PIL import Image


SUPPORTED_FORMATS = {"jpg", "jpeg", "png", "webp"}


# Function to find images in a directory
def find_image(input_dir: Path):
    for img_path in input_dir.rglob("*"):
        if img_path.suffix.lower() in SUPPORTED_FORMATS:
            yield img_path

def resize_image(inDir: Path, outDir: Path, width: int):
    pass


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Simple CLI Tool: just list images and their paths"
    )

    # Add input
    parser.add_argument(
        "input_dir", type=str, help="Path to the input directory(containing images)"
    )

    # Add output
    parser.add_argument("output_dir", type=str, help="Path to the output directory")

    # Parse arguments
    parser.add_argument(
        "--width", type=int, default=800, help="Width of the out put image"
    )

    # Parse the arguments
    args = parser.parse_args()
    inDir = Path(args.input_dir)
    outDir = Path(args.output_dir)

    # Check if input directory exists
    if not inDir.exists() or not inDir.is_dir():
        print(f"Error: There is no such directory: {inDir}")
        return

    print("=== imgtool-cli ===")
    print(f"Input Directory: {inDir}")
    print(f"Output Directory: {outDir}")
    print(f"Width: {args.width}")
    print("\n--- List of images to process ---")

    found = False

    for img_path in find_image(inDir):
        rel = img_path.relative_to(inDir)
        out_path = outDir / rel

        print(f"{img_path} -> {out_path}")
        found = True

    if not found:
        print("No images found in the specified directory")


if __name__ == "__main__":
    main()
