from flask import Blueprint, render_template
from utils.controller import ReadCsvDict, CheckData
from utils.static_url import item_csv_file, order_item_csv_file

item_bp = Blueprint("item", __name__)

@item_bp.route('/item')
def item_list():
    headers, lines = ReadCsvDict.file_name(filename=item_csv_file)
    datas = CheckData().check(lines)
            
    return render_template("item.html", headers=headers, datas=datas)

@item_bp.route('/item/<id>')
def item_info(id):
    headers, lines = ReadCsvDict.file_name(filename=item_csv_file)
    datas = CheckData().check_id(id, lines, "id")
    order_headers, order_lines = ReadCsvDict.file_name(filename=order_item_csv_file)
    
    total_price, ordered_data = CheckData().check_total_price(datas, order_lines)
    return render_template("item_info.html", headers=headers, datas=datas,
                           order_headers=order_headers, ordered_data=ordered_data,
                           total_price=total_price)