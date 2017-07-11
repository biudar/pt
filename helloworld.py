print "hello world!"

pante = ',,,,,'
all = ['g', 'o', 'd']
for name in all:
    print pante + name

print 'word'[1:2]
print 'word'[-1]

word = 'pante.mp3'
print word[-3:]
print len(word)
print 'te' in word
print word * 3

pan=['like','kill',4*4,25,3000]
print pan [3]
print pan [-3:]
print pan[:1]




pl=[49,502,81]
pl[0]=pl[0]+36
pl[1]=pl[1]+25
pl[2]=pl[2]+47

while pl[2]<4000000:
    print pl[2],
    pl[0],pl[2]=pl[2],pl[0]+pl[2]

x=int(raw_input('please enter#:'))
if x<0:
    print 'negative'
elif x==0:
    print 'zero'
elif x==1:
    print 'single'
else:
    print 'more'

a=['long','big','find']
for c in a:
    print c,len(c)



