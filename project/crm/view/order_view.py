from flask import Blueprint, render_template, request

from model.pagelist import pageList
from model.query_util import QueryUtil
from model.order_query import OrderSearch, OrderDetailSearch


order_bp = Blueprint("order", __name__)

@order_bp.route("/order")
def order():
    query_util = QueryUtil()
    order_search = OrderSearch()
    
    per_page = 15
    current_url = "/order"
    
    search_page = request.args.get("page", default=1, type=int)
    
    order_header = query_util.get_header_from_table('ordered')
    order_data, total_page = order_search.search_order(per_page=per_page, search_page=search_page)
    page_list = pageList(search_page, total_page)
    
    return render_template("order/order.html", order_header=order_header, order_data=order_data,
                           current_url=current_url,
                           total_page=total_page, page_list=page_list, page=search_page)
    

@order_bp.route("/order/<id>")
def order_detail(id):
    order_detail_search = OrderDetailSearch()    
    order_detail_header, order_detail_data = order_detail_search.search_order_id(id=id)
    item_url = "/item"
    return render_template("order/order_detail.html", order_detail_header=order_detail_header, order_detail_data=order_detail_data,
                           item_url=item_url)