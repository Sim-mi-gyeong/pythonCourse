# decorator

def copyright(func):

    def new_func():
        print("@ amamov")
        func()

    return new_func

@copyright 
def smile():
    # print("@ amamov")
    print(" 😀 ")

@copyright 
def angry():
    # print("@ amamov")
    print(" 😡 ")

@copyright 
def love():
    # print("@ amamov")
    print(" 😍 ")


# smile = copyright(smile)   # 굳이 함수를 재정의 해야하는가? 에 대한 불편함으로 -> @copyright 
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()