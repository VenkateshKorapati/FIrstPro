fname=input('Enter File Name:')
f=open('D:\\Sivagang.xlsx\\'+fname,'w')
feedback=input('Enter your valuable feedback')
f.write(feedback)
f.close()
