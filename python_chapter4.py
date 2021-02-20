#print 사용
var1 = 100
var2 = "Hello!"
var3 = "Hi, i\'m yudility.\t"
var4 = "Hi, i\'m yudility.\n"
#\뒤에 특수문자 쓰면 특수문자 그대로 출력가능

unit = '원'
print(var1)
print(var2)
print(var3)
print(var4)
print(var1, unit) 
print(str(var1)+ unit) 
"""문자형간의 +는 붙이기를 의미
+는 자료형을 같게 바꿔야 함."""

#리스트
p_list = [2,5,8,9]

print(p_list[0]) #인덱스는 0부터 시작
print(p_list[2])
print(len(p_list)) #len()함수는 리시트의 크기를 반환한다.
p_list[1] = 3 #리스트 원소값 변경하기

print(p_list)

#사용자 입력과 출력 input(), print()
input("이름을 입력하세요: ") #표준 입력 함수. 프롬프트 함수이다. 
'''반환형은 무조건 문자열이다. 
연산을 하고 싶다면 형변환을 해주어야한다. 입력결과도 출력해준다.'''

name = input("이름을 입력하세요: ")
print("Hi! ", name,". Nice to meet you.")

var6= input("Please input the first integer. : )
var7= int(input("Please input the second integer. : ))
'''반환형은 무조건 문자열이다. 
연산을 하고 싶다면 형변환을 해주어야한다. 입력결과도 출력해준다.'''
type(var6); type(var7)

print("줄바꿈은"); print("기본입니다."); #각 print문은 자동 줄바꿈이다. 
print("Welcome", 2021) # 여러값을 출력하는경우 ,를 사용
print("줄바꿈을 안할때는", end=''); print("이렇게 합니다.")


#함수(어떤 기능을 수행하는 코드 묶음)
""" def 함수 이름 (매개변수1, ...): ... return 반환값 """
def Hypo (bottom, height) : 
    hypotenuse = 0
    hypotenuse = (bottom **2 + height**2) **0.5
    return hypotenuse

result = 0
result =Hypo(3, 4)
print("두 변의 길이가 3과 4인 삼각형의 빗변의 길이는", result, "입니다.")


#사칙연산 프로그램만들기
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

def Add(num1,num2):
    add = num1 +num2
    return add

def Sub(num1,num2):
    sub = num1 -num2
    return sub

def Mul(num1,num2):
    mul = num1 *num2
    return mul
 
def Div(num1,num2):
    div = num1 /num2
    return div

print("Result is...")
print(" Add:", Add(num1,num2))
print(" Sub:", Sub(num1,num2))
print(" Mul:", Mul(num1,num2))
print(" Div:", Div(num1,num2))

