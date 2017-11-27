import pickle
from parse_out_email_text import parseOutText
word_data=[]
sham=[]
fh=open('spam.txt','r')
for line in fh:
	#print len(sham)
	sms=line.split(',')
	data=parseOutText(sms[1])
	if data!=None:
		word_data.append(data)
		if sms[0]=='spam':
			sham.append(0)
		else:
			sham.append(1)
fh.close()
#print sham
print len(sham)
print len(word_data)

pickle.dump( word_data, open("sms.pkl", "w"))
pickle.dump( sham, open("sham.pkl", "w"))

