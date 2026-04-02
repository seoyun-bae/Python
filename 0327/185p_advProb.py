persons = ["Kim", "Park", "Lee" ]
restaurants = ["Korea", "American", "French"]
locations = ["서울", "부산", "대전"]

for person in persons:
    for restaurant in restaurants:
        for location in locations:
            print(person + "이 " + location + "에 있는 " + restaurant + " 식당을 방문")
