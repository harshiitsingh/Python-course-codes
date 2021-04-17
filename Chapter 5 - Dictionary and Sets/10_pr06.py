favLang = {}
a = input("Enter your favorite language Harshit\n")
b = input("Enter your favorite language Ayushi\n")
c = input("Enter your favorite language Harsh\n")
d = input("Enter your favorite language Harshita\n")
favLang['Harshit'] = a
favLang['Ayushi'] = b
favLang['Harsh'] = c
favLang['Harshita'] = d
print(favLang)

# What happens if two keys or here two names will be same? --> then the later value will be taken as updated 
# What happens if two values or here two languages will be same? --> nothing happen
 
# S = {8,7,12,"Harry",[1,2]} --> throws error coz an unhashable or changeable element is present i.e., list
# S = {8,7,12,"Harry",(1,2)} --> correct , as tuple is present which cant be changed neither set can be changed