from flask import Flask, request, send_file
from PIL import Image, ImageDraw
import io

app = Flask(__name__)

@app.route('/generate')
def generate_image():
    img = Image.new('RGB', (200, 100), color='skyblue')
    d = ImageDraw.Draw(img)
    d.text((10, 40), "Hello Aqua!", fill='black')
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)



























































