from bs4 import BeautifulSoup


html = '''
<html>
    <body>
    <div class="content">
        <h1>Title</h1>
        <p>paragraph 1</p>
        <p>paragraph 2</p>
        <ul>
            <li>item 1</li>
            <li>item 2</li>
            <li>item 3</li>
        </ul>
    </div>
    <div class="sidebar">
        <h2>Sidebar Title</h2>
        <p>Sidebar content<p>
    </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print("-"*10)
sidebar_div = soup.find('div', class_='.sidebar')
print(sidebar_div)
print("-"*10)
sidebar_div = soup.select('.sidebar')
print(sidebar_div)
print("-"*10)
sidebar_div = soup.select_one('.sidebar')
print(sidebar_div)
print("-"*10)
p_tags_in_sidebar = sidebar_div.find_all('a')
for p_tag in p_tags_in_sidebar:
    print(p_tag.get_text())
print("-"*10)
p_tags_in_sidebar = soup.find_all('a')
for p_tag in p_tags_in_sidebar:
    print(p_tag.get_text())
print("-"*10)