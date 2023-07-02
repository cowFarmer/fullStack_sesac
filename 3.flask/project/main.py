from flask import Flask, render_template, request
import csv
import math
from functions.page.page_function import pageList
from functions.dict_controller import DictLower

app = Flask(__name__, static_folder="static")

user_csv_file = "./csv/user.csv"
# user_csv_file = "./csv/big_user.csv"
store_csv_file = "./csv/store.csv"
item_csv_file = "./csv/item.csv"
order_csv_file = "./csv/order.csv"
order_item_csv_file = "./csv/orderitem.csv"

# TODO mode에 따라서 search 결과 보여주기
def readFile(filename=None, search_info=None, per_page=None, current_page=None):
    data = []
    search_info_filter = {}
    
    if per_page == None:
        return print("per_page 값을 넣어주세요")
    
    with open(filename, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        lines = DictLower.key_lower(lines)
        headers = lines[0].keys()
        
        # search_info filtering
        for key, value in search_info.items():
            if value != "":
                search_info_filter[key] = value
        if search_info["age_group"] == -10:
            search_info_filter.pop("age_group")
        
        if len(search_info_filter) == 0:
            for line in lines:
                data.append(line)
        else:
            # name 먼저 필터링
            if "name" in search_info_filter.keys():
                data = []
                for line in lines:
                    if search_info_filter["name"] in line["name"]:
                        data.append(line)
                search_info_filter.pop("name")
                lines = data
            
            # group_age 필터링
            if "age_group" in search_info_filter.keys():
                data = []
                age_group_value = search_info_filter.get("age_group")
                search_info_filter = {"age_group": [str(_) for _ in range(age_group_value, age_group_value+10)]}
                
                for line in lines:
                    if line["age"] in search_info_filter["age_group"]:
                        data.append(line)
                search_info_filter.pop("age_group")
                lines = data
            
            # 나머지 요소들 다 같은 경우
            if len(search_info_filter) > 0:
                data = []
                for line in lines:
                    if all(line.get(key) == value for key, value in search_info_filter.items()):
                        data.append(line)
        
        total_page = math.ceil((len(data) / per_page))
        data_start_index = per_page * (current_page - 1)
        data_end_index = data_start_index + per_page
        slice_page_data = data[data_start_index:data_end_index]
        page_list = pageList(total_page, current_page)
        
    return headers, total_page, slice_page_data, page_list
        

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
    # 검색 공백 제거 .strip() 추가
    search_name = request.args.get("name", default="", type=str).strip()
    search_gender = request.args.get("gender", default="", type=str)
    search_age_group = request.args.get("age_group", default=-10, type=int)
    
    # 필터용 딕셔너리 추가
    search_info["name"] = search_name
    search_info["gender"] = search_gender
    search_info["age_group"] = search_age_group

    headers, total_page, slice_page_data, page_list = readFile(filename=user_csv_file, search_info=search_info, per_page=per_page, current_page=current_page)
    return render_template('main.html', headers=headers, datas=slice_page_data, total_page=total_page, page_list=page_list, 
                           page=current_page, search_name=search_name, search_gender=search_gender, search_age_group=search_age_group)

@app.route('/user/<id>')
def user_info(id):
    data = []
    with open(user_csv_file, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = next(lines)
        for line in lines:
            if line["Id"] == id:
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