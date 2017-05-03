'''
Use map/filter/reduce to do the following:
Find the frequency of a single word
Find the total frequency of a group of words
Find the most frequently occurring word
'''
import re

def get_text():
	start = "*** START OF THIS PROJECT GUTENBERG EBOOK ANNA KARENINA ***"
	end = "*** END OF THIS PROJECT GUTENBERG EBOOK ANNA KARENINA ***"
	txt = open("annaKarenina.txt","r").read()
	txt = txt[txt.index(start):txt.index(end)]

	lines = txt.split("\n")
	words = []
	for line in lines:
		words.extend(line.split(" "))

	c = 0
	cap = len(words)

	words = map(lambda s: unicode(s.rstrip('').replace('\r','').replace('.','').replace('"','').replace('_','').strip('",.*;:?!()').lower(), 'ascii', 'ignore'), words)
	words = filter(lambda w: len(w)>0 and re.search('[a-zA-Z]', w), words)
	return words

#GET TEXT BEFORE RUNNING OPS
txt = get_text()

def freq_of(word):
	return len(filter(lambda s: s.lower()==word, txt))

def freq_sum(wa,wb):
	return freq_of(wa)+freq_of(wb)

def total_freq_of(group):
	if len(group)==1:
		return freq_of(group[0])
	elif len(group)==0:
		return 0
	return reduce(freq_sum, group)

def freq_of_special(word):
	return [word.lower(),len(filter(lambda s: s.lower()==word, txt))]

def most_freq_word():
        
        #Create list(set()) of txt-- much more efficient bc no rept
        ntxt = list(set(txt))

        #do list of freqs for each item in new condensed list
        #map highest index to the word at that
        listOfFreq = [freq_of(i) for i in ntxt]
        most_pos = ntxt[listOfFreq.index(max(listOfFreq))]
        return txt[most_pos]

        #listOfFreq=map(freq_of, ntxt)
        #theWord = ""
        #bigBully = 0
        #for i in listOfFreq:
        #        if i[1]>bigBully:
        #                bigBully=i[1]
        #                theWord=i[0]
                
        #print theWord
        #return theWord

print "Freq of 'love': %d\nFreq of 'cat': %d"%(freq_of('love'),freq_of('cat'))
print "Total freq of ['love','cat']: %d"%(total_freq_of(['love','cat']))
print "Most frequent word is %s"%(most_freq_word())
