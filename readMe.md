# Active Contour Without Edges

This project is a Windows-ready Python implementation of the Chan-Vese "active contour without edges" image segmentation method. It was converted from the original Google Colab notebook named `Activate contour without edge.ipynb`.

The program reads an image, initializes a level set function, runs iterative Chan-Vese contour evolution, and saves red contour overlays as PNG files.

## 1. Files Included

The project folder contains all source files needed to run the code:

| File | Purpose |
| --- | --- |
| `active_contour_without_edges.py` | Main executable Python script. Runs the Chan-Vese contour algorithm on an input image. |
| `generate_sample_image.py` | Creates a simple `sample.bmp` image so you can test the program immediately. |
| `requirements.txt` | Python dependencies required for execution. |
| `run_sample_windows.bat` | Windows batch script that creates a virtual environment, installs dependencies, generates a sample image, and runs the algorithm. |
| `readMe.md` | Detailed setup and usage guide. |

## 2. System Requirements

Use a Windows computer with:

1. Windows 10 or Windows 11.
2. Python 3.9 or newer.
3. Internet access for the first dependency installation.
4. A terminal application such as Command Prompt, PowerShell, or Windows Terminal.

Python 3.10 or 3.11 is recommended.

## 3. Install Python on Windows

If Python is already installed, you can skip this section.

1. Open the official Python download page:
   `https://www.python.org/downloads/windows/`
2. Download the latest stable Windows installer.
3. Run the installer.
4. On the first installer screen, enable:
   `Add python.exe to PATH`
5. Click:
   `Install Now`
6. After installation, open PowerShell and check:

```powershell
python --version
```

If `python` is not recognized, try:

```powershell
py --version
```

The commands in this guide use `py -3` for virtual environment creation because it is reliable on Windows.

## 4. Recommended Project Location

Place this folder somewhere easy to access, for example:

```text
C:\Users\<YourUserName>\Documents\ActiveContourWithoutEdges
```

In PowerShell, move into the folder:

```powershell
cd C:\Users\<YourUserName>\Documents\ActiveContourWithoutEdges
```

Replace `<YourUserName>` with your actual Windows username.

## 5. Quick Start Using the Batch File

The easiest way to run the project is to double-click:

```text
run_sample_windows.bat
```

You can also run it from PowerShell:

```powershell
.\run_sample_windows.bat
```

The batch file performs these steps automatically:

1. Creates a Python virtual environment named `.venv`.
2. Activates the virtual environment.
3. Upgrades `pip`.
4. Installs packages from `requirements.txt`.
5. Generates `sample.bmp`.
6. Runs active contour segmentation on `sample.bmp`.
7. Saves output images into the `results` folder.

After it finishes, open:

```text
results\final_contour.png
```

You will also see intermediate files such as:

```text
results\iteration_002.png
results\iteration_004.png
...
results\iteration_020.png
```

## 6. Manual Setup in PowerShell

If you prefer to run each command manually, follow these steps.

### Step 1: Open PowerShell

Open the Start menu, search for `PowerShell`, and start it.

### Step 2: Enter the Project Folder

Example:

```powershell
cd C:\Users\<YourUserName>\Documents\ActiveContourWithoutEdges
```

### Step 3: Create a Virtual Environment

```powershell
py -3 -m venv .venv
```

This creates a local environment folder named `.venv`.

### Step 4: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation with an execution policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

When activation succeeds, your prompt usually begins with:

```text
(.venv)
```

### Step 5: Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The required packages are:

1. `numpy`
2. `opencv-python`
3. `matplotlib`

### Step 6: Generate a Test Image

```powershell
python generate_sample_image.py
```

This creates:

```text
sample.bmp
```

### Step 7: Run the Segmentation

```powershell
python active_contour_without_edges.py --image sample.bmp --output-dir results
```

The output folder will contain the contour visualization images.

## 7. Run on Your Own Image

Copy your image into the project folder. Supported formats include common OpenCV-readable files such as:

1. `.bmp`
2. `.png`
3. `.jpg`
4. `.jpeg`
5. `.tif`
6. `.tiff`

Example command:

```powershell
python active_contour_without_edges.py --image 1.bmp --output-dir results
```

If your image is in another folder, provide the full path:

```powershell
python active_contour_without_edges.py --image "C:\Users\<YourUserName>\Pictures\1.bmp" --output-dir results
```

