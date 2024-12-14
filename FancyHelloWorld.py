import os, time
symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','y','z', ' '] #symbols you wanna use
result = "hello world" #target word
current = ""
while current != result:
    for char in result:
        for symbol in symbols:
            print(current + symbol)
            time.sleep(0.05)
            os.system('cls')
            if symbol == char:
                current = current + symbol
                break
print(result)
