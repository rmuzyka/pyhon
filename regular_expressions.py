"""Wyrazenia regularne to pewne "wzorce", za pomoca ktorych mozna opisac ciag znakow. 
Za ich pomoca mozna okreslic z czego ma sie dokladnie skladac np. adres e-mail."""


import re

text = """Wyobraz sobie, ze ten tekst zawiera numer
PIN 9434 twojej karty do bankomatu, a ty wlasnie go
zapomniales. Jak szybko go odnalezc?"""

path = r'\d\d\d\d'
dopasowanie = re.search(path,text)
print (dopasowanie) #return block of characters in Match object form

if dopasowanie:
    numer = dopasowanie.group()  #group() wydobywa napis z obiektu Match
    print numer

#PAIR OF WORDS SEPARATES BY SPACE
pattern = r'\w+ \w+'

r = re.compile(pattern)
m = r.match('hello my best world !, python regex, june 2018')
#is equivalent to
m = re.match(pattern,'hello my best world !, python regex, june 2018')

print m.group()

#PAIR OF IDENTICAL WORDS
pattern = r'(\w+) \1'
r = re.compile(pattern)
n = r.match('hello world') #None
m = r.match('hello hello my my')
print n
print m.group()

pattern = r'(\w+) \1 \1'
r = re.compile(pattern)
m = r.match('my my my')
print m.group()

pattern = r'(\w+)\1a\1'
r = re.compile(pattern)
m = r.match('mymyamy')
print m.group()

#Dopasowanie pary identycznych slow przy pomocy grupy nazwanej
#robi to samo co r'(\w+) \1'
pattern = r'(?P<word>\w+) (?P=word)'
r = re.compile(pattern)
m = r.match('hello hello hello')
print m.group()

pattern = r'(?P<word>\w+) (?P=word) (?P=word)'
r = re.compile(pattern)
m = r.match('hello hello hello')
print m.group()

pattern = r'(?P<word>\w+)XX(?P=word)(?P=word)'
r = re.compile(pattern)
m = r.match('helloXXhellohello')
print m.group()

pattern = r'(?P<word>\w+) (?P=word) (?P<secondword>\w+) (?P=secondword) (?P=word)'
r = re.compile(pattern)
m = r.match('hello hello second second hello')
print m.group()


#CHANGING WWW ADDRESS ON HYPERLINK
str = r'http://www.python.org'
pattern = r'(http://\w+(\.\w+)+)'
r = re.compile(pattern)
link = r.sub(r'<a href="\1">\1</a>', str)
print link

#CHANGING WWW ADDRESS ON HYPERLINK WITH NAMED GROUP
str = r'http://www.pythonnamedgroup.org'
pattern = r'(?P<addr>http://\w+(\.\w+)+)'
r = re.compile(pattern)
link = r.sub(r'<a href="\g<addr>">\g<addr></a>', str)
print link


#OPCJE I MODYFIKATORY
r = re.compile("This is regex pattern", re.VERBOSE|re.IGNORECASE|re.DOTALL|re.MULTILINE)

a = re.compile(r'\d+\.\d*')
aa = a.match('123.12')
print aa.group()

b = re.compile(r"""\d+ #czesc calkowita
                   \.  #kropka dziesietna
                   \d* #czesc ulamkowa""", re.X)

c = re.compile("""(?x)  #wlacz komentarze
                   \d+  #czesc calkowita
                   \.   #kropka dziesietna
                   \d*  #czesc ulamkowa""")

"mozna tez wstawic we wzorcu komentarz postaci (?#komentarz)"


# # #

#1 LICZBA ZMIENNOPRZECINKOWA W LANCUCHU ZNAKOW
pattern = r'(\d+)\.(\d*)'   # probably equivalent to r'(\d+).(\d*)'
str = '342.79+12.56'
m = re.match(pattern, str)  # gdy wyszukujemy wiele razy efektywniej jest na poczatku dokonac kompilacji wzorca do obiektu
                            # r=re.compile(pattern) -> m=r.match(str)
if m:
    print ("{0} pasuje do {1}".format(pattern,str))
    print m.group()
else:
    print("{0} nie pasuje do {1}".format(pattern,str))
    
print m.group(0)
print m.group(1)
print m.group(2)
print m.start(1), m.end(1)


# re MODULE METHODS
pattern = r'(\d+)\.(\d*)'
str = 'a + 342.79+ b + 12.56 * 10'
str2 = '342.79+ b + 12.56 * 10'
r = re.compile(pattern)

