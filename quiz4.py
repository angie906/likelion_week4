def add(a,b):
    print(f"{a}+{b}={a+b}")

def sub(a,b):
    print(f"{a}-{b}={a-b}")

def mul(a,b):
    print(f"{a}*{b}={a*b}")

def div(a,b):
    print(f"{a}/{b}={a/b}")

while(1):
    command=input("원하는 숫자를 입력하세요. 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 종료")

    if command=='5':
        print("종료합니다.")
        break

    a=int(input("숫자 1을 입력하세요."))
    b=int(input("숫자 2를 입력하세요."))

    if command=='1':
        add(a,b)
    elif command=='2':
        sub(a,b)
    elif command=='3':
        mul(a,b)
    elif command=='4':
        div(a,b)