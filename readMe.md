# Active Contour Without Edges

## Included Files

This repository contains all files needed to run the project:

| File | Description |
| --- | --- |
| `active_contour_without_edges.py` | Main Python script for running Chan-Vese active contour segmentation. |
| `generate_sample_image.py` | Generates a simple `sample.bmp` test image. |
| `requirements.txt` | Python package dependencies. |
| `run_sample_windows.bat` | Windows batch script for automatic setup and sample execution. |
| `readMe.md` | Project usage instructions. |

## Virtual Environment Requirements

Use Python 3.9 or newer on Windows.

Create a virtual environment:

```powershell
py -3 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## How To Run

### Option 1: Run the Windows Batch File

Double-click:

```text
run_sample_windows.bat
```

Or run it from PowerShell:

```powershell
.\run_sample_windows.bat
```

This creates the virtual environment if needed, installs dependencies, generates `sample.bmp`, runs the segmentation, and saves results in:

```text
results
```

### Option 2: Run Commands Manually

Generate a sample image:

```powershell
python generate_sample_image.py
```

Run segmentation on the sample image:

```powershell
python active_contour_without_edges.py --image sample.bmp --output-dir results
```

Run segmentation on your own image:

```powershell
python active_contour_without_edges.py --image "C:\path\to\your\image.bmp" --output-dir results
```

Useful optional arguments:

```powershell
python active_contour_without_edges.py --image sample.bmp --output-dir results --iterations 80 --save-every 1
```

To show OpenCV preview windows while running:

```powershell
python active_contour_without_edges.py --image sample.bmp --output-dir results --display
```

The final output image is saved as:

```text
results\final_contour.png
```
