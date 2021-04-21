import sys
sys.path.append('..')
import file_walk as fw
import re
import os

from time import time


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

#1!!!!!!!!!!!!!!!!!!!!!!!!!
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

#2!!!!!!!!!!!!!!!!!!!!!!!!!!
starttime=time()
    linecounter=0
    for i in files:
        with open(i,'r',encoding="utf-8",errors='ignore') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    print('Lines of code:'+str(linecounter))
    print('Elapsed Time for finding all lines of code:'+str(time()-starttime)+'\'s')

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
    print(f'lapsed time:{end_time-start_time} \ 's')
symbols_letters_digid()

#4!!!!!!!!!!!!!!!!!!!!!!!!!

    def equality_statements():
        def equality_statements():
            counter = 0

        fls = []
        pattern = re.compile('\s+if\s*\(\s*.+\s*==\s*.+\)|^if\s*\(.+==.+\)|.*if\s*\(\s*\w+\s*\)')
        patternB = re.compile("\s*if\s*\(\s*\w+\s*\)")
        # |if\s*\(\s*(\w|\d)+\s*\)
        # if\s*\(\s*(\w|\d)+\s*\)-->if(k) αν k είναι boolean μεταβλητή η ένας αριθμός
        for x in files:
            with open(x, 'r', encoding='utf-8', errors='ignore') as f:
                # counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
                for k in f:
                    print(patternB.findall(k))
                    fls += pattern.findall(k)
                    fls += patternB.findall(k)
        print('\t If equality Statements found')
        print('===' * 30)
        id = 1
        for k in fls:
            k = k.replace(' ', '').replace('\t', '')
            # k=k.strip()
            tm.cprint(str(id) + '.' + str(k), 'green')
            id += 1
        print('\n\n')
        return len(fls)

#5!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

#6!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def commonvars():
    vars = {}
    # Τρια Μοτίβα μεταβλητών
    # int a;-->int\s+\w+;
    # int a=10;-->int\s+\w+\s*([=]\s*\w+\s*)+;
    # int a,b,c;-->int\s+\w+\s*([,]\s*\w+\s*)*;
    # Μη αποδεκτό-->const int a=10;

    # (int\s+\w+\s*([,]\s*\w+\s*)*[;]|\s*int\s+\w+\s*([=]\s*\w+\s*)+[;])
    patternf = re.compile('(int\s+\w+\s*([,]\s*\w+\s*)*[;]|\s*int\s+\w+\s*([=]\s*\w+\s*)+[;])')
    constpattern = re.compile('(const\s+int\s*\w+\s*([=]\s*\w+\s*)+[;])')
    for x in files:
        with open(x, 'r', encoding='utf-8', errors='ignore') as L:
            for k in L:
                cleanconst = k
                for l in constpattern.findall(k):
                    cleanconst = k.replace(l[0], '')
                for t in patternf.findall(cleanconst):
                    print('Variable:' + str(t))

