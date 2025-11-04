#!/usr/bin/env python
"""
Simple QR-code generator.
- Asks for text/URL and a filename
- Saves a black-on-white PNG
- Opens the image (Windows/macOS/Linux)
"""

import qrcode
from pathlib import Path
import sys
import os
from PIL import Image   # Pillow provides the PIL namespace

def main():
    # ------------------------------------------------------------------ #
    # 1. Get user input
    # ------------------------------------------------------------------ #
    data = input("Enter the text or URL: ").strip()
    if not data:
        print("Error: No data entered.")
        sys.exit(1)

    filename_input = input("Enter the filename (without extension): ").strip()
    if not filename_input:
        filename_input = "qr_code"

    # Force .png extension
    filename = Path(filename_input).with_suffix(".png")
    print(f"Will save to: {filename}")

    # ------------------------------------------------------------------ #
    # 2. Build the QR code
    # ------------------------------------------------------------------ #
    qr = qrcode.QRCode(
        version=None,          # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)          # fit=True makes the QR as small as possible

    # Pillow-based image (black on white)
    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # ------------------------------------------------------------------ #
    # 3. Save & show
    # ------------------------------------------------------------------ #
    img.save(filename)
    print(f"QR code saved as {filename}")

    # Optional: open the image automatically
    try:
        if sys.platform.startswith("darwin"):          # macOS
            os.system(f"open {filename}")
        elif sys.platform.startswith("win"):           # Windows
            os.startfile(filename)                     # type: ignore
        elif sys.platform.startswith("linux"):         # Linux
            os.system(f"xdg-open {filename}")
    except Exception as e:
        print(f"Could not open image automatically: {e}")

if __name__ == "__main__":
    main()