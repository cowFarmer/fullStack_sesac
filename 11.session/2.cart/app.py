from flask import Flask, render_template, session, redirect, url_for


app = Flask(__name__)
app.secret_key = "sesac_fullstack"

items = {
    "item1": {"name": "홍길동", "price": 50},
    "item2": {"name": "홍길순", "price": 150},
    "item3": {"name": "김아무개", "price": 30},
}

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/add_to_cart/<item_code>")
def add_to_cart(item_code):
    if "cart" not in session:
        session["cart"] = {}

    # 카트에 물건 담기
    if item_code in session["cart"]:
        session["cart"][item_code] += 1
    else:
        session["cart"][item_code] = 1
    
    session.modified = True
    
    # 담은 이후 옵션
    return redirect(url_for("index"))

@app.route("/remove_item_from_cart/<item_code>")
def remove_item_from_cart(item_code):
    if item_code == "all":
        session['cart'] = {}
    else:
        session['cart'].pop(item_code)
    session.modified = True
    
    return redirect(url_for('view_cart'))

@app.route("/view_cart")
def view_cart():
    cart = session.get("cart", {})
    if cart:
        for item_id, item_count in cart.items():
            item = items.get(item_id)
            cart[item_id] = {"name": item["name"], "price": item["price"], "count": item_count}
    
    total_price = 0
    for item_value in cart.values():
        total_price += item_value["price"] * item_value["count"]
    
    return render_template("cart.html", cart=cart, total_price=total_price)

if __name__ == "__main__":
    app.run(debug=True, port=8080)