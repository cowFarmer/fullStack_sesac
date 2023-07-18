from flask import request, render_template, Blueprint

from model.user_query import UserSearch
from model.pagelist import pageList
from model.query_util import QueryUtil
from model.user_detail_query import UserDetail


user_bp = Blueprint("user", __name__)

@user_bp.route("/user")
def user():
    query_util = QueryUtil()
    user_search = UserSearch()
    
    # OPTION
    per_page = 15
    # current_url = f"{request.url_rule}"
    current_url = "/user"
    
    # GET
    search_page = request.args.get("page", default=1, type=int)
    search_name = request.args.get("name", default="", type=str).strip()
    search_gender = request.args.get("gender", default="", type=str)
    search_age_group = request.args.get("age_group", default=0, type=int)
    
    header = query_util.get_header_from_table("user")
    data, total_page = user_search.search_user(search_name=search_name, search_gender=search_gender, search_age_group=search_age_group,
                           search_page=search_page, per_page=per_page)
    
    page_list = pageList(search_page, total_page)
    
    search_keyword = f"&name={search_name}&gender={search_gender}"
    if search_age_group != 0:
        search_keyword += f"&age_group={search_age_group}"
    
    return render_template("user/user.html", header=header, data=data, current_url=current_url,
                           search_name=search_name, search_gender=search_gender, search_age_group=search_age_group,
                           total_page=total_page, page_list=page_list, page=search_page,
                           search_keyword=search_keyword)
    
@user_bp.route("/user/<id>")
def user_detail(id):
    query_util = QueryUtil()
    user_detail = UserDetail()
    
    order_url = "/order_detail"
    store_url = "/store"
    
    user_header = query_util.get_header_from_table("user")
    user_data = user_detail.user_info(id=id)
    transaction_header = query_util.get_header_from_table("ordered")
    transaction_data = user_detail.user_transaction_history(id=id)
    order_item_count_header, order_item_count_data = user_detail.user_item_count_order(id=id)
    order_store_count_header, order_store_count_data = user_detail.user_store_count_order(id=id)
    
    return render_template("user/user_info.html", id=id, order_url=order_url, store_url=store_url,
                           user_header=user_header, user_data=user_data, transaction_header=transaction_header, transaction_data=transaction_data,
                           order_item_count_header=order_item_count_header, order_item_count_data=order_item_count_data,
                           order_store_count_header=order_store_count_header, order_store_count_data=order_store_count_data)