# Your code goes here:
def render_person(*param):
    return param[0]+" is a "+str(param[3])+" years old "+param[4]+" born in "+param[1]+" with "+param[2]+" eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))