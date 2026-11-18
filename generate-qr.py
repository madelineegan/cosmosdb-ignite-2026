#!/usr/bin/env python3
import argparse
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a high-resolution QR code for a public URL.")
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=24, border=5)
    qr.add_data(args.url)
    qr.make(fit=True)
    image = qr.make_image(fill_color="#000000", back_color="#ffffff")
    image.save(output)
    print(f"Created {output} -> {args.url}")


if __name__ == "__main__":
    main()
