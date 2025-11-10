from PIL import Image
import numpy as np

# Load images (ensure both images are the same size and mode)
cover = np.array(Image.open('bird2.png'))
watermarked = np.array(Image.open('bird2_watermark.png'))

# MSE Calculation
def mse(img1, img2):
    return np.mean((img1.astype(np.float64) - img2.astype(np.float64)) ** 2)

mse_value = mse(cover, watermarked)
print("MSE:", mse_value)

# PSNR Calculation
def psnr(img1, img2):
    mse_value = mse(img1, img2)
    if mse_value == 0:
        return float('inf')
    # Assume maximum pixel value is 255 (for 8-bit images)
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse_value))

psnr_value = psnr(cover, watermarked)
print("PSNR:", psnr_value)
