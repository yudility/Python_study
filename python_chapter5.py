#파이썬 5차시 - 조건문, 반복문

#조건문과 관계연산자 
"""관계연산자"""
a = 3645
b = 3645
c = 274

print(a < c)
'''False'''
print(a == b) #두 변수에 저장된 값을 비교
'''True'''
print(a is b) #두 변수가 가리키는 주소가 같은지 비교. 
'''False'''
print(a <= b)
'''True'''
print(( a > b ) > c ) # False> c --> 0 >274 // False는 0으로 취급
'''False'''
print( (a==b) == 1) #True == 1  --> 1 == 1
'''True'''


"""논리연산자"""
#and / or / not

t = True
f = False
var1 = 8
var2 = 5
var3 = 0
empty_list = []

print(t, 'AND', not(f), 'is', t and not(f),'.' ) 
'''True AND True is True .'''

print('NOT(',t,') is', not t,'.')
'''NOT( True ) is False .'''

print(( var1 == 8 ) and ( var2 == 4 )) #false
print(( var1 > 7 ) or ( var2 > 7 )) #true

print(var3, 'is', bool(var3),'.') # 0은 false
print(var1, 'is', bool(var1),'.') # 0이외의 정수는 true
print('Empty list is', bool(empty_list),'.') #빈 리스트는 --> false

"""조건문"""
# : 조건에 따라 특정 동작을 실행하도록 한다.(들여쓰기!)

if var1 < 10: #조건이 참일 때 
    print("10보다 작습니다.") #동작
else : #조건이 거짓일 때
    print("10보다 큽니다.") #동작하지 않음


#조건이 3개 이상인 경우
score = 96
if score >= 90 :
    print("합격입니다.")
    print("장학금도 지급됩니다!")
elif score >= 60 :
    print("합격입니다.")
else:
    print("불합격입니다.") 

'''조건의 순서를 맞춰야한다. 논리에러가 발생할 수 있다.
   중첩된 조건문도 가능(if문 안에 if문)'''


#반복문 - for문, while문
"""for문 : 반복범위를 지정하여 반복 수행"""
# for i in range(start=0, stop, step=1):

for i in range(1,4): #1부터 3까지 세 번 반복
    print(i)
for i in range(3): #0부터 2까지 세 번 반복
    print(i)
for i in range(1,6,2): #1,3,5만 반복
    print(i)
#for 변수 in [리스트] // 리스트 개수만큼 실행

for i in ['c', 'python', 'go']:
    print(i + " Rocks!")

"""while문 : 조건을 지정하여 반복을 수행. 조건이 거짓이되면 수행 멈춤"""
i=1
while i<4:
    print(i)
    i = i+1 #while 문의 경우 i가 증가하는 코드를 써줘야한다. 안그럼 무한 루프

#중첩된 반복문. 
for i in range(2, 10):
    print("[",i,"단]")
    for j in range(1, 10):
        print( i,'x', j,'=', i*j)
    print()

'''들여쓰기 유의하자'''

#5강 학습활동
import random

def Get_number() :
    return random.randint(1, 10)

x = Get_number()
type(x)
i=1
while i == 1:
    u_number = int(input("Guess the number!: "))
    if x == u_number:
        print("Correct! The number is", x, "!")
        i =0
    elif x < u_number:
        print("It's less than that. Try again.")
    else:
        print("It's more than that. Try again.")


