import matplotlib.pyplot as plt

x=[2,4,6,8]
y=[6,7,8,2,4]

x2=[1,3,5,9,11]
y2=[7,8,2,4,2]

population_ages=[22,55,62,45,21,22,34,44,42,53,3,45,56,122,24,45,65,110,17,100,106]
#ids=[x for x in range(len population_ages)]

bins=[0,10,20,30,40,50,60,70,80,90,100,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)



##plt.bar(x,y,label='Bar1',colour='r')
##plt.bar(x,y,label='Bar2',colour='c')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
