import pyqrcode
import io
import base64
import json
import argparse

def qr_generator(text_input):

    # # Create a QR code from the text
    # qr = pyqrcode.QRCode(
    #     version=1,
    #     box_size=10,
    #     border=4,
    # )

    # Create a QR code from the text
    qr = pyqrcode.create(text_input)

    # Save the QR code to a BytesIO object
    bytes_io = io.BytesIO()
    qr.png(bytes_io, scale=16)

    # Get the byte data from the BytesIO object
    img_bytes = bytes_io.getvalue()


    # Encode the bytes to a base64 string
    img_str = base64.b64encode(img_bytes).decode('utf-8')

    # Return the base64 string in the response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'qr_code': img_str
        }),
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a QR code from text.')
    parser.add_argument('text_input', type=str, help='The text to encode into a QR code.')

    args = parser.parse_args()

    print(qr_generator(args.text_input))