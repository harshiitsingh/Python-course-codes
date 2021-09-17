# Write a program mine a log file and find out whether it contains 'python'

# google --> log file stackoverflow
            # https://stackoverflow.org/wiki/Log
# google -> sapme log file --> ibm


# work/use of log/logs/log files :
# jb bhi aapki application chal rhi ho aap yahan apne logs daal skte ho application ki
# jisse aapko pta chal jaega ki aap ki application kya kr rhi about debug/error etc msgs at different times.

with open("ques 6 log.txt") as f:
    content = f.read() 
    # or
    # content = f.read().lower() 

if 'python' in content.lower(): # check line 23 in text file
    print("Yes python is present")
else:
    print("No python is not present")