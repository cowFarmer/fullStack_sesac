# pageList return function
def pageList(total_page, current_page):
    print(total_page, current_page)
    if current_page <= 2:
        page_list = [_ for _ in range(1, min(total_page+1, 6))]
    elif current_page == total_page or current_page == total_page - 1:
        page_list = [_ for _ in range(max(1, total_page-4), total_page+1)]
    else:
        page_list = [_ for _ in range(current_page-2, current_page+2+1)]
    return page_list