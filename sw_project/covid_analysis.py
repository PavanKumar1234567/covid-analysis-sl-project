import csv
import matplotlib.pyplot as plt
import numpy as np

with open("WHO-COVID-19-global-data.csv",'r') as fptr:
	creader=csv.reader(fptr,delimiter=",")
	final=[]
	listrep=[]
	for row in creader:
		s=row[:5]
		s.append(row[6])
		final.append(s)
		listrep.append(row)
# print(final)
completed=[]
cumlist=[]
c=0
for i in final[1:]:
	curcountry=i[2]
	if(curcountry in completed):
		continue
	cumdeaths=0
	cumcases=0
	for j in final:
		if(curcountry==j[2]):
			cumcases=cumcases+int(j[4])
			cumdeaths=cumdeaths+int(j[5])
	cumlist.append([curcountry,cumcases,cumdeaths])
	completed.append(curcountry)
	# print([curcountry,cumcases,cumdeaths])
	c=c+1
# print(cumlist)
# def sorted(l):
# 	l.sort(key=lambda k:k[1])
# 	return l
cumlist=sorted(cumlist,key=lambda k:k[1])
top3=cumlist[len(cumlist)-3:]

#writing top3 
towritelist=[]
for k in top3:
	for h in final:
		if(k[0]==h[2]):
			towritelist.append(h)

#print(towritelist)
with open("top3data.csv",'w') as w:
	cs=csv.writer(w)
	cs.writerows(towritelist)
####################### End of Preprocessing ###############################
####################Start of Global Data Processing ########################
listrep=[]
with open("top3data.csv") as fdescriptor:
	writer=csv.reader(fdescriptor)
	for row in writer:
		listrep.append(row)
# print(listrep)
p=['Brazil','India','United States of America']
countrywise=[]
for k in p:
	a=[]
	cumcases=0
	cumdeaths=0
	for x in listrep:
		if(x[2]==k):
			cumcases=cumcases+int(x[4])
			cumdeaths=cumdeaths+int(x[5])
			x.append(cumcases)
			x.append(cumdeaths)
			a.append(x)
	countrywise.append(a)
# print(countrywise)

# print(len(countrywise))
Brazil=countrywise[0]
India=countrywise[1]
usa=countrywise[2]
# print(Brazil)
brcumdeaths=[]
pies_brazil=[]
pies_india=[]
pies_usa=[]
x3=[]
y=[]
y1=[]
y2=[]
pie_brazil=[]
pie_india=[]
pie_usa=[]
temp=-1
m=0
index=0
prevcumdeaths=0
# print(len(x))
# print(len(y))
for i in Brazil:
	m+=1
	if(i[0] in ["2020-06-30","2020-12-31","2021-06-30","2021-12-31"]):
		x=i
		x[7]=x[7]-prevcumdeaths
		pies_brazil.append(x)
		pie_brazil.append(x[7])
		prevcumdeaths=i[7]

	if((m%150)==0):
		x3.append(i[0])
		y.append(i[6])
		temp=i[4]

m=0
x1=[]
prevcumdeaths=0
for i in India:
	m+=1
	if(i[0] in ["2020-06-30","2020-12-31","2021-06-30","2021-12-31"]):
		x=i
		x[7]=x[7]-prevcumdeaths
		pies_india.append(x)
		pie_india.append(x[7])
		prevcumdeaths=i[7]
	if((m%150)==0):
		x1.append(i[0])
		y1.append(i[6])
		temp=i[4]
m=0
prevcumdeaths=0
x2=[]
for i in usa:
	m+=1
	if(i[0] in ["2020-06-30","2020-12-31","2021-06-30","2021-12-31"]):
		x=i
		x[7]=x[7]-prevcumdeaths
		pies_usa.append(x)
		pie_usa.append(x[7])
		prevcumdeaths=i[7]
	if((m%150)==0):
		x2.append(i[0])
		y2.append(i[6])
		temp=i[4]

plt.figure(3)

