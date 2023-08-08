import requests
from bs4 import BeautifulSoup
from datetime import date


def get_movie_ranking_data():
    movie_url = "https://movie.daum.net"
    ranking_url = "/ranking/reservation"
    
    data = requests.get(movie_url+ranking_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    
    movie_ranking_section = soup.select('#mainContent > .section_ranking > .box_ranking > .list_movieranking > li')

    movie_data = []
    for movie in movie_ranking_section:
        movie_thumb_cont = movie.select_one('.thumb_cont')
        movie_info = movie.select_one('.poster_info > a')
        
        name = movie_thumb_cont.select_one('.tit_item > a').text
        grade = movie_thumb_cont.select_one('.txt_grade').text
        reservation_percente = movie_thumb_cont.select_one('.info_txt > .txt_num').text
        img_url = movie.select_one('.img_thumb')['src']
        short_summary = movie_info.text.strip()
        url = f"{movie_url}{movie_thumb_cont.select_one('.tit_item > a')['href']}"
        ranking = movie.select_one('.rank_num').text
        today_date = date.today()
        
        movie_data.append({
            'name': name,
            'grade': grade,
            'reservation_percente': reservation_percente,
            'img_url': img_url,
            'short_summary': short_summary,
            'url': url,
            'ranking': ranking,
            'today_date': today_date,
        })
    return movie_data

if __name__ == '__main__':
    print(get_movie_ranking_data())