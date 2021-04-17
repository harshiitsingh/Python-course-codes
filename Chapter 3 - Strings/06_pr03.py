st = "This is a string with double  spaces    ok  ."
st1 = "This is a string with double spaces"

doubleSpaces = st.find("  ")
doubleSpaces1 = st1.find("  ")
print(doubleSpaces)
print(doubleSpaces1)

# not proper way to check double spaces 
# can also be done by if else statement 

# Q 4
st = st.replace("  "," ")
print(st)

# loop