plt.plot(x3,y,'g',label='Brazil')
plt.plot(x1,y1,'y',label='India', linewidth=1)
plt.plot(x2,y2,'c',label='USA', linewidth=1)
plt.title('line plot for top3 most effected countries.')
plt.ylabel('cases')
plt.xlabel('Date')
plt.legend()
plt.savefig("top3.png")

plt.figure(0)
b=np.array(pie_brazil)
# print(y)
mylabels = ["Jan 2020-Jun 2020", "Jul 2020-Dec 2020", "Jan 2021-Jun 2021", "Jul 2021-Dec 2021"]
myexplode = [0, 0, 0.2, 0]

plt.pie(b, labels = mylabels, explode = myexplode, shadow = True)
plt.savefig("pie_brazil")
# plt.show() 


plt.figure(1)
mylabels = ["Jan 2020-Jun 2020", "Jul 2020-Dec 2020", "Jan 2021-Jun 2021", "Jul 2021-Dec 2021"]
i=np.array(pie_india)
myexplode = [0, 0, 0.2, 0]
plt.pie(i, labels = mylabels,explode = myexplode, shadow = True)
plt.savefig("pie_india")

plt.figure(2)
mylabels = ["Jan 2020-Jun 2020", "Jul 2020-Dec 2020", "Jan 2021-Jun 2021", "Jul 2021-Dec 2021"]
u=np.array(pie_usa)
myexplode = [0, 0, 0, 0.2]	
plt.pie(u, labels = mylabels, explode = myexplode, shadow = True)
plt.savefig("pie_usa")

#male_female graph
brazil=[]
usa=[]
india=[]
lst=[]
with open("top3male_female.csv") as fdescriptor:
	writer=csv.reader(fdescriptor)
	for row in writer:
		if(row[0]=="USA"):
			usa.append(row)
		if(row[0]=="Brazil"):
			brazil.append(row)
# for i in usa:
# 	print(i)
# for i in brazil:
# 	print(i)
male_usa=0
female_usa=0
male_brazil=0
female_brazil=0
male_india=0
female_india=0
for i in usa:
	if(i[-2]!="NA"):
		male_usa=male_usa+int(i[-2])
	if(i[-1]!="NA"):
		female_usa=female_usa+int(i[-1])
for j in brazil:
	if(j[-2]!="NA"):
		male_brazil=male_brazil+int(i[-2])
	if(i[-1]!="NA"):
		female_brazil=female_brazil+int(i[-1])

# print(male_usa)
# print(female_usa)
# print(female_brazil)
# print(male_brazil)

total_usa=male_usa+female_usa
total_brazil=male_brazil+female_brazil

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

mu=np.array(male_usa)
fu=np.array(female_usa)
mb=np.array(male_brazil)
fb=np.array(female_brazil)

a=[]
b=[]

a.append(mu/total_usa)
a.append(mb/total_brazil)
b.append(fu/total_usa)
b.append(fb/total_brazil)

bar1 = np.arange(len(a))
bar2 = [i + barWidth for i in bar1]

plt.bar(bar1, a, color ='b', width = barWidth,label ='male')

plt.bar(bar2, b, color ='g', width = barWidth,label ='female')

plt.xlabel('countries', fontweight ='bold', fontsize = 20)
plt.ylabel('deaths', fontweight ='bold', fontsize = 20)

plt.xticks([kr + barWidth for kr in range(len(a))],['USA', 'BRAZIL'])
plt.legend()
plt.savefig("deaths_male_vs_female")
#############################END OF GLOBAL DATA ANALYSIS PART#####################
#############################START OF INDIA DATA ANALYSIS PART#####################
with open("covid_19_india.csv",'r') as reader:
	csv_reader_list=list(csv.reader(reader))
header=csv_reader_list[0]
sorted_data=sorted(csv_reader_list[1:],key=lambda y:y[3])
# print(header)
withactivelist=[]
for x in sorted_data:
	x[-1]=int(x[-1])
	x[-2]=int(x[-2])
	x[-3]=int(x[-3])
	x.append(int(x[-1])-(int(x[-2])+int(x[-3])))
	withactivelist.append(x)
# print(withactivelist[-10:])
header.append('active_cases')
state_data=[]
cur_state=[]
maxlist=[]

