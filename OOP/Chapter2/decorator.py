# decorator

def copyright(func):

    def new_func():
        print("@ amamov")
        func()

    return new_func

@copyright 
def smile():
    # print("@ amamov")
    print(" π ")

@copyright 
def angry():
    # print("@ amamov")
    print(" π‘ ")

@copyright 
def love():
    # print("@ amamov")
    print(" π ")


# smile = copyright(smile)   # κ΅³μ΄ ν¨μλ₯Ό μ¬μ μ ν΄μΌνλκ°? μ λν λΆνΈν¨μΌλ‘ -> @copyright 
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()