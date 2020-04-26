import wikipedia
from bs4 import BeautifulSoup
import re
import datetime
import csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg 

def show():
	x=[1,3,5,7]
	y=[18,15,17,8]
	plt.plot(x,y,color='r')
	#plt.show()
	plt.savefig('mydata.png',dpi=300)
	img = mpimg.imread('mydata.png') 
  # Output Images 
	plt.imshow(img) 
	return "ok"
#import schedule
#import time
'''
pat1='/wiki/2020_coronavirus_pandemic_'

pat2='/wiki/2019%E2%80%9320_coronavirus_pandemic_in_mainland_China'

pat3='/wiki/2020_coronavirus_pandemic_in_India'

x=datetime.datetime.now()
x=x.strftime('%x')
x=x.replace('/','')

tempname="mydata"+x

#def job():
content = wikipedia.page("Template:2019–20_coronavirus_pandemic_data").html()
soup=BeautifulSoup(content,"html.parser")
i=1

outfile=open(tempname+'.csv', 'w', newline='')
writer = csv.writer(outfile)
writer.writerow(["COUNTRY", "CASES", "DEATHS",'RECOVERED'])
temp=[]

for a in soup.find_all('a',href=True,text=True):
	if re.search(pat1,a['href']) or re.search(pat2,a['href']) or re.search(pat3,a['href']) :
		parent=a.parent
		if ' ' in a.string:
			a.string=a.string.replace(' ','')
		temp.append(a.string)
		if parent is not None:
			sibs=parent.find_next_siblings()
			for sib in sibs:
				if sib.string is not None:
					if ',' in sib.string:
						sib.string=sib.string.replace(',','')
						sib.string=sib.string.rstrip('\n')
					else:
						sib.string=sib.string.rstrip('\n')
					if sib.string.isdigit():
							temp.append(int(sib.string))
					else:
							temp.append(0)
		writer.writerow(temp)
		outfile.flush()  # flush() had no effect
		if i>60:
			break
		temp.clear()
	i=i+1
outfile.close()

		
df=pd.read_csv(tempname+'.csv',encoding="ISO-8859-1")


df.loc[df['COUNTRY'] == 'UnitedStates', 'COUNTRY'] = 'USA'
df.loc[df['COUNTRY'] == 'UnitedKingdom', 'COUNTRY'] = 'UK'
df.loc[df['COUNTRY'] == 'Germany', 'COUNTRY'] = 'Germ'
df.loc[df['COUNTRY'] == 'Netherlands', 'COUNTRY'] = 'Dutch'
df.loc[df['COUNTRY'] == 'Switzerland', 'COUNTRY'] = 'Swiss'
df.loc[df['COUNTRY'] == 'Belgium', 'COUNTRY'] = 'Belg'
df.loc[df['COUNTRY'] == 'Canada', 'COUNTRY'] = 'Cana'
plt.figure(figsize=(12,5))
plt.plot(df.COUNTRY,df.CASES,'r.-',label='CASES')
plt.plot(df.COUNTRY,df.DEATHS,'g.-',label='DEATHS')
plt.plot(df.COUNTRY,df.RECOVERED,'b.-',label='RECOVERED')

plt.xlabel('Countries')
plt.ylabel('Numbers')
plt.legend()
plt.show()


#schedule.every(2).minutes.do(job)

#while True:
#	schedule.run_pending()
#	time.sleep(1)
	
'''
