a =['know']
for new in a:
    try:
        f = open (new,'r')
    except IOError:
        print 'canoot open',new
    else:
        print new,'lines:',len(f.readlines())
        f.close()