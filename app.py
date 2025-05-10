@app.route('/emotion', methods=['POST'])
def emotion():
    data = request.get_json()
    print("Received data from frontend:", data)  # Debug line
    user_emotion = data.get('emotion')

    try:
        result = subprocess.run(
            ["ollama", "run", "qwen", f"What emotion is this: '{user_emotion}'?"],
            capture_output=True, text=True
        )
        print("Ollama output:", result.stdout)  # Debug line
        return jsonify({'response': result.stdout.strip()})
    except Exception as e:
        print("Error:", e)
        return jsonify({'response': f"Error: {e}"})
