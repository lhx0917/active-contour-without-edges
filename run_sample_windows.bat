@echo off
setlocal

if not exist .venv (
    py -3 -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python generate_sample_image.py
python active_contour_without_edges.py --image sample.bmp --output-dir results --iterations 20 --save-every 2

echo.
echo Finished. Open the results folder to view final_contour.png and iteration images.
pause
