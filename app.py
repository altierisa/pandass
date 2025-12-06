import pandas as pd
import os 

csv_path='sales.csv'

if not os.path.exists(csv_path):
    data=[{'date':'2025-12-01','product':'camisa','price':50,'quantity':2},
        {'date':'2025-12-01','product':'vestido','price':60,'quantity':2},
        {'date':'2025-12-01','product':'calça','price':100,'quantity':1},
        {'date':'2025-12-01','product':'bolsa','price':80,'quantity':2},
        {'date':'2025-12-01','product':'colar','price':25,'quantity':3},
        {'date':'2025-12-01','product':'aneis','price':15,'quantity':5},
        {'date':'2025-12-01','product':'oculos','price':50,'quantity':1},
        {'date':'2025-12-01','product':'sueter','price':70,'quantity':3},
        {'date':'2025-12-01','product':'bota','price':99,'quantity':2},
        {'date':'2025-12-01','product':'tenis','price':400,'quantity':1}
    ]
    
    df_example = pd.DataFrame(data)
    df_example.to_csv(csv_path,index=False)
    print('uhul criou',csv_path)

df= pd.read_csv(csv_path,parse_dates=['date'])
required={'date', 'product','price','quantity'}
if not required.issubset(set(df.columns)):
    print('as colunas estão erradas')

df['total']= df['price']*df['quantity']
df=[['total']].to_csv('total.csv',index=False)
print('Arquivo criado')