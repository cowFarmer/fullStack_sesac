from flask import request, render_template, Blueprint
import math

from utils.database_util import ConnectDatabase


user_bp = Blueprint("user", __name__)

@user_bp.route("/user")
def user():
    # OPTION
    per_page = 15
    
    # GET
    current_page = request.args.get("page", default=1, type=int)
    search_name = request.args.get("name", default="", type=str).strip()
    search_gender = request.args.get("gender", default="", type=str)
    search_age_group = request.args.get("age_group", default=0, type=int)
    
    lookup_database = ConnectDatabase()
    query = '''
    SELECT *
    FROM user
    LIMIT 5;
    '''
    data = lookup_database.get_db_from_query(query)
    header = data[0].keys()
    
    query = '''
    SELECT COUNT(*) AS total_user
    FROM user;
    '''
    total_data = lookup_database.get_db_from_query(query)
    total_page = math.ceil(total_data[0]["total_user"] / per_page)
    
    # search_name, search_age_group
    
    return render_template("user.html", header=header, data=data)