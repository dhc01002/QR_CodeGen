import pyqrcode
import io
import base64
import json

def lambda_handler(event):
    # Extract the text from the event object
    #text = event['text']
    text_input =event.get("key")

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