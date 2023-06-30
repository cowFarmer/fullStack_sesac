from flask import Flask, render_template, request
import csv

# TODO user_info에서 user가 주문한 order 모아보기

app = Flask(__name__, static_folder="static")

user_csv_file = "./csv/user.csv"
big_user_csv_file = "./csv/big.csv"
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
    page = request.args.get('page', default=1, type=int)
    # 검색 공백 제거 .strip() 추가
    search_name = request.args.get('name', default="", type=str).strip()
    data = []
    per_page = 5    
    with open(user_csv_file, "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = next(lines)
        
        for line in lines:
            if search_name != "":
                if search_name in line["Name"]:
                    data.append(line)
            else:
                data.append(line)
        
    total_page = (len(data) // per_page) + 1
    start_index = per_page * (page - 1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]
    # 현재 페이지 기준 앞, 뒤로 2개씩 page_list 만들기
    page_list = [_ for _ in range(max(1, page-2), min(total_page, page+2)+1)]
    
    return render_template('main.html', headers=headers, datas=page_data, total_page=total_page, 
                           page=page, page_list=page_list, search_name=search_name)

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