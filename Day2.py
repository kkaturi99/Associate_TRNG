# x=5
# def func(a):
#     return a + x  # x는 전역 변수

# print(func(10))  # 15 출력
# def func2(a):
#     x =  10  # x 값을 변경
#     return a + x  # x는 지역 변수

# print(func2(10))  # 20 출력


#키워드 인자
def connectURL( server="www.naver.com", port="1717"):   #디폴트값 설정해둠
    strURL = "https://" + server + ":" + port
    print(strURL)
    

connectURL("www.example.com", "8080") # https://www.example.com:8080 출력
connectURL(port="8080", server="www.example.com") # https://www.example.com:8080 출력
connectURL() # https://www.naver.com:1717 출력
