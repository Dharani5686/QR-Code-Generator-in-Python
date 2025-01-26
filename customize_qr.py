import qrcode
from PIL import Image

# Create the basic QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the grid
    border=4,  # thickness of the border
)

# Add data to the QR code
qr.add_data("https://github.com/Dharani5686")
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')
img.save("Dharani's_Github_profile.png")