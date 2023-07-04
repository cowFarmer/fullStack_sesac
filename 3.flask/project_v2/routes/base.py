from flask import Flask, render_template, request, Blueprint
from test.static_url import user_csv_file, order_csv_file, order_item_csv_file, item_csv_file, store_csv_file
from test.controller import ReadCsvDict, CheckData
from user.views import user_bp

app = Flask(__name__, static_folder="static")

app.register_blueprint(user_bp)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/store')
def store_list():
    headers, lines = ReadCsvDict.file_name(filename=store_csv_file)
    datas = CheckData().check(lines)
    return render_template("store_list.html", headers=headers, datas=datas)

@app.route('/store/<id>')
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
        
@app.route('/item')
def item_list():
    headers, lines = ReadCsvDict.file_name(filename=item_csv_file)
    datas = CheckData().check(lines)
            
    return render_template("item.html", headers=headers, datas=datas)

@app.route('/item/<id>')
def item_info(id):
    headers, lines = ReadCsvDict.file_name(filename=item_csv_file)
    datas = CheckData().check_id(id, lines, "id")
    order_headers, order_lines = ReadCsvDict.file_name(filename=order_item_csv_file)
    
    total_price, ordered_data = CheckData().check_total_price(datas, order_lines)
    return render_template("item_info.html", headers=headers, datas=datas,
                           order_headers=order_headers, ordered_data=ordered_data,
                           total_price=total_price)

@app.route('/order')
def order_list():
    headers, lines = ReadCsvDict.file_name(filename=order_csv_file)
    datas = CheckData().check(lines)
    
    return render_template("order.html", headers=headers, datas=datas)

@app.route('/order/<id>')
def order_id(id):
    return render_template("tmp.html")

@app.route('/order_item')
def order_item_list():
    headers, lines = ReadCsvDict.file_name(filename=order_item_csv_file)
    datas = CheckData().check(lines)
    
    return render_template("order_item.html", headers=headers, datas=datas)

    
@app.route('/order_item/<id>')
def order_item_id(id):
    return render_template("tmp.html")

if __name__ == "__main__":
    app.run(debug=True, port=8888)
    # app.run(debug=True, port=8888, host='0.0.0.0')