#   The subject marks are in out of 100, hence no need to convert it into % 

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You are fail because you have less than 33% in one of the subject.")
# else:
#     if(sub1+sub2+sub3)/3 <40:
#         print("You are fail due to total percentage less than 40.")
#     else:
#         print("Congratulations! You are passed!")

# HARRY'S METHOD
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subject.")
elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage less than 40.")
else:
    print("Congratulations! You are passed!")