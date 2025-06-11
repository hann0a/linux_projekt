import sys
import numpy as np
from PIL import Image


def find_threshold(image):
    r,g,b = image.split()

    r_data = list(r.getdata())
    g_data = list(g.getdata())
    b_data = list(b.getdata())

    all_pixels = np.array(r_data + g_data + b_data)
    over_threshold = int(np.percentile(all_pixels, 95))
    under_threshold = int(np.percentile(all_pixels, 10))
    

    return over_threshold, under_threshold

if __name__ == "__main__":
    image_path = sys.argv[1]
    image = Image.open(image_path)
    over, under = find_threshold(image)
    print(f"{over} {under}")