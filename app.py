from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from datetime import datetime

app = Flask(__name__)

# Set OG title and description
og_title = "Information Form"
og_description = "Enter Targets Information"

@app.route('/')
def index():
    return render_template('index.html', og_title=og_title, og_description=og_description)

@app.route('/generate_txt', methods=['POST'])
def generate_txt():
    if request.method == 'POST':
        reason = request.form.get('reason', '')
        full_name = request.form.get('fullName', '')
        alias = request.form.get('alias', '')
        dob = request.form.get('dob', '')
        age = request.form.get('age', '')
        phone_number = request.form.get('phoneNumber', '')
        address = request.form.get('address', '')
        state = request.form.get('state', '')
        city = request.form.get('city', '')
        zip_code = request.form.get('zip', '')
        country = request.form.get('country', '')
        other_info = request.form.get('otherInfo', '')

        # Generate file name using full name
        file_name = f"{full_name.replace(' ', '_')}.txt"
        file_path = os.path.join('txts', file_name)

        # Write data to the file
        with open(file_path, 'w') as file:
            file.write(f"Reason: {reason}\n")
            file.write(f"Full Name: {full_name}\n")
            file.write(f"Alias: {alias}\n")
            file.write(f"Date Of Birth: {dob}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Phone Number: {phone_number}\n")  # Phone number above address
            file.write(f"Address: {address}\n")
            file.write(f"State: {state}\n")
            file.write(f"City: {city}\n")
            file.write(f"Zip: {zip_code}\n")
            file.write(f"Country: {country}\n")
            file.write(f"Other Info: {other_info}\n")

        return redirect(url_for('download_txt', file_name=file_name))

@app.route('/download_txt/<file_name>')
def download_txt(file_name):
    file_path = os.path.join('txts', file_name)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1738, debug=True)

