class Account:
    num_account=0
    def __init__(self,name):
            self.name=name
            Account.num_account +=1


kb = Account("KB")
woori = Account("WOORI")

print kb.name
print woori.name
    
print Account.num_account