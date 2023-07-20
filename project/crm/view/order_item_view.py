from flask import Blueprint, render_template, request

from model.pagelist import pageList
from model.query_util import QueryUtil
from model.order_query import OrderItemSearch


order_item_bp = Blueprint("order_item", __name__)

@order_item_bp.route("/order_item")
def order_item():
    query_util = QueryUtil()
    order_item_search = OrderItemSearch()
    
    per_page = 15
    current_url = "/order_item"
    order_url = "/order"
    item_url = "/item"
    
    search_page = request.args.get("page", default=1, type=int)
    
    order_item_header = query_util.get_header_from_table('orderitem')
    order_item_data, total_page = order_item_search.search_order_item(per_page=per_page, search_page=search_page)
    page_list = pageList(search_page, total_page)
    
    
    return render_template("order/order_item.html", order_item_header=order_item_header, order_item_data=order_item_data,
                           current_url=current_url, item_url=item_url, order_url=order_url,
                           total_page=total_page, page_list=page_list, page=search_page)
