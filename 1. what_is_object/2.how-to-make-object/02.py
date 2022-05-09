class User:
    pass

user1 = User()
user2 = User()
user3 = User()
user4 = User()


user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

#인스턴스 변수 

print(user1.email)

print(user2.age)


#객체만 생성해놓으면, class 안에 속성을 넣어놓지 않아도, 해당 객체에 속성이 부여된다. 
#인스턴스 변수를 사용하기 위해서는 그 전에 속성값을 꼭 정의해놓아야한다. 