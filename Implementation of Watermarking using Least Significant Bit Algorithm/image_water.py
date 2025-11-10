from PIL import Image
import numpy as np

# Load the cover image
cover = Image.open('coverimage.png').convert('L')  # 'L' mode for grayscale
# Load the watermark image
watermark = Image.open('water2.png').convert('L')

if watermark.size != cover.size:
    watermark = watermark.resize(cover.size)


cover_array = np.array(cover)
watermark_array = np.array(watermark)

cover_flat = cover_array.flatten()
watermark_flat = watermark_array.flatten()

watermark_bits = (watermark_flat >> 7) & 1  # Get MSB (0 or 1) per pixel

embedded_flat = (cover_flat & 0xFE) | watermark_bits  # Replace LSB of cover pixel with watermark bit

embedded_array = embedded_flat.reshape(cover_array.shape)
watermarked_image = Image.fromarray(embedded_array.astype(np.uint8))
watermarked_image.save('watermarked_image.png')
print("Embedding done: watermarked_image.png")

# Load watermarked image
wm_img = Image.open('watermarked_image.png').convert('L')
wm_flat = np.array(wm_img).flatten()

# Extract LSBs
extracted_bits = wm_flat & 1
extracted_pixels = (extracted_bits * 255).astype(np.uint8)  # Stretch 0/1 to 0/255 for visibility

# Reshape to image shape and save
extracted_array = extracted_pixels.reshape(cover_array.shape)
extracted_image = Image.fromarray(extracted_array)
extracted_image.save('extracted_watermark.png')
print("Extraction done: extracted_watermark.png")


original = np.array(Image.open('coverimage.png'))
watermarked = np.array(Image.open('watermarked_image.png'))

# MSE function
def mse(img1, img2):
    return np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)

# PSNR function using the standard formula
def psnr(img1, img2):
    mse_value = mse(img1, img2)
    if mse_value == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 10 * np.log10((PIXEL_MAX ** 2) / mse_value)

# Calculate values
mse_value = mse(original, watermarked)
psnr_value = psnr(original, watermarked)

# Print results for easy comparison
print('--- Image Quality Comparison ---')
print(f'MSE between original and watermarked image: {mse_value}')
print(f'PSNR between original and watermarked image: {psnr_value} dB')
