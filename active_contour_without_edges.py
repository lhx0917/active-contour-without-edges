import argparse
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def initialize_level_set(shape, rectangle):
    """Create the initial level set function used by the Chan-Vese iteration."""
    height, width = shape
    y1, x1, y2, x2 = rectangle

    y1 = max(0, min(height, y1))
    y2 = max(0, min(height, y2))
    x1 = max(0, min(width, x1))
    x2 = max(0, min(width, x2))

    if y1 >= y2 or x1 >= x2:
        raise ValueError(
            "Invalid initial rectangle. Use values in the order y1 x1 y2 x2, "
            "and make sure y1 < y2 and x1 < x2."
        )

    level_set = np.ones((height, width), dtype=np.float64)
    level_set[y1:y2, x1:x2] = -1.0
    return -level_set


def chan_vese_step(level_set, image_gray, mu, nu, epsilon, step):
    drac = (epsilon / np.pi) / (epsilon * epsilon + level_set * level_set)
    heaviside = 0.5 * (1.0 + (2.0 / np.pi) * np.arctan(level_set / epsilon))

    gradient_y, gradient_x = np.gradient(level_set)
    gradient_norm = np.sqrt(gradient_x * gradient_x + gradient_y * gradient_y)
    normal_x = gradient_x / (gradient_norm + 1e-6)
    normal_y = gradient_y / (gradient_norm + 1e-6)

    normal_xx, _ = np.gradient(normal_x)
    _, normal_yy = np.gradient(normal_y)
    curvature = normal_xx + normal_yy

    length_term = nu * drac * curvature
    laplacian = cv2.Laplacian(level_set, cv2.CV_64F)
    penalty_term = mu * (laplacian - curvature)

    inside_weighted = heaviside * image_gray
    outside_weighted = (1.0 - heaviside) * image_gray
    outside_mask = 1.0 - heaviside

    c1 = inside_weighted.sum() / (heaviside.sum() + 1e-10)
    c2 = outside_weighted.sum() / (outside_mask.sum() + 1e-10)

    cv_term = drac * (
        -1.0 * (image_gray - c1) * (image_gray - c1)
        + (image_gray - c2) * (image_gray - c2)
    )

    return level_set + step * (length_term + penalty_term + cv_term)


def draw_contour(image_rgb, level_set, title, output_path):
    plt.figure(figsize=(6, 6))
    plt.imshow(image_rgb)
    plt.xticks([])
    plt.yticks([])
    plt.contour(level_set, [0], colors="r", linewidths=2)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def run_segmentation(
    image_path,
    output_dir,
    init_rect,
    mu,
    nu,
    iterations,
    epsilon,
    step,
    save_every,
    display,
):
    image_path = Path(image_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    image_bgr = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image_bgr is None:
        raise FileNotFoundError(f"Could not read image file: {image_path}")

    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY).astype(np.float64)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    level_set = initialize_level_set(image_gray.shape, init_rect)

    saved_paths = []
    for i in range(1, iterations + 1):
        level_set = chan_vese_step(level_set, image_gray, mu, nu, epsilon, step)

        if i % save_every == 0 or i == iterations:
            output_path = output_dir / f"iteration_{i:03d}.png"
            draw_contour(image_rgb, level_set, f"Iteration: {i}", output_path)
            saved_paths.append(output_path)
            print(f"Saved {output_path}")

            if display:
                preview = cv2.imread(str(output_path), cv2.IMREAD_COLOR)
                cv2.imshow("Active Contour Without Edges", preview)
                cv2.waitKey(1)

    final_path = output_dir / "final_contour.png"
    draw_contour(image_rgb, level_set, f"Final contour after {iterations} iterations", final_path)
    print(f"Saved {final_path}")

    if display:
        preview = cv2.imread(str(final_path), cv2.IMREAD_COLOR)
        cv2.imshow("Active Contour Without Edges", preview)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return final_path, saved_paths


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Chan-Vese active contour without edges on a local image."
    )
    parser.add_argument("--image", required=True, help="Path to the input image, such as sample.bmp.")
    parser.add_argument("--output-dir", default="results", help="Directory for generated contour images.")
    parser.add_argument(
        "--init-rect",
        nargs=4,
        type=int,
        default=[30, 30, 80, 80],
        metavar=("Y1", "X1", "Y2", "X2"),
        help="Initial rectangle in pixel coordinates. Default: 30 30 80 80.",
    )
    parser.add_argument("--mu", type=float, default=1.0, help="Penalty coefficient. Default: 1.0.")
    parser.add_argument(
        "--nu",
        type=float,
        default=0.003 * 255 * 255,
        help="Length coefficient. Default: 0.003 * 255 * 255.",
    )
    parser.add_argument("--iterations", type=int, default=20, help="Number of iterations. Default: 20.")
    parser.add_argument("--epsilon", type=float, default=1.0, help="Regularized delta width. Default: 1.0.")
    parser.add_argument("--step", type=float, default=0.1, help="Iteration step size. Default: 0.1.")
    parser.add_argument("--save-every", type=int, default=2, help="Save an image every N iterations. Default: 2.")
    parser.add_argument("--display", action="store_true", help="Show OpenCV preview windows while running.")
    return parser.parse_args()


def main():
    args = parse_args()
    run_segmentation(
        image_path=args.image,
        output_dir=args.output_dir,
        init_rect=args.init_rect,
        mu=args.mu,
        nu=args.nu,
        iterations=args.iterations,
        epsilon=args.epsilon,
        step=args.step,
        save_every=max(1, args.save_every),
        display=args.display,
    )


if __name__ == "__main__":
    main()
