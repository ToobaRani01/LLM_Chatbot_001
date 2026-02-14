from flask import Flask , render_template , request , jsonify
from llm_config import coversation

app = Flask(__name__)
@app.route("/")
def home():
    """ Main chat interface load karta hai """
    return render_template("index.html")



@app.route("/chat", methods=["POST"])
def chat():
     
    """Frontend se message receive karke LLM se response leta hai """
    user_message = request.json.get("message")
    try:
        # Check if this is the very first message in memory
        is_first = len(coversation.memory.chat_memory.messages) == 0
        
        # Get AI Response
        response = coversation.predict(input=user_message)

        # Agar pehla interaction hai, to greeting attach karein
        if is_first:
            # response = f"Hello Tooba 👋 I am your AI assistant.\n\n{response}"
            response = "Hello Tooba 👋 I am your AI assistant. How can I help you today?"
    except Exception as e:
        response = f"Error: {str(e)}"

    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)