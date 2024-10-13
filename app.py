from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app) 
openai.api_key = ''

@app.route('/generate-image', methods=['POST'])
def generate_image():
    # Get the prompt text from the request
    prompt = request.json.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Call the OpenAI DALL·E API to generate an image
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"  # Image resolution (you can use 256x256, 512x512, or 1024x1024)
        )

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']

        # Return the image URL as a response
        return jsonify({"image_url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

