from PIL import Image
import pyheif

def openHEIC(img):
    heif_file = pyheif.read(img)
    image = Image.frombytes(
        heif_file.mode, heif_file.size,
        heif_file.data, "raw",
        heif_file.mode, heif_file.stride)

    return image