for i in range(len(withactivelist)-1):
	if(withactivelist[i][3]==withactivelist[i+1][3]):
		cur_state.append(withactivelist[i])
	else:
		state_data.append(sorted(cur_state,key=lambda h:h[1]))
		if(len(cur_state)>2):
			maxlist.append(state_data[-1][-1])
		cur_state=[]
temp=sorted(maxlist,key=lambda y:y[-2])[-3:]
top3affected=[]
for x in temp:
	top3affected.append(x[3])
# print(top3affected)
karnataka_data=[]
kerala_data=[]
Maharastra_data=[]
for i in state_data:
	if(len(i)<=2):
		continue
	if(i[0][3]==top3affected[0]):
		karnataka_data=i
	if(i[0][3]==top3affected[1]):
		kerala_data=i
	if(i[0][3]==top3affected[2]):
		Maharastra_data=i
# print(karnataka_data[:])
tem=0
for k in kerala_data:
	if(k[1]=='2020-03-09'):
		break
	tem=tem+1
kerala_data=kerala_data[tem:]
print(kerala_data[0])
print(karnataka_data[0])
print(Maharastra_data[0])

m=0
x=[]
y=[]
x1=[]
y1=[]
x2=[]
y2=[]

for i in karnataka_data:
	m+=1
	if((m%100)==0):
		x.append(i[1])
		y.append(i[-3])

m=0
for j in kerala_data:
	m+=1
	if((m%100)==0):
		x1.append(j[1])
		y1.append(j[-3])

m=0
for k in Maharastra_data:
	m+=1
	if((m%100)==0):
		x2.append(k[1])
		y2.append(k[-3])

plt.figure(5)
plt.plot(x,y,'g',label='Karnataka')
plt.plot(x1,y1,'y',label='Kerala',linewidth=1)
plt.plot(x2,y2,'c',label='maharastra',linewidth=1)

plt.title('line plot for top3 most effected states.')
plt.ylabel('cases')
plt.xlabel('Date')
plt.legend()
plt.savefig("top3states.png")

pies_kerala=[]
pies_karnataka=[]
pies_Maharastra=[]
prevcum=0
x=[]
for i in kerala_data:
	if(i[1] in ['2020-08-09','2020-12-30','2021-04-09','2021-08-09']):
		pies_kerala.append(i[-2]-prevcum)
		prevcum=i[-2]
print(pies_kerala)

plt.figure(7)
mylabels = ["Mar 2020-Jul 2020","Aug 2020-Dec 2020", "Jan 2020-April 2020", "May 2021-Aug 2021"]
u=np.array(pies_kerala)
myexplode = [0, 0, 0, 0.2]	
plt.pie(u, labels = mylabels, explode = myexplode, shadow = True)
plt.savefig("pie_kerala")
prevcum=0

for i in karnataka_data:
	if(i[1] in ['2020-08-10','2020-12-29','2021-04-10','2021-08-08']):
		pies_karnataka.append(i[-2]-prevcum)
		prevcum=i[-2]
print(pies_karnataka)

plt.figure(11)
mylabels = ["Mar 2020-Jul 2020","Aug 2020-Dec 2020", "Jan 2020-April 2020", "May 2021-Aug 2021"]
v=np.array(pies_karnataka)
myexplode = [0, 0, 0, 0.2]	
plt.pie(v, labels = mylabels, explode = myexplode, shadow = True)
plt.savefig("pie_karnataka")


prevcum=0
for i in Maharastra_data:
	if(i[1] in ['2020-08-10','2020-12-29','2021-04-10','2021-08-08']):
		pies_Maharastra.append(i[-2]-prevcum)
		prevcum=i[-2]
print(pies_Maharastra)

plt.figure(13)
mylabels = ["Mar 2020-Jul 2020","Aug 2020-Dec 2020", "Jan 2020-April 2020", "May 2021-Aug 2021"]
v=np.array(pies_Maharastra)
myexplode = [0, 0, 0, 0.2]	
plt.pie(v, labels = mylabels, explode = myexplode, shadow = True)
plt.savefig("pie_Maharastra")