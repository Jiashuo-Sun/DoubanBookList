import os
import pandas as pd

def cleanlink(url):
    url = url.split('?')[0]
    url = url.split('/')[:5]
    return('/'.join(url)+'/')

def cleanBookName(name):
    cleanName = name.split('(')[0]
    cleanName = cleanName.split('（')[0]
    return(cleanName)

if __name__ == '__main__':
    datapath = os.path.join(os.path.dirname(os.getcwd()),'data/')
    bookinfo = pd.read_csv(datapath+'BookInfoSet.csv', names = ['isnb','name','author','Avg','Num','URL','date'])
    print('Totle\t  '+str(len(bookinfo)))

    cleanData = bookinfo.drop(['isnb', 'URL','date'], axis = 1)
    cleanData.dropna(subset = ['Avg','Num'], inplace = True)
    cleanData.reset_index(drop = True, inplace = True)
    cleanData['name'] = cleanData['name'].apply(cleanBookName)
    # cleanData['date'] = cleanData['date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').date())

    print(cleanData['name'].describe()[:2])
    CleanBookInfo = cleanData.sample(0)
    
    for i in range(len(cleanData)):
        if cleanData.iloc[i]['name'] in CleanBookInfo['name'].values:
            reviewnum = CleanBookInfo['Num'][CleanBookInfo['name'] == cleanData.iloc[i]['name']] + cleanData.iloc[i]['Num']
            reviewavg = (CleanBookInfo['Avg'][CleanBookInfo['name'] == cleanData.iloc[i]['name']] * CleanBookInfo['Num'][CleanBookInfo['name'] == cleanData.iloc[i]['name']] + cleanData.iloc[i]['Avg'] * cleanData.iloc[i]['Num']) / reviewnum
            CleanBookInfo['Num'][CleanBookInfo['name'] == cleanData.iloc[i]['name']] = reviewnum
            CleanBookInfo['Avg'][CleanBookInfo['name'] == cleanData.iloc[i]['name']] = reviewavg
        
        else:
            CleanBookInfo = CleanBookInfo.append(cleanData.iloc[i])

    CleanBookInfo.to_csv(datapath+'CleanBookInfo.csv', index = False, header = False)
