# file = open('my_file.txt') # while opening the file need to close because of the resources it stores, but everytime it is hard to remember to whether it is close or not so for that solution we will use with , use of with will also help to make the file even if it is not exists

# contents = file.read()
# print(contents)

# file.close()


# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)



with open('new_file.txt',mode = 'a') as file:
    file.write('\n New Text')
