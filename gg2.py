#file = open ("new.txt", "x")
#file.close()

file = open ("new.txt", "w")
file.write("to be or not to be that is the question ")
file.close()

file = open ("new.txt", "r")
print(file.read())
file.close()

answer = input("who is the author?")

file = open ("new.txt", "a")
file.write('\n' + answer)
file.close()
answer = input("who is the author?")

file = open ("new.txt", "a")
file.write('\n' + answer)
file.close()

answer = input("who is the author?")
file = open ("new.txt", "a")
file.write('\n' + answer)
file.close()


run = True
while run:
    file_name = input("enter file name")+".txt"
    try:
        with open(file_name, "r") as file:
            print(file.read())
        run = False
    except:
        print("file not found")