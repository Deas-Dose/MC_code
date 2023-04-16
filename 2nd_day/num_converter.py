# a: roman to number converter, b: roman number in the function, c: the output of func a, d: each number in b, e: real roman number to be converted, f: number to convert to roman
# g: the string to print, z: map for roman numbers, r: reverse order of z

# code explanation:
# get the inputs
f,e=int("1800"),"MMMDCCXXIV".split('/')
# a map for roman numbers in latin, note that the 9s and 4s are mandatory because there isn't another "simple" way to get them with code
z={'M':1000,"CM":900,'D':500,"CD":400,'C':100,"XC":90,'L':50,"XL":40,'X':10,"IX":9,'V':5,"IV":4,'I':1}
# a map for latin numbers in roman
r={v:k for k,v in z.items()}
# initialising a list to store the outputs
g=["",0]

# convert numbers to roman, first load each key-value pair from the map into a variable
for x in r:
    # keep looping while the number to convert is bigger than any key in the map
    while f>=x:
        # this can be done in 2 ways afaik but this is just shorter
        # always add the map key if it's smaller than the actual value to the result
        g[0]+=r[x]
        # substract what we added from the number to convert
        f-=x

# this function should convert roman to latin numbers
def a(b):
    # initialise an empty variable
    c=0
    # loop through the length of the roman number
    for i in range(len(b)):
        # check if the index is bigger than the length of the roman number to not go beyond, and also check if the value of the key in the roman number is the same or bigger than the next letter to not miscalculate stuff
        # the first condition will return false at the end of the calculations
        # the second condition is what will make the code add up numbers
        if i+1!=len(b) and z[b[i]]<z[b[i+1]]:
            # substract the value from the result because it will corrupt the calculations with wrong numbers
            c-=z[b[i]]
        else:
            # this is just a "not" version of the above condition
            c+=z[b[i]]
    # return the result in string so that we can make a full string out of the result
    return str(c)

# Join the numbers gotten from the above function, the "/" is because the tests where made on a date and not on a normal number
g[1]="/".join(a(d) for d in e)
# return the whole results (roman to latin and the reverse)
print(" ".join(g))
