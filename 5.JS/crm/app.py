from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: 월간 매출액 합산을 구하시오
    # 테이블로 2023-01 ~ 2023-12 까지 월간 매출액을 구하는 쿼리
    conn = sqlite3.connect("./db/crm.db")
    cursor = conn.cursor()
    
    cursor.execute('''
            SELECT 
                strftime("%Y-%m", ordered.OrderAt) AS Month,
                SUM(item.UnitPrice) AS "TotalPrice Per Month"
            FROM ordered
            JOIN orderitem ON ordered.Id = orderitem.OrderId
            JOIN item ON orderitem.ItemId = item.Id
            GROUP BY Month
              ''')
    rows = cursor.fetchall()
    
    labels = []
    revenues = []
    
    for row in rows:
        labels.append(row[0])
        revenues.append(row[1])
    
    return render_template("index.html", rows=rows, labels=labels, revenues=revenues)

if __name__ == "__main__":
    app.run(debug=True)