def checkKey(dict, Key):

    if key in dict.keys():
        print("Present, ", end =" ")
        print("value =", dict[key])
    else:
        print("Not present")


dict = {'a': 100, 'b':200, 'c':300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)
