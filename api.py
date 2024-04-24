from flask import Flask, request, jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(_name_)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    # Get image file from request
    image_file = request.files['image']
    # Read image using PIL
    image = Image.open(image_file)
    # Remove background
    output = remove(image)
    # Convert output image to bytes
    img_bytes = io.BytesIO()
    output.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    # Return the output image as a response
    return img_bytes, 200, {'Content-Type': 'image/png'}

if _name_ == '_main_':
    app.run(debug=True)