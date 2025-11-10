from PIL import Image
import numpy as np

# Step 1: Load cover and watermark images as RGB (color)
cover = Image.open('bird1.png').convert('RGB')
watermark = Image.open('bird2.png').convert('RGB')

# Step 2: Resize watermark to match cover size if needed
if watermark.size != cover.size:
    watermark = watermark.resize(cover.size)

# Step 3: Convert images to NumPy arrays
cover_array = np.array(cover)
watermark_array = np.array(watermark)

# Step 4: Flatten arrays for per-pixel/channel processing
cover_flat = cover_array.flatten()
watermark_flat = watermark_array.flatten()

# Step 5: Prepare the watermark bits (take the 4 MSBs from each watermark pixel value)
watermark_bits_4 = (watermark_flat >> 4) & 0x0F   # Grab the upper 4 bits

# Step 6: Embed the 4 watermark bits into the 4 LSBs of cover image
embedded_flat = (cover_flat & 0xF0) | watermark_bits_4    # 0xF0 = 11110000, 0x0F = 00001111

# Step 7: Reshape and save the watermarked image
embedded_array = embedded_flat.reshape(cover_array.shape)
watermarked_img = Image.fromarray(embedded_array.astype(np.uint8))
watermarked_img.save('bird_4bit.png')
print("Watermark embedding done: bird_4bit.png")

# -------- Extraction Process --------

# Step 8: Load watermarked image
extracted_img = Image.open('bird_4bit.png').convert('RGB')
extracted_flat = np.array(extracted_img).flatten()

# Step 9: Extract the 4 LSBs to reconstruct the 4 MSBs of the watermark image
extracted_bits_4 = extracted_flat & 0x0F
extracted_pixels = (extracted_bits_4 << 4).astype(np.uint8)  # Shift back to MSB positions

# Step 10: Reshape and save the extracted watermark image
extracted_array = extracted_pixels.reshape(cover_array.shape)
extracted_watermark = Image.fromarray(extracted_array)
extracted_watermark.save('extracted_bird_4bit.png')
print("Extraction done: extracted_bird_4bit.png")
