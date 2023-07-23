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
        request_data_count = request.form.getlist('item_count')
        request_item_id = request.form.getlist('item_id')
        store_id = request.base_url.split("/")[-1].replace("store=", "")
        user_id = None
        order_check_flag = 0
        
        for idx, d in enumerate(request_data_count):
            if int(d) != 0:
                order_check_flag += 1
                ordered_append.kiosk_data(user_id=user_id, store_id=store_id)
                ordered_id = ordered_append.get_ordered_id()
                orderitem_append.kiosk_data(order_id=ordered_id, item_id=request_item_id[idx])
        if order_check_flag == 0:
            pass
        else:
            # TODO ordered id query 조회해서 return 하게끔 하기
            # TODO 주문 내역 확인 창 뜨면 좋을듯
            return render_template("kiosk/kiosk_history.html")
    
    store_header, store_data = store_detail.store_info(id=id)
    item_header, item_data = item_search.search_item_sort_type()
    
    return render_template("kiosk/kiosk_order.html", id=id, 
                           store_header=store_header, store_data=store_data, item_header=item_header, item_data=item_data)


@kiosk_bp.route("/kiosk/done", methods=["GET", "POST"])
def kiosk_done():
    return render_template("kiosk/kiosk_done.html")