# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-12-26

### Fixed

- Fixed file extension matching issue in `find_image()` function
  - `Path.suffix` returns extensions with a dot (e.g., `.jpg`), now properly stripped before comparison
- Fixed invalid return value in `resize_image()` function
  - Corrected tuple return to `(orig_width, orig_height, width, new_height)`
- Fixed missing resize operation in main loop
  - Images are now actually resized, not just listed
