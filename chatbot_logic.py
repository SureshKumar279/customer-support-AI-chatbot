import json

def load_inventory():
    with open('data/inventory.json') as f:
        return json.load(f)

def answer_query(user_input):
    inventory = load_inventory()
    user_input = user_input.lower()

    for product, sizes in inventory.items():
        if product.lower() in user_input:
            for size, stock in sizes.items():
                if size.lower() in user_input:
                    if stock > 0:
                        return f"Yes, {product} size {size} is in stock ({stock} available)."
                    else:
                        return f"Sorry, {product} size {size} is out of stock."

            # Product found but no size mentioned
            available_sizes = [s for s, qty in sizes.items() if qty > 0]
            if available_sizes:
                return f"{product} is available in sizes: {', '.join(available_sizes)}"
            else:
                return f"Sorry, {product} is completely out of stock."

    return "I’m sorry, I couldn’t find that product. Please check the name or size."