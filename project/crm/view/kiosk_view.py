from flask import Blueprint, render_template

from model.query_util import QueryUtil
from model.store_query import StoreSearch


kiosk_bp = Blueprint('kiosk', __name__)

@kiosk_bp.route("/kiosk")
def kiosk():
    # TODO 
    # 1. store 정보 가져오기
    # 2. store 선택하여 kiosk_store로 이동하기
    query_util = QueryUtil()
    store_search = StoreSearch()
    current_url = "/kiosk"
    
    header, data = store_search.store_data()
    return render_template("/kiosk/kiosk.html", header=header, data=data,
                           current_url=current_url)

@kiosk_bp.route("/kiost/store=<id>")
def kiosk_store(id):
    # TODO
    # 3. store에 있는 메뉴 조회할 수 있게 하기
    # 4. 메뉴 +- 버튼 만들기
    # 5. submit 버튼 만들기
    # 6. 메뉴 GET하기
    # 7. GET한 결과 DB에 POST하기
    
    print(id)
    pass