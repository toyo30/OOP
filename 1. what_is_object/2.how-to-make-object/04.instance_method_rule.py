#객체 지향 함수는 속성과 행동이있다.

#python에서 속성은 변수로 나타낸다. 
#행동은 함수로 나타낸다. 이를 메소드라고 한다. 

#매소드에는 
# 인스턴스 매소드, 클래스 메소드, 정적 메소드가 있다. 


#인스턴스 메소드는 
#인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드 

class User:
    def say_hello(some_user):
        print("안녕하세요! 저는 {}입니다.".format(some_user.name))
    
    def login(some_user, my_email, my_password):
        #로그인 메소드
        if(some_user.email == my_email and some_user.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

user1 = User()


user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

User.say_hello(user1)
user1.say_hello()
#파라미터를 안 넘겨주었는데 왜 값이 생길까?

#인스턴스 매소드의 특별한 규칙 
#User.say_hello(user1)
#클래스에서 매소드를 호출함 

#user1.say_hello()
#인스턴스에서 매소드를 호출함
#인스턴스에서 매소드를 호출하면, 
# user1의 인스턴스가 say_hello()의 파라미터로 자동으로 전달됨.


#user1.say_hello(user1)
#인스턴스에서 매소드를 호출하고, 인스턴스를 다시 파라미터로 넘겨주면,
#TypeError: say_hello() takes 1 positional argument but 2 were given
#변수를 2개를 넘겨주었다고 뜬다. 이는 인스턴스 매소드의 특별한 규칙 때문이다. 
#User.say_hello(user1, user1)랑 완전히 같은 형태다.  
