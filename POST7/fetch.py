import os,sys,time,re

D=r'C:\Program Files\Adem71\ncm\POSTPR'

#os.system('git checkout *.pst')

for i in os.listdir(D):
    if re.match(r'^(.+(0888|0999|6000|1210).+|STANKI\.SKR)$',i):
        print D,i,'->',i
        S=open(r'%s\%s'%(D,i),'rb')
        T=open(i,'wb')
        T.write(S.read())
        S.close()
        T.close()

raw_input('.')
