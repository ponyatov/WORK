import os,sys,time,re

D=r'C:\Program Files\Adem71\ncm\POSTPR'

for i in os.listdir(D):
    if re.match(r'.+(0999|1210)\..+',i):
        print D,i,'->',i
        S=open(r'%s\%s'%(D,i),'rb')
        T=open(i,'wb')
        T.write(S.read())
        S.close()
        T.close()
for i in ['STANKI.SKR']:
        print D,i,'->',i
        S=open(r'%s\%s'%(D,i),'rb')
        T=open(i,'wb')
        T.write(S.read())
        S.close()
        T.close()
    
raw_input('.')