Use quotation marks when the path contains spaces.

## 8. Command-Line Options

The main script supports these options:

| Option | Default | Meaning |
| --- | --- | --- |
| `--image` | Required | Input image path. |
| `--output-dir` | `results` | Folder where output PNG files are saved. |
| `--init-rect Y1 X1 Y2 X2` | `30 30 80 80` | Initial level set rectangle. Coordinates are row/column style: top, left, bottom, right. |
| `--mu` | `1.0` | Penalty coefficient used in the level set update. |
| `--nu` | `0.003 * 255 * 255` | Contour length coefficient. |
| `--iterations` | `20` | Number of evolution iterations. |
| `--epsilon` | `1.0` | Regularization width for the smoothed Dirac and Heaviside functions. |
| `--step` | `0.1` | Time step for each iteration. |
| `--save-every` | `2` | Save an intermediate visualization every N iterations. |
| `--display` | Disabled | Show OpenCV preview windows while running. |

Example with custom parameters:

```powershell
python active_contour_without_edges.py --image sample.bmp --output-dir results_custom --init-rect 40 40 110 110 --iterations 60 --save-every 5 --step 0.05
```

## 9. Choosing the Initial Rectangle

The initial rectangle controls where the contour starts.

The format is:

```text
--init-rect Y1 X1 Y2 X2
```

For example:

```powershell
python active_contour_without_edges.py --image sample.bmp --init-rect 30 30 80 80
```

This means:

1. Top row: `30`
2. Left column: `30`
3. Bottom row: `80`
4. Right column: `80`

If your target object is larger or located elsewhere, change these values. The rectangle must be inside the image size.

## 10. Output Files

The script saves visual results as PNG images.

Typical output:

```text
results\iteration_002.png
results\iteration_004.png
results\iteration_006.png
...
results\iteration_020.png
results\final_contour.png
```

Each image shows:

1. The original input image.
2. A red contour line where the level set function crosses zero.

## 11. Algorithm Summary

The code implements a level-set based Chan-Vese segmentation model.

The main steps are:

1. Read the input image with OpenCV.
2. Convert the image from BGR to grayscale.
3. Initialize a level set function with a rectangular region.
4. Compute a smoothed Dirac delta function.
5. Compute a smoothed Heaviside function.
6. Estimate the average gray value inside and outside the contour.
7. Compute curvature and regularization terms.
8. Update the level set function.
9. Draw the zero level set as a red contour.
10. Save intermediate and final results.

The implementation preserves the structure of the original Colab notebook while making it easier to run as a reusable Windows command-line program.

## 12. Troubleshooting

### Python is not recognized

Try:

```powershell
py --version
```

If that works, use:

```powershell
py -3 -m venv .venv
```

If neither command works, reinstall Python and enable `Add python.exe to PATH`.

### PowerShell blocks virtual environment activation

Run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### `cv2` import fails

Install dependencies again:

```powershell
python -m pip install -r requirements.txt
```

### Image cannot be read

Check that:

1. The image path is correct.
2. The file extension is supported.
3. The path is wrapped in quotes if it contains spaces.

Example:

```powershell
python active_contour_without_edges.py --image "C:\Users\<YourUserName>\Pictures\my image.bmp"
```

### No useful contour appears

Try these adjustments:

1. Increase iterations:

```powershell
python active_contour_without_edges.py --image sample.bmp --iterations 80
```

2. Change the initial rectangle:

```powershell
python active_contour_without_edges.py --image sample.bmp --init-rect 40 40 120 120
```

3. Reduce step size if the contour changes too aggressively:

```powershell
python active_contour_without_edges.py --image sample.bmp --step 0.05
```

4. Try a cleaner image with stronger contrast between object and background.

## 13. Notes for Windows Paths

Windows paths often contain backslashes. Both of these styles can work:

```powershell
python active_contour_without_edges.py --image "C:\Users\<YourUserName>\Pictures\1.bmp"
```

or:

```powershell
python active_contour_without_edges.py --image C:\Users\<YourUserName>\Pictures\1.bmp
```

Use quotes if there are spaces in the path.

## 14. Clean Up

To remove generated output files, delete the `results` folder.

To remove the Python virtual environment, delete the `.venv` folder.

You can recreate both at any time by running:

```powershell
.\run_sample_windows.bat
```
