import tkinter as tk
from tkinter import scrolledtext
import json
import re

def check_inventory(query):
    normalized_query = query.replace("_", " ").lower()
    for category, products in inventory.items():
        for product, details in products.items():
            normalized_product = product.replace("_", " ").lower()
            if normalized_product in normalized_query:
                sizes = details.get("sizes", {})
                # Check if a size is mentioned
                for size in sizes:
                    if re.search(rf"\b{re.escape(size.lower())}\b", normalized_query):
                        stock = sizes[size]
                        return f"Yes, we have {stock} {normalized_product}(s) in size {size}." if stock > 0 else f"Sorry, {normalized_product} in size {size} is out of stock."

                # If no size mentioned, return general info
                info = f"{normalized_product.capitalize()} is available in sizes: {', '.join(sizes.keys())}. "
                info += f"It comes in colors: {', '.join(details.get('colors', []))}. "
                info += f"Price: {details.get('price')}, Fabric: {details.get('fabric')}."
                return info
    return None

def generate_response(query):
    inventory_answer = check_inventory(query)
    if inventory_answer:
        return inventory_answer
    else:
        return "Sorry, I don't have that information. Please ask about available products or sizes."

def handle_user_input():
    user_message = user_entry.get()
    if user_message.strip() == "":
        return

    conversation_area.insert(tk.END, f"You: {user_message}\n")
    user_entry.delete(0, tk.END)

    response = generate_response(user_message)
    conversation_area.insert(tk.END, f"Bot: {response}\n\n")
    conversation_area.see(tk.END)

# Load inventory
with open("inventory.json", "r") as file:
    inventory = json.load(file)

# GUI setup
root = tk.Tk()
root.title("Fashion Support Chatbot")

conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
conversation_area.pack(padx=10, pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

user_entry = tk.Entry(frame, width=50, font=("Arial", 12))
user_entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(frame, text="Send", font=("Arial", 12), command=handle_user_input)
send_button.pack(side=tk.LEFT)

conversation_area.insert(tk.END, "Bot: Hello! Ask me about product stock, sizes, or anything else.\n\n")

root.mainloop()
from flask import Flask, request, jsonify
from chatbot_logic import get_chatbot_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
