import pyqrcode

# Data to be encoded in the QR code
data = "https://www.google.com"

# Generate QR code
qr = pyqrcode.create(data)

# Save QR code as a PNG file
qr.png("qrcode.png")

print("QR code generated successfully!")
