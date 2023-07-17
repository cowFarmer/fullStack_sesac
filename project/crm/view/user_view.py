from flask import request, render_template, Blueprint

from model.user_query import UserSearch
from model.pagelist import pageList
from model.database_util import DatabaseController


user_bp = Blueprint("user", __name__)

@user_bp.route("/user")
def user():
    user_search = UserSearch()
    db_controlloer = DatabaseController()
    
    # OPTION
    per_page = 5
    current_url = request.url_rule
    
    # GET
    search_page = request.args.get("page", default=1, type=int)
    search_name = request.args.get("name", default="", type=str).strip()
    search_gender = request.args.get("gender", default="", type=str)
    search_age_group = request.args.get("age_group", default=0, type=int)
    
    header = db_controlloer.get_header_from_table("user")
    
    # 필터 적용 쿼리 받기
    data, total_page = user_search.search_user(search_page=search_page, search_name=search_name, search_gender=search_gender, search_age_group=search_age_group,
                           per_page=per_page)
    
    page_list = pageList(search_page, total_page)
    
    search_keyword = f"&name={search_name}&gender={search_gender}"
    if search_age_group != 0:
        search_keyword += f"&age_group={search_age_group}"
    
    return render_template("user/user.html", header=header, data=data, current_url = current_url,
                           search_name=search_name, search_gender=search_gender, search_age_group=search_age_group,
                           total_page=total_page, page_list=page_list, page=search_page,
                           search_keyword=search_keyword)
    
@user_bp.route("/user/<id>")
def user_detail(id):
    print(id)
    return render_template("user/user_info.html", id = id)