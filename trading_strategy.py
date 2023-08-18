import numpy as np

pro=[]
ln=10000
day=5
for j in range(ln):
    initial_investment=10000
    #for 5 day 
    for i in range(day):
        # 0.3 is my target price and -0.3 is my stop loss
        # 0.6 is winning probability of the strategy and 0.4 is loss probability
        # get winning probability from paper trade or from privious trade using certain strategy, 
        # like if you get 6 winning trade out of 10 then my winning probability is 0.6%
        x=np.random.choice([0.3,-0.3],p=[0.6,0.4])   

        # lot_price is price of 1 lot of bank nifty
        # uniform(4000,8000) means that lot price can be anything in between 4000 to 8000
        lot_price=np.random.uniform(4000,8000)

        # lot is no. of lot you can get base on fund, you have and the lot price
        # initialy fund is 10000 then it's depend upon profite and loss
        lot=initial_investment//lot_price
        if lot==0: #if there is not sufficient fund 
            break
        # fund after the trade    
        initial_investment=initial_investment+lot*lot_price*x
    pro.append(initial_investment)




z=[i for i in pro if i >10000]  #give no. of trade close more then 10000 out of 10000
print('profit probability = ',(len(z)/ln)*100)
print('median : ',np.median(pro))
print('mean : ',np.mean(pro))
print('max : ',max(pro))
print('min : ', min(pro))
import matplotlib.pyplot as plt
plt.hist(pro,bins=50)
#plt.boxplot(pro)
plt.show()
