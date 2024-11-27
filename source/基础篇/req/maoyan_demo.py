import re 
import requests 
import json
from typing import List

def get_one_page():
    url = "https://www.maoyan.com/board/4"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like   Gecko) Chrome/65.0.3325.162 Safari/537.36'  
        }
    response = requests.get(url,headers=headers)
    html = response.text
    return html

def parse_item(html_content):
    # 正则表达式，使用命名组
#   <dd>
#                         <i class="board-index board-index-1">1</i>
#     <a href="/films/1200486" title="我不是药神" class="image-link" data-act="boarditem-click" data-val="{movieId:1200486}">
#       <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.pipi.cn/mmdb/54ecde9a2c9f2a51ba06d67d795a9434b8421.jpg?imageView2/1/w/160/h/220" alt="我不是药神" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
#         <p class="star">
#                 主演：徐峥,王传君,周一围
#         </p>
# <p class="releasetime">上映时间：2018-07-05</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
#     </div>

#       </div>
#     </div>

#                 </dd>
    pattern = re.compile( r'<dd>.*?<a href="/films/(?P<id>\d+)" title="(?P<title>.*?)".*?/>.*?<img data-src="(?P<url>.*?)".*?</dd>', re.DOTALL)
    
    # 搜索匹配
 
    # 搜索匹配
    match_iter = pattern.finditer(html_content)
    
    # 提取信息并创建MovieInfo实例
    for match in match_iter:
        group_dict = match.groupdict()
        yield group_dict
        # yield movie_info
        #print(movie_info.__dict__)
def write_to_file(item_list):
    with open('maoyan_movie.txt', 'w', encoding='utf-8') as f:
        json.dump(item_list, f,indent=4)
if __name__ == '__main__':
    html_content = get_one_page()
    print(html_content)
    item_list =  list(parse_item(html_content))
    write_to_file(item_list)

