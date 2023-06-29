from flask import Flask, render_template, request
import csv

app = Flask(__name__, static_folder="static")

def get_user(id):
    with open("./csv/user.csv", "r") as file:
        lines = csv.DictReader(file)
        for line in lines:
            print(line)
            if line["Id"] == id:
                return line
    return None

# csv 파일의 공백 처리
@app.route('/space')
def user_space():
    data = []
    with open("./csv/data_space.csv", "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        for line in lines:
            # clean_row = {key.strip: value.strip() for key, value in line.items()}
            # data.append(clean_row)
            data.append(line)
            return data
    return None
   
# csv 파일 읽은 그대로 header를 처리하는 방법   
@app.route('/header')
def header():
    data = []
    with open("./csv/data_space.csv", "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = [header.strip() for header in lines.fieldnames]
        # # 첫 줄을 header로 가져오는 두 번째 방법
        # headers = next(lines)
        for line in lines:
            data.append(line)
    return render_template('header.html', headers=headers, datas=data)

@app.route('/big_user/')
def big_user():
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_name = search_name.strip()    
    data = []
    per_page = 5    
                
    with open("./csv/user.csv", "r") as file:
        lines = csv.DictReader(file, skipinitialspace=True)
        headers = next(lines)
        
        if search_name != "":
            for line in lines:
                if search_name in line['Name']:
                    data.append(line)
        else:
            for line in lines:
                data.append(line)
                
    total_page = (len(data) // per_page) + 1
    start_index = per_page * (page - 1)
    end_index = max(5, start_index + per_page)
    page_data = data[start_index:end_index]
    current_min_page_num = max(1, page-2)
    current_max_page_num = min(total_page, page+2)
    page_list = [_ for _ in range(current_min_page_num, current_max_page_num+1)]
    
    return render_template('big_user.html', headers=headers, datas=page_data, total_page=total_page, page=page, page_list=page_list)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user')
def user():
    with open("./csv/user.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("main.html", users_info = lines)

@app.route('/user/<id>')
def user_info(id):
    user = get_user(id)
    return render_template("user_info.html", user_info = user)

@app.route('/store')
def store_list():
    with open("./csv/store.csv", "r") as file:
        lines = csv.reader(file)
        return render_template("store_list.html", users_info = lines)

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