def file_parser():
    print(os.getcwd())
    allfiles = []


try:
    for path, _, file in os.walk(top=parentroot, topdown=True):
        allfiles += [path + '/' + l for l in file if
                     l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
except:
    print('Can not open folder oop-master')
    return list([])
return allfiles


def filesbycategory():
    counter = {'cpp': 0, 'hpp': 0, 'h': 0, 'c': 0}
    starttime = time()
    for x in files:
        if re.match('.+\.cpp$', x):
          # if x.endswith('.cpp'):
            counter['cpp'] += 1
        elif x.endswith('.hpp'):
            counter['hpp'] += 1
        elif x.endswith('.h'):
            counter['h'] += 1
        else:
            counter['c'] += 1

    for key in counter:
        print(str(key) + '-->' + str(counter[key]))
    endtime = time()
    print('Lapsed Time:' + str(endtime - starttime) + ' s')

starttime=time()
    linecounter=0
    for i in files:
        with open(i,'r',encoding="utf-8",errors='ignore') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    tm.cprint('Lines of code:'+str(linecounter),'red')
    tm.cprint('Elapsed Time for finding all lines of code:'+str(time()-starttime)+'\'s','red')

def equality_statements():
    def equality_statements():
    counter=0
    fls=[]
    pattern=re.compile('\s+if\s*\(\s*.+\s*==\s*.+\)|^if\s*\(.+==.+\)|.*if\s*\(\s*\w+\s*\)')
    patternB=re.compile("\s*if\s*\(\s*\w+\s*\)")
    #|if\s*\(\s*(\w|\d)+\s*\)
    #if\s*\(\s*(\w|\d)+\s*\)-->if(k) αν k είναι boolean μεταβλητή η ένας αριθμός
    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as f:
            #counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
            for k in f:
                print(patternB.findall(k))
                fls+=pattern.findall(k)
                fls+=patternB.findall(k)
    tm.cprint('\t If equality Statements found','blue')
    tm.cprint('==='*30,'red')
    id=1
    for k in fls:
        k=k.replace(' ','').replace('\t','')
        #k=k.strip()
        tm.cprint(str(id)+'.'+str(k),'green')
        id+=1
    print('\n\n')
    return len(fls)
import sys
sys.path.append('..')
import file_walk as fw
import re
import os
import termcolor as tm

#Χρήση custom module file_walk:[https://github.com/vasnastos/Assignment_AGP/blob/master/file_walk.py]
#Απαραίτητος ο φάκελος oop-master
files=fw.file_parser()

def over_12_characters():
    found=0
    print(len(files))
    #for regex
    pattern=re.compile('\s*for\s*\(\s*.*\s*;\s*.*\s*;\s*.*\s*\)|\s*for\s*\(\s*.+[:]\s*.+\s*\)')
    for x in files:
        with open(x,'r',encoding='ISO-8859-1') as f:
           for k in f:
               for l in pattern.findall(k):
                   tm.cprint(l,'red')
                   current=l[int(l.find('('))+1:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         tm.cprint(current,'green')
                         found+=1
                   print('')
    print(f'for loops with over 12 characters:{found}')

#Test σε αρχείο sample.cpp
def tester():
    found=0
    pattern=re.compile('for\s*\(.+;.+;.+\)|for\s*\(.+[:].+\)')
    with open("sample.cpp",'r',encoding='utf-8') as L:
        for x in L:
            for l in pattern.findall(x):
                   tm.cprint(l,'red')
                   current=l[int(l.find('for('))+4:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         tm.cprint(current,'green')
                         found+=1
                   print('')
    print(f'for loops with over 12 characters:{found}')

#Περίπτωση με εύρεση kαι inline εντολών for
#split based for
def tester1():
    found=0
    pattern=re.compile('\(.+;.+;.+\)|\(.+[:].+\)')
    with open('sample.cpp','r') as f:
        for x in f:
            data=[]
            if 'for' in x:
                data=x.split('for')
            if len(data)==0:
                continue
            for k in data:
               if pattern.match(k):
                   tm.cprint(k,'red')
                   for m in pattern.findall(k):
                       fixed=m[m.find('(')+1:len(m)-1]
                       fixed=fixed.strip().replace(' ','')
                       if len(fixed)>=12:
                           tm.cprint(len(fixed),'yellow')
                           tm.cprint(fixed,'green')
                           found+=1
               tm.cprint('============================================================','white')
        tm.cprint(f'Matches Found:{found}','blue')

over_12_characters()
#tester()
#tester1()