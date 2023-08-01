from flask import Blueprint, render_template, request

from model.item_query import ItemSearch, ItemDetail
from app import Store

item_bp = Blueprint("item", __name__)

@item_bp.route("/item")
def item():
    item_search = ItemSearch()
    current_url = "/item"
    header, data = item_search.search_item()
    test = Store.query.all()
    print(test)
    
    return render_template("item/item.html", current_url=current_url, header=header, data=data)

@item_bp.route("/item/<id>")
def item_detail(id):
    item_detail = ItemDetail()
    current_url = "/item"
    item_header, item_data = item_detail.item_info(id=id)
    history_header, history_data = item_detail.item_transaction_history(id=id)
    month = [d["month"] for d in history_data]
    total_revenue = [d["total revenue"] for d in history_data]
    total_count = [d["total count"] for d in history_data]
    return render_template("item/item_detail.html", current_url=current_url, 
                           item_header=item_header, item_data=item_data, history_header=history_header, history_data=history_data,
                           month=month, total_revenue=total_revenue, total_count=total_count)