m = r.match(str)   # brak dopasowania
m = r.match(str2)   # jest dopasowanie 342.79

m = r.search(str)  # dopasowuje pierwsza liczbe zmiennoprzecinkowa, tj. 342.79
if m:
    print(m.group())


floats = [ x[0] for x in re.findall( r'((\d+)\.(\d*))', str) ]  # r'(\d+)\.(\d*)' return only ['342', '12']
""" only x return that list ('342.79', '342', '79')
    because ((\d+)\.(\d*)) return 3! groups
    consequently
    (\d+)\.(\d*) return only 2 groups
    and in this case x = ('342', '79')
    """
print("floats=", floats)


for m in r.finditer(str):   #return an iterator yielding match objects (not in list)
    print(m.group())
        # >342.79
        # >12.56

list = [m.group() for m in r.finditer(str)]
print ("list=",list)

pattern = r'(\d+)\.(\d*)'
str = 'a + 342.79+ b + 12.56 * 10'
# pattern = r'\d+\.\d*'
r = re.compile(pattern)
# m = r.search(str)
# print 'xxxxxxxxxx  ' + m.group()
# newstr = r.sub('\2.\1', str);
newstr = r.sub('\\2.\\1', str);
# \\ is equivalent to r'':
        # r.sub(r'\2.\1', str);
print 'sub: ' + str
print 'sub: ' + newstr

newstr = r.subn(r"\2.\1", str)  # return also number of changes
print 'subn: '
print newstr


str = 'a + 342.79+ b + 12.56 * 10'
terms1 = re.split("\s*[+*]\s*", str) # [+*] a single character of: + or *
terms2 = re.split("(\s*[+*]\s*)", str)
print terms1
print terms2
#split from Marcin
str_we_want = '12:34:56:78:90:AB'
str_we_have = '1234567890AB'
terms = re.split('(\w\w)', str_we_have, maxsplit=0)
print terms
my_terms = [terms[x] for x in range(0,len(terms)) if x%2!=0]
print my_terms
sep = ':'
print sep.join(my_terms)

def split_function(str, sep):
    division = re.split('(\w\w)', str)
    division_without_sep = [division[x] for x in range(0,len(division)) if x%2!=0]
    print 'funkcja ' + sep.join(division_without_sep)
    return sep.join(division_without_sep)
split_function(str_we_have, sep)

#split from py documentation
r = re.split('\W+', 'Words, words, words. ')
print r
r = re.split('(\W+)', 'Words, words, words. ')
print r
r = re.split('[a-f]+','0aaa3B9', flags=re.IGNORECASE)
print r
r = re.split('(\W+)', '...wor    ds, words...')
rr = re.split('\W+', '...wor     ds, words...')
print r
print rr
r = re.split('x*', 'axbc')
rr = re.split('x+', 'axbc')
print r
print rr


#DIFFRENT TASK FROM NET
text =  "one two 3.44 5,6 seven.eight nine,ten"
result = ["one", "two", "3.44", "5,6" , "seven", "eight", "nine", "ten"]
result = re.split('\s|(?<!\d)[.,](?!\d)', text)
print result

s='foobaz'
sr='forbard '
print (re.match('foo(?!bar)',s)).group()
print (re.search('(?<!foo)bard',sr)).group()

text = "one,two one , two 3.44 5,6 seven.eight nine,ten,1.2,a,5"
print re.split('\s|(?<!\d)[.,][.,](?!\d)', text)
print re.split('(\s|[.,](?!\d))', text)
print re.split('\s|(?<!\d)[.,]|[.,](?!\d)', text)

s='Beautiful, is; better*than\nugly'
# print re.split(',|;|\*|\n',s)
print re.split('(?i)[^a-z ]',s)

delimeters = "a", "...", "(c)"
example = "stackoverflow (c) is awesome... isn't it?"
regexPattern = '|'.join(map(re.escape, delimeters))
    # python map()
        # def calculateSquare(n):
        #     return n*n
        # numbers = (1,2,3,4)
        # result = map(calculateSquare, numbers)
        # print(result)
        # numbersSquare = set(result)
        # print numbersSquare
    # print re.escape('python.org')
    # > python\.org
print regexPattern
print re.split(regexPattern, example)




# !assert 
#wyciaganie danej grupy





# a = 'dsd dsd dsd'
# print(a.split()) #['dsd', 'dsd', 'dsd']