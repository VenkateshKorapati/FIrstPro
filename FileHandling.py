fname=input('Enter File Name')
f=open('D:\\Python\\'+fname,'w')
feedback=input('Enter Feedback Data')
f.write(feedback)
f.close()
