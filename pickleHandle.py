'''
    use with statement
'''

try:
    with open('read.txt',mode='w',encoding='utf-8') as f:
        f.write('\n test write with statement')

    with open('read.txt',mode='r',encoding='utf-8') as f2:
        print(f2.read())
        print(f2)

    #pickle
    import pickle

    with open('test.pickle', mode='wb') as pf:
        lis =['one','two','three']
        dics = {'tom':'111-111-1111','james':'222-222-2222'}
        tups = (lis,dics)
        pickle.dump(tups,pf)
        pickle.dump(lis,pf)


    with open('test.pickle', mode='rb') as pf2:
        objlist = pickle.load(pf2)
        print(len(objlist))
        print(len(objlist[0]))
        print(len(objlist[1]))
        #print(objlist[0])
        #print(objlist[1])
        #print(objlist[2])

        objlist = pickle.load(pf2)
        print(len(objlist))

except Exception as e:
    print(e)



