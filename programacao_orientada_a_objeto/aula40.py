# Metaclasses são o tipo das clases 

# class Foo:
#     ...


Foo = type('Foo', (object,),{})
f = Foo()
#print(isinstance(f,Foo))
print(type(f))
print(type(Foo))

