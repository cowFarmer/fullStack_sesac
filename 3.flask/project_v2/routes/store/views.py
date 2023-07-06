from flask import Blueprint, render_template
from utils.controller import ReadCsvDict, CheckData
from utils.static_url import store_csv_file, order_csv_file, item_csv_file, order_item_csv_file


store_bp = Blueprint('store', __name__)

@store_bp.route('/store')
def store_list():
    headers, lines = ReadCsvDict.file_name(filename=store_csv_file)
    datas = CheckData().check(lines)
    return render_template("store_list.html", headers=headers, datas=datas)

@store_bp.route('/store/<id>')
def store_info(id):
    headers, lines = ReadCsvDict.file_name(filename=store_csv_file)
    datas = CheckData().check_id(id, lines, "id")
    
    ordered_data = []
    order_headers, order_lines = ReadCsvDict.file_name(filename=order_csv_file)
    ordered_data = CheckData().check_same_feature(datas, "id", order_lines, "storeid")
    
    # 오더 유저 아이디와 오더 아이템 비교
    _, order_item_lines = ReadCsvDict.file_name(filename=order_item_csv_file)
    ordered_item = CheckData().check_same_feature(ordered_data, "orderid", order_item_lines, "orderid")
    
    # 오더 아이템과 아이템 비교
    _, item_lines = ReadCsvDict.file_name(filename=item_csv_file)
    items = CheckData().check_same_feature(ordered_item, "itemid", item_lines, "id")
    
    total_price = CheckData().total_price(items)
    
    return render_template("store_info.html", headers=headers, datas=datas, 
                           order_headers=order_headers, ordered_data=ordered_data,
                           total_price=total_price)