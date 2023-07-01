from flask import Flask, render_template, request
import csv
from page.page_function import pageList

app = Flask(__name__, static_folder="static")

user_csv_file = "./csv/user.csv"
# user_csv_file = "./csv/big_user.csv"
store_csv_file = "./csv/store.csv"
item_csv_file = "./csv/item.csv"
order_csv_file = "./csv/order.csv"
order_item_csv_file = "./csv/orderitem.csv"

# TODO mode에 따라서 search 결과 보여주기
def readFile(filename=None, mode=None, search_info=None, per_page=None, current_page=None):
    data = []
    
    if per_page == None:
        return print("per_page 값을 넣어주세요")
    
    with open(filename, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = next(lines)
        
        # mode가 search인 경우 search_info의 데이터가 Name에 있으면 data 추가
        if mode == "search":
            for line in lines:
                if search_info != "":
                    if search_info in line("Name"):
                        data.append(line)
        else:
            for line in lines:
                data.append(line)
        
        total_page = len(data) // per_page
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
    # GET
    current_page = request.args.get('page', default=1, type=int)
    # 검색 공백 제거 .strip() 추가
    search_name = request.args.get('name', default="", type=str).strip()
    
    # OPTION
    per_page = 5
    
    headers, total_page, slice_page_data, page_list = readFile(filename=user_csv_file, search_info=search_name, per_page=per_page, current_page=current_page)
    
    return render_template('main.html', headers=headers, datas=slice_page_data, total_page=total_page, 
                           page=current_page, page_list=page_list, search_name=search_name)

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
    
# # csv 파일의 공백 처리
# @app.route('/space')
# def user_space():
#     data = []
#     with open("./csv/data_space.csv", "r") as file:
#         lines = csv.DictReader(file, skipinitialspace=True)
#         for line in lines:
#             data.append(line)
#             return data
#     return None
   
# # csv 파일 읽은 그대로 header를 처리하는 방법   
# @app.route('/header')
# def header():
#     data = []
#     with open("./csv/data_space.csv", "r") as file:
#         lines = csv.DictReader(file, skipinitialspace=True)
#         headers = next(lines)
#         for line in lines:
#             data.append(line)
#     return render_template('header.html', headers=headers, datas=data)    
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)