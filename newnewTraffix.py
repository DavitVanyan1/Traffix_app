from flask import Flask, render_template, send_file, request, redirect, url_for
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Traffix_app_page.html')

@app.route('/get-map-image')
def get_map_image():
    map_path = url_for('static', filename='Yerevan-Map.jpg')
    if os.path.exists(map_path):
        return send_file(map_path, mimetype='image/jpeg')
    else:
        return "Map image not found. Put 'Yerevan-Map.jpg' at the configured path.", 404

@app.route('/get-logo-image')
def get_logo_image():
    logo_path = r"C:\Users\User\Desktop\Traffix_logo.jpg"
    if os.path.exists(logo_path):
        return send_file(logo_path, mimetype='image/jpeg')
    else:
        return "Logo image not found. Put 'Traffix_logo.jpg' at the configured path.", 404

@app.route('/download-registration-form')
def download_registration_form():
    # Create a simple PDF registration form
    # In a real application, you would use a library like reportlab to generate a PDF
    # For this example, we'll create a simple text file that represents a PDF
    form_content = """PARKING LOT REGISTRATION FORM
    
Please fill out this form to register your parking lot with Traffix.

OWNER INFORMATION:
First Name: __________________
Last Name: ___________________
Email: _______________________
Phone: _______________________

PARKING LOT INFORMATION:
Name: ________________________
Address: _____________________
Total Spaces: ________________
Hourly Rate: _________________

DOCUMENTS REQUIRED:
- Proof of ownership or authorization
- Business license
- Tax identification number
- Site plan/layout

Please submit this completed form along with the required documents."""
    
    # Save to a temporary file
    temp_path = "parking_registration_form.pdf"
    with open(temp_path, 'w') as f:
        f.write(form_content)
    
    return send_file(temp_path, as_attachment=True, download_name="Traffix_Parking_Registration_Form.pdf")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)