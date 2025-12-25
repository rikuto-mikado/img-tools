# img-tools

A simple CLI tool for resizing images.

## Overview

This tool resizes images in a directory while maintaining aspect ratio. It supports JPG, PNG, and WebP formats.

## Usage

```bash
python app.py <input_dir> <output_dir> [--width WIDTH]
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `input_dir` | Directory containing images | Required |
| `output_dir` | Directory for resized images | Required |
| `--width` | Target width in pixels | 800 |

### Example

```bash
python app.py ./input ./output --width 1024
```

## Installation

```bash
pip install -r requirements.txt
```

## License

See [LICENSE](LICENSE) file.
