class SimpleClass:
    name = "This is simpleClass"
    
    def info(self):
        return "Info Call "+self.name

s = SimpleClass()
print s.name
print s.info()

print SimpleClass.info(s)
