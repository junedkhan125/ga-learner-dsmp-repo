# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = (data['int.rate'].str[:-1]).astype('float64')

data['int.rate'] = data['int.rate'] / 100
z_statistic, p_value = ztest(data[ data['purpose']=='small_business']['int.rate'] ,value= data['int.rate'].mean()  ,alternative='larger')

if p_value < 0.05:
    inference='Reject'
else:
    inference = 'Accept'

print('Z = ',z_statistic)
print('p_value = ',p_value)
print(inference)



# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest
import matplotlib.pyplot as plt
import seaborn as sns
#Code starts here

z_statistic, p_value = ztest( data[ data['paid.back.loan'] == 'No' ]['installment'], 
                               data[ data['paid.back.loan'] == 'Yes' ]['installment']  
                            )

print('Z statistic ',z_statistic)
print('P value  ',p_value)

if p_value < 0.05:
    inference ='Reject'
else:
    inference ='Accept'

print(inference)



# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes' ]['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No' ]['purpose'].value_counts()

observed= pd.concat([yes.transpose(),no.transpose()],axis=1, keys=['Yes','No'])
print(observed)

chi2, p, dof, ex = chi2_contingency(observed)

print('Chi 2 ',chi2)
print('critical_value  ',critical_value)

if chi2 > critical_value :
    inference ='Reject'
else:
    inference = 'Accept'

print(inference)



# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data = pd.read_csv(path)

data_sample = data.sample(n=sample_size,random_state=0)

sample_mean = data_sample['installment'].mean()

sample_std = data_sample['installment'].std()

margin_of_error = z_critical * ( sample_std / math.sqrt(sample_size) )

confidence_interval = [ sample_mean - margin_of_error , sample_mean + margin_of_error  ]

true_mean = data['installment'].mean()

print('confidence_interval = ',confidence_interval)
print('true mean ',true_mean)


# --------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig,axes = plt.subplots ( 3,1)

for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        m.append( (data.sample(n=sample_size[i],random_state=0))['installment'].mean()) 
    mean_series = pd.Series(m)
    axes[i].hist(mean_series)
    axes[i].set_title('Mean of sample with '+str(sample_size[i]))

plt.tight_layout()
plt.show()        


