def lt(x,y):
    return x< y

def le(x,y):
    return x <= y

def mt(x,y):
    return x > y

def me(x,y):
    return x >= y



def satisfaction(satis,cont,fun):
    for sat in satis:
        for con in cont:
            if con[2]=='<=':
                op = le
            elif con[2] == '<':
                op = lt
            elif con[2] == '>':
                op = mt
            elif con[2] == '>=':
                op = me
            if op(con[0]*sat[0] + con[1]*sat[1],con[3]):
                can = True
            else:
                can = False
                break
        if can:
            print(sat,' ',True,fun[0]*sat[0] + fun[1]*sat[1])
        else:
            print(sat,' ',False)


print(satisfaction([[1,4],[2,2],[3,1.5],[2,1],[2,-1]],
    [[6,4,'<=',24],[1,2,'<=',6],[0,1,'<=',2],[-1,1,'<=',1],
        [1,0,'>=',0],[0,1,'>=',0],[1,0,'<=',2.5]], [5,4]))
