import feedparser
import re
import uuid

def getwordcounts(url):
  data = feedparser.parse(url)
  wc = {}

  for entry in data.entries:
    if 'summary' in entry: summary=entry.summary
    else: summary = entry.description

    words = getwords(entry.title + ' ' + summary)
    for word in words:
      wc.setdefault(word, 0)
      wc[word] += 1
  
  return getattr(data.feed, 'title', str(uuid.uuid1())), wc
#  return data.feed.title, wc

def getwords(html):
  txt = re.compile(r'<[^>]+>').sub('', html)
  words = re.compile(r'[^A-Z^a-z]+').split(txt)
  return [word.lower() for word in words if word!='']

apcount = {}
wordcounts = {}

# feedlist = [line for line in file('feedlist.txt')]

with open('feedlist.txt') as file:
  feedlist = [line for line in file]

for feedurl in feedlist:
    print("### feedurl: " + feedurl)
#  try:
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word, count in wc.items():
      apcount.setdefault(word,0)
      if count>1:
        apcount[word]+=1
#  except:
#    print 'Failed to parse feed %s' % feedurl

wordlist = []
for word, blogcount in apcount.items():
  fraction = float(blogcount) / len(feedlist)
  if fraction > 0.1 and fraction < 0.5: wordlist.append(word)

# out = file('blogdata.txt', 'w')
with open('blogdata.txt', 'w') as out:
  out.write('Blog')
  for word in wordlist: out.write('\t%s' % word)
  out.write('\n')

  for blog, wordcount in wordcounts.items():
    out.write(blog)
    for word in wordlist:
      if word in wordcount: out.write('\t%d' % wordcount[word])
      else: out.write('\t0')
    out.write('\n')
