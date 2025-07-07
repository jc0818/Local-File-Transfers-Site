from flask import Flask, request, send_from_directory, render_template_string
import os
from urllib.parse import quote

#Develop By jc0818

UPLOAD_FOLDER = os.path.abspath('./shared')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_PAGE = '''
<!doctype html>
<html style="margin:0; padding:0; height:100%; overflow:hidden;">
<head>
<title>🟢 F1L3 S3RV3R 🟢</title>
<style>
body {
    background-color: black;
    color: lime;
    font-family: monospace;
    margin: 0;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    position: relative;
}

#binaryBackground {
    position: fixed;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    color: lime;
    opacity: 0.2;
    font-size: 14px;
    z-index: 0;
    white-space: pre;
    pointer-events: none;
}

#mainContent {
    z-index: 1;
    text-align: center;
}

a {
    color: lime;
    text-decoration: none;
}
</style>
</head>
<body>
<pre id="binaryBackground"></pre>

<div id="mainContent">
    <h1>🟢 F1L3 S3RV3R 🟢</h1>

    <h2>File Upload</h2>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>

    <h2>File List</h2>
    <ul style="list-style:none; padding:0;">
    {% for filename in files %}
      <li><a href="/download/{{ filename | urlencode }}">{{ filename }}</a></li>
    {% endfor %}
    </ul>
</div>

<script>
function generateBinary(rows, cols) {
    let str = '';
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            str += Math.random() > 0.5 ? '1' : '0';
        }
        str += '\\n';
    }
    return str;
}

function updateBackground() {
    const bg = document.getElementById('binaryBackground');
    const rows = Math.floor(window.innerHeight / 14);
    const cols = Math.floor(window.innerWidth / 9);
    bg.textContent = generateBinary(rows, cols);
}

setInterval(updateBackground, 200);
window.addEventListener('resize', updateBackground);
updateBackground();
</script>

</body>
</html>
'''

@app.template_filter('urlencode')
def urlencode_filter(s):
    return quote(s)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(save_path)
            print(f"File Save Success: {save_path}")
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(HTML_PAGE, files=files)

@app.route('/download/<path:filename>')
def download(filename):
    print(f"Download Request: {filename}")
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    print(f"Share Folder Address: {UPLOAD_FOLDER}")
    app.run(host='0.0.0.0', port=5000)
