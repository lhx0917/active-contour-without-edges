# Active Contour Without Edges

This repository provides a Windows-ready Python script for Chan-Vese active contour segmentation.

## Included Files

| File | Description |
| --- | --- |
| `active_contour_without_edges.py` | Main script for running active contour segmentation on an input image. |
| `requirements.txt` | Python dependencies required by the script. |
| `readMe.md` | Setup and usage instructions. |

## Virtual Environment Requirements

Use Python 3.9 or newer on Windows.


Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## How To Run

Prepare an input image first. The script supports common OpenCV-readable image formats such as `.bmp`, `.png`, `.jpg`, `.jpeg`, `.tif`, and `.tiff`.

Run segmentation:

```powershell
python active_contour_without_edges.py --image "C:\path\to\your\image.bmp" --output-dir results
```

Example if the image is in the project folder:

```powershell
python active_contour_without_edges.py --image 1.bmp --output-dir results
```

Useful optional arguments:

```powershell
python active_contour_without_edges.py --image 1.bmp --output-dir results --iterations 80 --save-every 1
```

Show OpenCV preview windows while running:

```powershell
python active_contour_without_edges.py --image 1.bmp --output-dir results --display
```

The final result is saved as:

```text
results\final_contour.png
```

Intermediate contour images are saved according to `--save-every`, for example:

```text
results\iteration_002.png
results\iteration_004.png
```
