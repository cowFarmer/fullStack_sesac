import requests
from bs4 import BeautifulSoup


def get_movie_data():
    movie_url = "https://movie.daum.net"
    ranking_url = "/ranking/reservation"
    
    data = requests.get(movie_url+ranking_url)
    soup = BeautifulSoup(data.text, 'html.parser')
    
    movie_ranking_section = soup.select('#mainContent > .section_ranking > .box_ranking > .list_movieranking > li')

    for movie in movie_ranking_section:
        movie_thumb_cont = movie.select_one('.thumb_cont')
        name = movie_thumb_cont.select_one('.tit_item > a').text
        grade = movie_thumb_cont.select_one('.txt_grade').text
        reservation_percente = movie_thumb_cont.select_one('.info_txt > .txt_num').text
        
        movie_info = movie.select_one('.poster_info > a')
        img_url = f"{movie_url}{movie_info['href']}"
        short_summary = movie_info.text.strip()
        
        print(name)
        print(grade)
        print(reservation_percente)
        print(img_url)
        print(short_summary)
        pass            

if __name__ == '__main__':
    get_movie_data()