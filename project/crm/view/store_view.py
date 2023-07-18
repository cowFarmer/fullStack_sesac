from flask import render_template, Blueprint, request


from model.pagelist import pageList
from model.query_util import QueryUtil
from model.store_query import StoreSearch, StoreDetail


store_bp = Blueprint("store", __name__)

@store_bp.route("/store")
def store():
    query_util = QueryUtil()
    store_search = StoreSearch()
    
    per_page = 15
    current_url = "/store"
    
    search_page = request.args.get("page", default=1, type=int)
    
    store_header = query_util.get_header_from_table('store')
    store_item, total_page = store_search.search_store(search_page=search_page, per_page=per_page)
    page_list = pageList(search_page, total_page)
    
    return render_template("store/store.html", header=store_header, data=store_item, current_url=current_url,
                           total_page=total_page, page_list=page_list, page=search_page)

@store_bp.route("/store/<id>")
def store_detail(id):
    store_detail = StoreDetail()
    user_url = "/user"
    
    # TODO: MONTH url 추가하기
    search_month = request.args.get("month", default="", type=str)
    
    store_header, store_data = store_detail.store_info(id=id)
    transaction_header, transaction_data = store_detail.store_transaction_history_per_month(id=id)
    regular_customer_header, regular_customer_data = store_detail.store_transaction_history_regular_customer(id=id)
    
    return render_template("store/store_info.html", id=id, user_url=user_url,
                           store_header=store_header, store_data=store_data,
                           transaction_header=transaction_header, transaction_data=transaction_data,
                           regular_customer_header=regular_customer_header, regular_customer_data=regular_customer_data)