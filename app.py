from flask import Flask, render_template, request, jsonify
from llm_config import llm   # sirf llm import karna hai

app = Flask(__name__)

@app.route("/")
def home():
    """ Main chat interface load karta hai """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Frontend se message receive karke LLM se response leta hai"""
    user_message = request.json.get("message")
    try:
        # Directly call the LLM
        response = llm.invoke(user_message).content
    except Exception as e:
        response = f"Error: {str(e)}"

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
