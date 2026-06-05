from pathlib import Path

import cv2
import numpy as np


def main():
    output_path = Path("sample.bmp")

    image = np.full((160, 160, 3), 220, dtype=np.uint8)
    cv2.circle(image, (82, 82), 42, (60, 60, 60), thickness=-1)
    cv2.rectangle(image, (12, 12), (148, 148), (235, 235, 235), thickness=2)
    cv2.GaussianBlur(image, (3, 3), 0, dst=image)

    cv2.imwrite(str(output_path), image)
    print(f"Created {output_path.resolve()}")


if __name__ == "__main__":
    main()
