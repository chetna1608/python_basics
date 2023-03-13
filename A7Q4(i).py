'''
def func1():
                l1 = list()
                l2 = list()
                for i in range(0,5):
                                l1.append(i)
                                l2.append(i+3)
                print(l1)
                print(l2)
                '''
def func2():
                l3 = list()
                l4 = list()
                for i in range(0,5):
                                l3.append(i)
                                l4.append(i+3)
                                l3,l4=l4,l3
                print(l3)
                print(l4)

func2()

