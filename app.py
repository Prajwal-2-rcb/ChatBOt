from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Google Generative AI API key
genai.configure(api_key='AIzaSyDcm1pCetUX3tDQyBQ7hbS88thTaBZuM7Q')  # Replace with your actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        formatted_text = response.text.replace("\n", "<br>")  # Replace line breaks with <br> for HTML
        return jsonify({'text': formatted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
