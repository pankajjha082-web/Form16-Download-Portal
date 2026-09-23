from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# ==========================

# CONFIGURATION

# ==========================

BASE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Form16"
)

YEAR = "2026-27"

# ==========================

# HOME PAGE

# ==========================

@app.route('/')
def home():
    return render_template('index.html')

# ==========================

# SEARCH PAN

# ==========================

@app.route('/search', methods=['POST'])
def search():
    pan = request.form.get('pan', '').strip().upper()

    if not pan:
        return render_template(
            'not_found.html',
            pan='INVALID PAN'
        )

    files = []

    part_a_path = os.path.join(
        BASE_DIR,
        "PATT A",
        f"{pan}_{YEAR}.pdf"
    )

    part_b_path = os.path.join(
        BASE_DIR,
        "PART B",
        f"{pan}_PARTB_{YEAR}.pdf"
    )

    if os.path.isfile(part_a_path):
        files.append("Part A")

    if os.path.isfile(part_b_path):
        files.append("Part B")

    if files:
        return render_template(
            'results.html',
            pan=pan,
            files=files
        )

    return render_template(
        'not_found.html',
        pan=pan
    )

# ==========================

# DOWNLOAD FILE

# ==========================

@app.route('/download/<part>/<pan>')
def download(part, pan):
    pan = pan.strip().upper()
    if part == "Part A":
        pdf_path = os.path.join(
            BASE_DIR,
            "PATT A",
            f"{pan}_{YEAR}.pdf"
        )

    elif part == "Part B":
        pdf_path = os.path.join(
            BASE_DIR,
            "PART B",
            f"{pan}_PARTB_{YEAR}.pdf"
        )

    else:
        return "Invalid Document Type"

    if not os.path.isfile(pdf_path):
        return f"File not found for PAN: {pan}"

    return send_file(
        pdf_path,
        as_attachment=True
    )

# ==========================

# ERROR HANDLERS

# ==========================

@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        'not_found.html',
        pan='PAGE NOT FOUND'
    ), 404

@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error", 500

# ==========================

# RUN APP

# ==========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
