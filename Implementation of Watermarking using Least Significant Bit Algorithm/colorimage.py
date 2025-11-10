from PIL import Image
import numpy as np

# Step 1: Load cover and watermark images as RGB (color)
cover = Image.open('bird2.png').convert('RGB')
watermark = Image.open('bird1.png').convert('RGB')

# Step 2: Resize watermark to match cover size if needed
if watermark.size != cover.size:
    watermark = watermark.resize(cover.size)

# Step 3: Convert images to NumPy arrays
cover_array = np.array(cover)
watermark_array = np.array(watermark)

# Step 4: Flatten arrays for per-pixel/channel processing
cover_flat = cover_array.flatten()
watermark_flat = watermark_array.flatten()

# Step 5: Create watermark bits (use the MSB for each channel for visibility)
watermark_bits = (watermark_flat >> 7) & 1  # MSB (Most significant bit) per channel

# Step 6: Embed watermark bits into the LSB of each color channel of cover image
embedded_flat = (cover_flat & 0xFE) | watermark_bits  # 0xFE = 11111110

# Step 7: Reshape and save the watermarked image
embedded_array = embedded_flat.reshape(cover_array.shape)
watermarked_img = Image.fromarray(embedded_array.astype(np.uint8))
watermarked_img.save('bird2_watermark.png')
print("Watermark embedding done: bird2_watermark.png")

# -------- Extraction Process --------

# Step 8: Load watermarked image
extracted_img = Image.open('bird2_watermark.png').convert('RGB')
extracted_flat = np.array(extracted_img).flatten()

# Step 9: Extract LSBs to reconstruct watermark image
extracted_bits = extracted_flat & 1
extracted_pixels = (extracted_bits * 255).astype(np.uint8)

# Step 10: Reshape and save the extracted watermark image (RGB)
extracted_array = extracted_pixels.reshape(cover_array.shape)
extracted_watermark = Image.fromarray(extracted_array)
extracted_watermark.save('bird2_extracted_watermark.png')
print("Extraction done: bird2_extracted_watermark.png")
