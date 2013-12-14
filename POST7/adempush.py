import os,sys,time,re

D=r'C:\Program Files\Adem71\ncm\POSTPR'

NOW = '%.4i%.2i%.2i%.2i%.2i%.2i'%time.localtime()[:6] ; print NOW

for C in [
r'copy "%s\STANKI.SKR" "%s\STANKI.SKR.%s"'%(D,D,NOW),
r'copy STANKI.SKR "%s\"'%D,
r'copy *.ank "%s\"'%D
]:
    print C
    print os.system(C)
    
raw_input('.')
