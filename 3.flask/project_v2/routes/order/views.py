from flask import Blueprint, render_template
from utils.controller import ReadCsvDict, CheckData
from utils.static_url import order_csv_file

order_bp = Blueprint('order', __name__)


@order_bp.route('/order')
def order_list():
    headers, lines = ReadCsvDict.file_name(filename=order_csv_file)
    datas = CheckData().check(lines)
    
    return render_template("order.html", headers=headers, datas=datas)

@order_bp.route('/order/<id>')
def order_id(id):
    return render_template("tmp.html")