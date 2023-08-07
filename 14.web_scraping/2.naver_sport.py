import requests
from bs4 import BeautifulSoup


def get_naver_sportsnews():
    data = requests.get('https://sports.news.naver.com/index')
    soup = BeautifulSoup(data.text, 'html.parser')

    news = soup.select('.today_list > li')

    naver_news_url = "https://sports.news.naver.com"

    for n in news:
        # news의 title 제목 가져오기
        # print(n.select_one('.title').text)
        
        a_tag = n.select_one('a')
        print(a_tag['title'])
        print(f"{naver_news_url}{a_tag['href']}")
    

def get_naver_land(type):
    naver_news_url = "https://land.naver.com"
    
    data = requests.get('https://land.naver.com/news/')
    soup = BeautifulSoup(data.text, 'html.parser')
    
    main_container = soup.select_one('#container > #content')
    
    if type == 'headline':
        class_type = 'NE\=a\:chl'
    elif type == 'trend':
        class_type = 'NE\=a\:trd'
    else:
        return "unknown type"
    
    section = main_container.select_one(f'.{class_type}')
    
    li_tags = section.select('ul > li')
    
    for li in li_tags:
        if type == 'headline':
            detail_url = f"{naver_news_url}{li.select('a')[1]['href']}"
        elif type == 'trend':
            detail_url = f"{naver_news_url}{li.select_one('a')['href']}"
        
        get_news_content(detail_url)    
        
        # header, body = get_news_content(detail_url)
        # print(header)
        # print(body)
    
def get_news_content(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    
    # 이런 식으로 표현도 가능
    news_content = soup.select_one('.news_end')
    if news_content:
        start_span = news_content.find('span')
        end_p = news_content.find('p', class_='source')
        if start_span and end_p:
            content = start_span.next_element
            while content and content != end_p:
                if isinstance(content, str) and content.strip():
                    print(content.strip())
                content = content.next_element
    print('-'*10)
    
    # container = soup.select_one('#container')
    # header = container.select_one('.article_header').text
    # body = container.select_one('.article_body').text
                
    # return header, body
    
if __name__ == '__main__':
    # get_naver_sportsnews()
    get_naver_land('headline')
    # get_naver_land('trend')