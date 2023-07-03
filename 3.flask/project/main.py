from flask import Flask, render_template, request
import csv
from functions.dict_controller import ReadCsvDict
from functions.user.user_function import filter_user_file

app = Flask(__name__, static_folder="static")

user_csv_file = "./csv/user.csv"
# user_csv_file = "./csv/big_user.csv"
store_csv_file = "./csv/store.csv"
item_csv_file = "./csv/item.csv"
order_csv_file = "./csv/order.csv"
order_item_csv_file = "./csv/orderitem.csv"

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
    search_age_group = request.args.get("age_group", default=-10, type=int)
    
    # 필터용 딕셔너리 추가
    search_info["name"] = search_name
    search_info["gender"] = search_gender
    search_info["age_group"] = search_age_group

    headers, total_page, slice_page_data, page_list = filter_user_file(filename=user_csv_file, search_info=search_info, per_page=per_page, current_page=current_page)
    return render_template('main.html', headers=headers, datas=slice_page_data, total_page=total_page, page_list=page_list, 
                           page=current_page, search_name=search_name, search_gender=search_gender, search_age_group=search_age_group)

@app.route('/user/<id>')
def user_info(id):
    data = []
    headers, lines = ReadCsvDict.file_name(filename=user_csv_file)
    for line in lines:
        if line["id"] == id:
            data.append(line)
            break
    
    return render_template("user_info.html", headers=headers, datas=data)

@app.route('/store')
def store_list():
    data = []
    with open(store_csv_file, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = next(lines)
        for line in lines:
            data.append(line)
    
    return render_template("store_list.html", headers=headers, datas=data)

@app.route('/store/<id>')
def store_info(id):
    data = []
    with open(order_csv_file, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = next(lines)
        for line in lines:
            if line["StoreId"] == id:
                data.append(line)
                
    return render_template("store_order_info.html", headers=headers, datas=data)
        
@app.route('/item')
def item_list():
    with open("./csv/item.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("item.html", users_info = lines)


@app.route('/order')
def order_list():
    with open("./csv/order.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("order.html", users_info = lines)


@app.route('/order_item')
def order_item_list():
    with open("./csv/orderitem.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("order_item.html", users_info = lines)

    
if __name__ == "__main__":
    app.run(debug=True, port=8080)
    # app.run(debug=True, port=8080, host='0.0.0.0')