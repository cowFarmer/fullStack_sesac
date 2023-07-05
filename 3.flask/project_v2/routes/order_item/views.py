from flask import Blueprint, render_template
from utils.controller import ReadCsvDict, CheckData
from utils.static_url import order_item_csv_file

order_item = Blueprint('order_item', __name__)

@order_item.route('/order_item')
def order_item_list():
    headers, lines = ReadCsvDict.file_name(filename=order_item_csv_file)
    datas = CheckData().check(lines)
    
    return render_template("order_item.html", headers=headers, datas=datas)

@order_item.route('/order_item/<id>')
def order_item_id(id):
    return render_template("tmp.html")