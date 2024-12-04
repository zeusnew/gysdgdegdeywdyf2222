from flask import Flask, render_template, request, jsonify
from truecallerpy import search_phonenumber

app = Flask(__name__)

# API Key
API_KEY = 'a1i0Z--jzbJC6kx-2_s3OMNW2X7O2Qe3ca-XwmHexijCBA6MNKAO2ciUw756zhWj'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    phone_number = request.form['phone_number']
    try:
        response = search_phonenumber(phone_number, "IN", API_KEY)
        if "data" in response and len(response["data"]) > 0:
            data = response["data"][0]
            return jsonify({'success': True, 'data': data})
        else:
            return jsonify({'success': False, 'message': 'No data found.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
