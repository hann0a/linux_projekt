import sys
import numpy as np
from PIL import Image


def is_overexposed(image, threshold=100, max_ratio=0.1):
    gray = image.convert('L')
    pixels = np.array(gray).flatten()
    bright_pixels = np.sum(pixels >= threshold)
    ratio = bright_pixels / len(pixels)
    return ratio > max_ratio


def is_underexposed(image, threshold=50, max_ratio=0.1):
    gray = image.convert('L')
    pixels = np.array(gray).flatten()
    dark_pixels = np.sum(pixels <= threshold)
    ratio = dark_pixels / len(pixels)
    return ratio > max_ratio


if __name__ == "__main__":
    image_path = sys.argv[1]
    over_threshold = int(sys.argv[2])
    under_threshold = int(sys.argv[3])

    image = Image.open(image_path)

    if is_overexposed(image, threshold=over_threshold) or is_underexposed(image, threshold=under_threshold):
        print("False")
        sys.exit(0)
    else:
        print("True")
        sys.exit(0)