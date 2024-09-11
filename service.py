from flask import Flask, render_template, request, send_file, url_for
import os
from flask_bootstrap import Bootstrap5
import qrcode
from io import BytesIO


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

Bootstrap5(app)
url = None
@app.route('/', methods=['GET', 'POST'])
def main():
    url = request.form.get('url')
    img_url = None
    if url != None:
        img = qrcode.make(url)
        type(img)
        img.save("qr.png")
        img_url='/qr-image'
    
    return render_template("qr.html" , img_url=img_url)

@app.route('/qr-image')
def qr_image():
    url = request.args.get('url')
    if url:
        img = qrcode.make(url)
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qr_code.png')
    return '', 404

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)