import random

class GenerateAddress:
    def __init__(self):
        self.korea_areas = ["서울", "경기", "강원", "충청북도", "충청남도", "경상북도", "경상남도", "전라북도", "전라남도", "제주"]
        self.seoul_areas = ["강남구", "강동구", "강서구", "강북구", "관악구", "광진구", "구로구", "금천구", "노원구", \
                            "동대문구", "도봉구", "동작구", "마포구", "서대문구", "성동구", "성북구", "서초구", "송파구", \
                            "영등포구", "용산구", "양천구", "은평구", "종로구", "중구", "중랑구"]
        self.road_names = ["로", "길", "대로", "번길"]
    
    def get_address(self):
        self.address = f"{random.choice(self.korea_areas)} {random.choice(self.seoul_areas)} {random.randint(1, 100)}{random.choice(self.road_names)} {random.randint(1, 100)}"
        return self.address