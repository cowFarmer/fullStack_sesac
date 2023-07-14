from flask import request, render_template, Blueprint
import math

from utils.query_util import QueryManager
from utils.page.pagelist import pageList


user_bp = Blueprint("user", __name__)

@user_bp.route("/user")
def user():
    # current_url
    current_url = request.url_rule
    
    # OPTION
    per_page = 5
    
    # GET
    search_page = request.args.get("page", default=1, type=int)
    search_name = request.args.get("name", default="", type=str).strip()
    search_gender = request.args.get("gender", default="", type=str)
    search_age_group = request.args.get("age_group", default=0, type=int)
    
    query_util = QueryManager()
    
    # 필터 적용 쿼리 받기
    query = query_util.search_user(search_page=search_page, search_name=search_name, search_gender=search_gender, search_age_group=search_age_group,
                           per_page=per_page)
    
    header, data = query_util.get_db_from_query(query)
    
    total_page = query_util.get_count_total_from_query(per_page, query)
    
    page_list = pageList(search_page, total_page)
    print(total_page)
    print(page_list)
    return render_template("user.html", header=header, data=data, url = current_url,
                           search_name=search_name, search_gender=search_gender, search_age_group=search_age_group,
                           total_page=total_page, page_list=page_list, page=search_page)