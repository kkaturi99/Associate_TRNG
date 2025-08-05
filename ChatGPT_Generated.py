#ChatGPT_Generated
# strA = "python is very easy to learn"
# strB = "파이썬ㅋㅋㅋ"

# print(len(strA))  
# print(len(strB)) 
# print(strA[:2])
# print(strB[-3:]) 
# print(strA[5:10])

# strC = strA + strB
# strD = """
# 여러 라인
# multi line
# 문자열을
# string
# """

# print(strD)
# print(strD[0:5])  # 첫 5글자 출력
# print(strD[-6:])  # 마지막 6글자 출력
# print(strD[9:])  # 9번째부터 끝에서 1글자 전까지 출력

# colors = ["red", "green", "blue"]
# colors.append("yellow")
# print(colors)  # ['red', 'green', 'blue', 'yellow']
# colors.insert(1, "orange")
# print(colors)  # ['red', 'orange', 'green', 'blue', 'yellow']


# list = [1,2,3,4,6,12,17,21]
# print(len(list))  # 리스트의 길이 출력
# print(list[-3])  # 리스트의 마지막 3번째 요
# list.append(100)  # 리스트에 100 추가
# print(list)  # [1, 2, 3, 4, 6, 12, 17, 21, 100]
# list.insert(5, 99)  # 2번째 인덱스에 99 추가
# print(list)  # [1, 2, 99, 3, 4, 6, 12, 17, 21, 100]
# list.remove(12)
# print(list)  # [1, 2, 99, 3, 4, 6, 17, 21, 100]


# device = ("아이폰", "아이패드", "맥북", "애플워치")
# device.count
# device.index("아이패드")  # 아이패드의 인덱스 찾기

# def sum(a, b):
#     return a + b

# print(sum(3, 5) ) # 8

# """ 
# #튜플활용
# print("---TUple---")
# tp = (100,200,300,400,500)
# print(len(tp))  # 튜플의 길이 출력
# print(tp[2]) 
# print(tp.index(300))

# def calc(a,b):
#     return a + b, a - b

# c = (calc(10, 5))  # (15, 5)
# print(calc(tp[2], tp[3]))
# print(type(c))

# print("id:%s, name:%s, age:%s" % (1, "홍길동", 20))  #(1, '홍길동', 20) 이게 튜플임
# print("id:{}, name:{}, age:{}".format(1, "홍길동", 20))  # id:1, name:홍길동, age:20

# args = (5,6)
# print(calc(*args))  # 언패킹: calc(5, 6)와 동일
# """




# #Set 활용
# print("---Set---")
# s = {1, 2, 3, 4, 5}
# v = {4, 5, 6, 7, 8}
# print(s.union(v))  # 합집합: {1, 2, 3, 4, 5, 6, 7, 8}
# print(s.intersection(v))  # 교집합: {4, 5}
# print(s.difference(v))  # 차집합: {1, 2, 3}


#dictionary 활용
# print("---Dictionary---")
# colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
# colors["orange"] = "orange"
# colors["Cherry"] = "red" # 새로운 키-값 추가
# print(colors) 
# print(colors["apple"])  # "red" 출력
# print(colors.get("banana"))  # "yellow" 출력
# del colors["grape"]  # "grape" 키 삭제
# print(colors)  # {'apple': 'red', 'banana': 'yellow', 'orange': 'orange', 'Cherry': 'red'}

# device = {"아이폰": 5 , "아이패드": 3, "맥북": 2, "애플워치": 4}
# print(device)
# print(device["아이폰"])
# del device["아이패드"]  # "아이패드" 키 삭제
# print(device)  # {'아이폰': 5, '맥북': 2, '애플워치': 4}
# device["아이폰"] = 200
# print(device)  # {'아이폰': 200, '맥북': 2, '애플워치': 4}

# for item in device.items():
#     print(item)  # 각 키-값 쌍 출력

# for k,v in device.items():
#     print(f"Device: {k}, Remains: {v}")  # 각 키-값 쌍을 포맷팅하여 출력
    

# isRight = True
# print(type(isRight))  # <class 'bool'>


# def setValue(newvalue):
#     x = newvalue
#     print(" 함수 내부 :",x)
    
# returnValue = setValue(10)
# print("함수 외부:", returnValue)  # None 출력, 함수가 값을 반환하지 않음

# def swap(a, b):
#     return b, a  # 튜플로 반환

# result = swap(10, 20)
# print(result)  # (20, 10) 출력


#demo loop
# value = 5
# while value > 0:
#     print(value)
#     value -= 1  # value를 1씩 감소시킴
    
# fruits = {"apple": 3, "banana": 2, "orange": 5}
# for item in fruits.items():
#     print(f"{item[0]}: {item[1]}")  # 각 과일과 개수를 출력
    
# def getbiggerthan10(i):
#     return i>10

# lst = [1,5,10,15,20,30]
# itemL = filter(getbiggerthan10, lst)   
# for item in itemL:
#     print(item)

# itemL = filter(lambda i: i > 10, lst)  # 람다 함수로 필터링
# for item in itemL:
#     print(item)  # 15, 20, 30 출력


#democlass 
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "Default Name"
    def print(self):
        print(f"my name is {self.name}")
        
        
p1 = Person()
p2 = Person()
p1.name = "Alice"
p1.print()
p2.print()