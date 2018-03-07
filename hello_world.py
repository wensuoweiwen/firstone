
def demo_controlflow():
    score=65
    if score>99:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print 3,'C'
    while score<100:
        print score
        score+=10

demo_controlflow()

def demo_list():
    lista=[1,2,3]
    print 1,lista
    listb=['a',1,'c',1.1]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4,'a' in lista
    print 5, lista+listb
    listb.insert(0,'www')
    print 6, listb
    listb.pop(1)
    print 7, listb
    print 8,lista[0]
    listb.sort(reverse=True)
    print 9,listb
    listb.sort(reverse=False)
    print 10, listb
    tuplea=(1,2,3)
    listaa=[1,2,3]
    listaa.append(4)
    print 11, listaa

demo_list()

def demo_dict():
    dicta={1:1,2:4,3:9}
    print 1,dicta
    print 2, dicta.keys(),dicta.values()
demo_dict()