from flask import Blueprint, render_template, request, redirect

from model.query_util import QueryUtil
from model.store_query import StoreSearch, StoreDetail
from model.item_query import ItemSearch


kiosk_bp = Blueprint('kiosk', __name__)

@kiosk_bp.route("/kiosk")
def kiosk():
    # TODO 1차
    # 1. store 정보 가져오기
    # 2. store 선택하여 kiosk_store로 이동하기
    query_util = QueryUtil()
    store_search = StoreSearch()
    # request.path
    current_url = "/kiosk"
    
    header, data = store_search.store_data()
    return render_template("/kiosk/kiosk.html", header=header, data=data,
                           current_url=current_url)

@kiosk_bp.route("/kiosk/store=<id>", methods=["GET", "POST"])
def kiosk_store(id):
    store_detail = StoreDetail()
    item_search = ItemSearch()
    
    if request.method == "POST":
        request_data_count = request.form.getlist('item_count')
        request_data_key = request.form.getlist('item_key')
        request_data_value = request.form.getlist('item_value')
        print(request_data_count)
        print(request_data_key)
        print(request_data_value)
        
        for i in request_data_count:
            pass
        
        # return render_template("kiosk/kiosk_done.html")
    # TODO 2차
    # 3. store에 있는 메뉴 조회할 수 있게 하기
    # 4. 메뉴 +- 버튼 만들기
    # 5. submit 버튼 만들기
    # 6. 메뉴 GET하기
    # 7. GET한 결과 DB에 POST하기
    store_header, store_data = store_detail.store_info(id=id)
    item_header, item_data = item_search.search_item_sort_type()
    
    return render_template("kiosk/kiosk_order.html", id=id, 
                           store_header=store_header, store_data=store_data, item_header=item_header, item_data=item_data)


@kiosk_bp.route("/kiosk/done", methods=["GET", "POST"])
def kiosk_done():
    return render_template("kiosk/kiosk_done.html")