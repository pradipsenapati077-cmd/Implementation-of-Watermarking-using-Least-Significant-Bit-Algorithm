# Implementation-of-Watermarking-using-Least-Significant-Bit-Algorithm
A simple yet effective Python project demonstrating LSB-based image steganography using color (RGB) images.
This script embeds the Most Significant Bits (MSB) of a watermark image into the Least Significant Bits (LSB) of a cover image and allows extraction later.

🚀 Features

✅ Works on color RGB images
✅ Fully automated watermark size adjustment
✅ Simple LSB embedding algorithm
✅ Extracts watermark from the watermarked image
✅ Outputs watermarked and extracted images

📸 Input / Output Overview
📥 Inputs
File	Description
bird1.png	Watermark image
bird2.png	Cover image
📤 Outputs
File	Description
bird2_watermark.png	Watermarked output image
bird2_extracted_watermark.png	Extracted watermark

🧠 How the Algorithm Works
✅ Embedding

Load both cover and watermark images

Resize watermark to match cover (if needed)

Convert both images into NumPy arrays

Extract the MSB from watermark pixels

Replace the LSB of cover pixels with watermark bits

Save the generated watermarked image

✅ Extraction

Load the watermarked image

Extract the LSB from each pixel

Multiply extracted bits by 255 (for visibility)

Save as extracted watermark image

📂 Project Structure
lsb-color-watermarking/
│
├── colorimage.py
├── bird1.png
├── bird2.png
├── bird2_watermark.png
└── bird2_extracted_watermark.png
