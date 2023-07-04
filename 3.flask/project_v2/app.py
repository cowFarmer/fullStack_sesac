from flask import Flask, render_template, request
from functions.controller import ReadCsvDict, CheckData
from functions.user.user_function import filter_user_file

app = Flask(__name__, static_folder="static")

############################
# user_csv_file = "./csv/user.csv"
# user_csv_file = "./csv/big_user.csv"
# store_csv_file = "./csv/store.csv"
# item_csv_file = "./csv/item.csv"
# order_csv_file = "./csv/order.csv"
# order_item_csv_file = "./csv/orderitem.csv"
############################
# make csv 적용
user_csv_file = "./make_csv/user.csv"
store_csv_file = "./make_csv/store.csv"
item_csv_file = "./make_csv/item.csv"
order_csv_file = "./make_csv/order.csv"
order_item_csv_file = "./make_csv/orderlist.csv"
############################


@app.route('/')
def home():
    return render_template("home.html")

# user
@app.route('/user')
def user():
    # OPTION
    per_page = 5
    search_info = {}
    
    # GET
    current_page = request.args.get("page", default=1, type=int)
    search_name = request.args.get("name", default="", type=str).strip()
    search_gender = request.args.get("gender", default="", type=str)
    search_age_group = request.args.get("age_group", default=0, type=int)
    
    # 필터용 딕셔너리 추가
    search_info["name"] = search_name
    search_info["gender"] = search_gender
    search_info["age_group"] = search_age_group

    headers, total_page, slice_page_data, page_list = filter_user_file(filename=user_csv_file, search_info=search_info, per_page=per_page, current_page=current_page)
    
    return render_template('user.html', headers=headers, datas=slice_page_data, total_page=total_page, page_list=page_list, 
                           page=current_page, search_name=search_name, search_gender=search_gender, search_age_group=search_age_group)

@app.route('/user/<id>')
def user_info(id):
    # 유저 아이디 값 가져오기
    headers, lines = ReadCsvDict.file_name(filename=user_csv_file)
    datas = CheckData().check_id(id, lines, "id")
    
    # 유저 아이디와 오더 유저 아이디 비교
    order_headers, order_lines = ReadCsvDict.file_name(filename=order_csv_file)
    ordered_data = CheckData().check_same_feature(datas, "id", order_lines, "userid")
    
    # 오더 유저 아이디와 오더 아이템 비교
    _, order_item_lines = ReadCsvDict.file_name(filename=order_item_csv_file)
    ordered_item = CheckData().check_same_feature(ordered_data, "orderid", order_item_lines, "orderid")
    
    # 오더 아이템과 아이템 비교
    _, item_lines = ReadCsvDict.file_name(filename=item_csv_file)
    items = CheckData().check_same_feature(ordered_item, "itemid", item_lines, "id")
    
    total_price = CheckData().total_price(items)
    
    return render_template("user_info.html", headers=headers, datas=datas,
                           order_headers=order_headers, ordered_data=ordered_data,
                           total_price=total_price)

@app.route('/store')
def store_list():
    headers, lines = ReadCsvDict.file_name(filename=store_csv_file)
    datas = CheckData().check(lines)
    print("hello")
    return render_template("store_list.html", headers=headers, datas=datas)

@app.route('/store/<id>')
def store_info(id):
    headers, lines = ReadCsvDict.file_name(filename=store_csv_file)
    datas = CheckData().check_id(id, lines, "id")
    
    ordered_data = []
    order_headers, order_lines = ReadCsvDict.file_name(filename=order_csv_file)
    ordered_data = CheckData().check_same_feature(datas, "id", order_lines, "storeid")

    for i in headers:
        if i == "id":
            print("id")
    return render_template("store_order_info.html", headers=headers, datas=datas, 
                           order_headers=order_headers, ordered_data=ordered_data)
        
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