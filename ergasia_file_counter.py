
import re
import os

from time import time
start_directory = "C:/Users/nikde/Documents/oop-master"

files = []
try:
   for path, _, file in os.walk(start_directory, topdown=False):

       files += [path + '/' + l for l in file if
       l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
except:
    print('Can not open folder oop-master')
    print(list([]))
print(files)
#1!!!!!!!!!!!!!!!!!!!!!!!!!
def filesbycategory():

    counter = {'cpp': 0, 'hpp': 0, 'h': 0, 'c': 0}
    starttime = time()

    for x in files:
        if x.endswith('.cpp'):
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
filesbycategory()

#2!!!!!!!!!!!!!!!!!!!!!!!!!!
def alllines_function():
    starttime=time()
    linecounter=0
    for i in files:
        with open(i,'r',encoding="utf-8",errors='ignore') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    print('Lines of code:'+str(linecounter))

    print('Elapsed Time for finding all lines of code:' + str(time()-starttime) + ' s')
alllines_function()

#3!!!!!!!!!!!!!!!!!!!!!!!
def symbols_letters_digid():
    parser={'characters':0,'digits':0,'symbols':0}
    patternC=re.compile('[A-Za-z]')
    patternD=re.compile('\d')
    if len(files)==0:
        print('no input data!!!')
        return
    start_time=time()
    for x in files:
        with open(x,'r',encoding="utf-8",errors='ignore') as f:
            for k in f:
                chars = len(patternC.findall(k))
                digits = len(patternD.findall(k))
                parser['characters']+=chars
                parser['digits'] += digits
                parser['symbols'] +=len(k)-(chars+digits)
    end_time=time()
    for x in parser:
        print(f'{x}-->{parser[x]}')
    print('=='*30)
    print('lapsed time:'  +str(end_time-start_time) + 's' )
symbols_letters_digid()

#4!!!!!!!!!!!!!!!!!!!!!!!!!

def equality_statements():

    counter=0
    fls=[]
    pattern=re.compile('\s+if\s*\(\s*.+\s*==\s*.+\)|^if\s*\(.+==.+\)|.*if\s*\(\s*\w+\s*\)|\s*if\s*\(\s*\w+\s*\)')

    start_time = time()
    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as f:
            #counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
            for k in f:
                print(pattern.findall(k))
                fls+=pattern.findall(k)
    print('\t If equality Statements found')
    print('==='*30)
    id=1
    for k in fls:
        k=k.replace(' ','').replace('\t','')
        #k=k.strip()
        print(str(id)+'.'+str(k))
        id+=1
    print('\n\n')
    print('lapsed time:' + str(time() - start_time) + 's')
    return len(fls)
equality_statements()

#5!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def over_12_characters():
    found=0
    print(len(files))
    #for regex
    pattern=re.compile('\s*for\s*\(\s*.*\s*;\s*.*\s*;\s*.*\s*\)|\s*for\s*\(\s*.+[:]\s*.+\s*\)')
    start_time = time()
    for x in files:
        with open(x,'r',encoding='ISO-8859-1') as f:
           for k in f:
               for l in pattern.findall(k):
                   print(l)
                   current=l[int(l.find('('))+1:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         print(current)
                         found+=1
                   print('')
    print(f'for loops with over 12 characters:{found}')
    print('lapsed time:' + str(time() - start_time) + 's')
over_12_characters()
#6!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def commonvars():
    commonvars = dict({})
    # Pattern for variables
    unacceptable = re.compile('((const|static|static\sconst)\s+int\s+\w+\s*[=]\s*\w+\s*[;])')
    pattern = re.compile('\s*int\s+\w+[;]')
    patternA = re.compile('(\s*int\s+\w+([,]\w+)*[;])')
    patternB = re.compile('(\s*int\s+\w+([=]\w+)+[;])')
    patternC = re.compile('(\s*int\s+\w+\s*[=]\s*\w+\s*([,]\s*\w+\s*[=]\s*\w+\s*)+[;])')

    matches = []
    start_time = time()
    for x in files:
        with open(x, 'r', encoding='utf8', errors='ignore') as f:
            lines = f.readlines()
            for k in lines:
                word = k
                if word.startswith('//') or word.startswith('#'):
                    continue

                for l in unacceptable.finditer(k):
                    word = k[0:l.start()] + k[l.end():]

                for n1 in pattern.findall(word):
                    if len(n1) == 0: continue
                    word = n1.replace(';', '').strip()
                    spdat = re.split('\s', word)
                    if spdat[1] in commonvars:
                        commonvars[spdat[1]] += 1
                    else:
                        commonvars.update({spdat[1]: 1})
                for n2 in [l[0] for l in patternA.findall(word)]:
                    word = n2.replace(';', ' ').strip()
                    data2 = re.split('[,\s]', word)
                    for j in data2:
                        if j.strip() == 'int':
                            continue
                        if j.strip() in commonvars:
                            commonvars[j.strip()] += 1
                        else:
                            commonvars.update({j.strip(): 1})
                for n3 in [l[0] for l in patternB.findall(word)]:
                    word = n3.strip().replace(';', '')
                    data3 = [x for x in re.split('[\s=]', word) if x.strip() != ';' and re.search('^\s+$', x) == None]
                    counter = 0
                    for j in data3:
                        counter += 1
                        if len(data3) == int(counter):
                            continue
                        if j.strip() == 'int':
                            continue
                        if j.strip() in commonvars:
                            commonvars[j.strip()] += 1
                        else:
                            commonvars.update({j.strip(): 1})

                for n4 in [l[0] for l in patternC.findall(k)]:
                    word = n4.strip().replace(';', '')

                    data4 = [x.replace(' ', '') for x in word.split(',')]
                    for j in data4:
                        checkstr1 = word.split('=')[0]
                        checkstr = checkstr1.split(' ')[1]
                        if checkstr in commonvars:
                            commonvars[checkstr] += 1
                        else:
                            commonvars.update({checkstr: 1})

    tops = sorted(commonvars.items(), key=lambda elem: elem[1])
    # print(commonvars['j'])
    for i in range(len(tops) - 1, len(tops) - 4, -1):
        print(f'{tops[i][0]}-->{tops[i][1]}')
    print('lapsed time:' + str(time() - start_time) + 's')
commonvars()
