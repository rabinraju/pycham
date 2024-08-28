class animal():
    def sound(self):
        print("animal makes sound")


class dog(animal):

    def sound(self):
        print("dog is bitting")


a1 = dog()
a1.sound()
# polymorfisom,the word of polymorfisom is having many form,
# in programing polymorfism is same function but diffrent signature
# a ,b,c is parameter,argument
def add(a, b, c):
    print(a + b + c)
add(10, 11, 11)


class animal():
    def sound(self):
        print("animal macks sound")


class dog(animal):
    def sound(self):
        print("dogs brocks")


class bird(dog):
    def sound(self):
        print("birds sing")


b1 = bird()
b1.sound()
