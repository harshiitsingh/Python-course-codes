# l = [i*7 for i in range(1, 11)] # for l to be used in join it should be string
# l = str([i*7 for i in range(1, 11)]) 
l = [str(i*7) for i in range(1, 11)]
print(l)

verticalTable = "\n".join(l)
print(verticalTable)