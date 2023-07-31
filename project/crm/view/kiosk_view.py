from flask import Blueprint, render_template, request, redirect

from model.query_util import QueryUtil
from model.store_query import StoreSearch, StoreDetail
from model.item_query import ItemSearch
from model.kiosk_query import OrderedAppend, OrderitemAppend


kiosk_bp = Blueprint('kiosk', __name__)

@kiosk_bp.route("/kiosk")
def kiosk():
    store_search = StoreSearch()
    # request.path
    current_url = request.path
    
    header, data = store_search.store_data()
    return render_template("/kiosk/kiosk.html", header=header, data=data,
                           current_url=current_url)

@kiosk_bp.route("/kiosk/store=<id>", methods=["GET", "POST"])
def kiosk_store(id):
    store_detail = StoreDetail()
    item_search = ItemSearch()
    ordered_append = OrderedAppend()
    orderitem_append = OrderitemAppend()
    
    if request.method == "POST":
        user_id = None
        request_data_count = [int(count) for count in request.form.getlist('item_count')]
        request_item_id = request.form.getlist('item_id')
        
        if sum(request_data_count) > 0:
            user_id = ordered_append.get_tmp_user_id()
            ordered_id = ordered_append.get_tmp_ordered_id()
            ordered_append.kiosk_data(user_id=user_id, store_id=id)
            
            for idx, count in enumerate(request_data_count):
                orderitem_append.kiosk_data(order_id=ordered_id, item_id=request_item_id[idx], count=count)
                
            return render_template("kiosk/kiosk_history.html")
        else:            
            pass

    store_header, store_data = store_detail.store_info(id=id)
    item_header, item_data = item_search.search_item_sort_type()
    
    return render_template("kiosk/kiosk_order.html", id=id, 
                           store_header=store_header, store_data=store_data, item_header=item_header, item_data=item_data)