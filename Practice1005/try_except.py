
'''
catchblocks can be great, 
but if you run the code without them,
the editor will show you where exactly the problem lies
'''
try:
    a = 1
    b = 2
    c = "donuts"

    print('created vars')
    
    d = a + b
    print(d)

    print('printed d')

    e = a + c # error
    print(e)

    print('printed e')
except Exception as error:
    # handle exception
    print("BOO! there was an error")
    print(error)
else:
    # handle success
    print("YAY! there was no error")
finally:
    # always execute regardless of exception or success
    print("donuts are yummy!")