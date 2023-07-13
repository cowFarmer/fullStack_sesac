from flask import Blueprint, render_template, request
from utils.controller import ReadCsvDict, CheckData
from utils.static_url import order_csv_file

order_bp = Blueprint('order', __name__)


@order_bp.route('/order')
def order_list():
    start_date = request.args.get("start_date", default="", type=str)
    end_date = request.args.get("end_date", default="", type=str)
    
    headers, lines = ReadCsvDict.file_name(filename=order_csv_file)
    
    # date filtering
    datas, result_flag = CheckData().check_date(lines, start_date, end_date)
    
    return render_template("order.html", headers=headers, datas=datas,
                           start_date=start_date, end_date=end_date, result_flag=result_flag)

@order_bp.route('/order/<id>')
def order_id(id):
    return render_template("tmp.html")