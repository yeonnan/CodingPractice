# pprint는 pretty print의 약자이며, 데이터를 더 예쁘게 출력해 줍니다.
from pprint import pprint

sample_data = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":
        {
            "batter":
                [
                    {"id": "1001", "type": "Regular"},
                    {"id": "1002", "type": "Chocolate"},
                    {"id": "1003", "type": "Blueberry"},
                    {"id": "1004", "type": "Devil's Food"}
                ]
        },
    "topping":
        [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5007", "type": "Powdered Sugar"},
            {"id": "5006", "type": "Chocolate with Sprinkles"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"}
        ]
}

pprint(sample_data) # print로 출력했을 때와 결과 비교해 보기!!