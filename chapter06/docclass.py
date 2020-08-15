import re
import math

def getwords(doc):
  # splitter = re.compile('\\W*')
  splitter = re.compile('\\W+')
  words = [s.lower() for s in splitter.split(doc) if len(s) > 2 and len(s) < 20]
  return dict([(w, 1) for w in words])

class classifier:
  def __init__(self, getfeatures, filename = None):
    self.fc = {} # feature count
    self.cc = {} # category count
    self.getfeatures = getfeatures

  def incf(self, f, cat):
    self.fc.setdefault(f, {})
    self.fc[f].setdefault(cat, 0)
    self.fc[f][cat] += 1

  def incc(self, cat):
    self.cc.setdefault(cat, 0)
    self.cc[cat] += 1

  def fcount(self, f, cat): # count of items which has specified feature in specified category
    if f in self.fc and cat in self.fc[f]:
      return float(self.fc[f][cat])
    return 0.0

  def catcount(self, cat): # count of items in specified category
    if cat in self.cc:
      return float(self.cc[cat])
    return 0.0

  def totalcount(self): # total item count
    return sum(self.cc.values())

  def categories(self):
    return self.cc.keys()

  def train(self, item, cat):
    features = self.getfeatures(item)
    for f in features:
      self.incf(f, cat)
    self.incc(cat)
  
  def fprob(self, f, cat):
    if self.catcount(cat) == 0: return 0
    return self.fcount(f, cat) / self.catcount(cat)

  def weightedprob(self, f, cat, prf, weight = 1.0, ap = 0.5):
    basicprob = prf(f, cat)
    totals = sum([self.fcount(f, c) for c in self.categories()]) # total count of documents containing specified feature 
    bp = ((weight * ap) + (totals * basicprob)) / (weight + totals)
    return bp

def sampletrain(cl):
  cl.train('Nobody owns the water', 'good')
  cl.train('the quick rabbit jumps fences', 'good')
  cl.train('buy pharmaceuiticals now', 'bad')
  cl.train('make quick money at the online casino', 'bad')
  cl.train('the quick brown fox jumps', 'good')

class naivebayes(classifier):
  def docprob(self, item, cat):
    features = self.getfeatures(item)
    p = 1
    for f in features: p *= self.weightedprob(f, cat, self.fprob)
    return p

  def prob(self, item, cat):
    catprob = self.catcount(cat) / self.totalcount()
    docprob = self.docprob(item, cat)
    return docprob * catprob

  def __init__(self, getfeatures):
    classifier.__init__(self, getfeatures)
    self.thresholds = {}


  def setthreshold(self, cat, t):
    self.thresholds[cat] = t

  def getthreshold(self, cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]

  def classify(self, item, default = None):
    probs = {}
    max = 0.0
    for cat in self.categories():
      probs[cat] = self.prob(item, cat)
      if probs[cat] > max:
        max = probs[cat]
        best = cat

    for cat in probs:
      if cat == best: continue
      if probs[cat] * self.getthreshold(best) > probs[best]: return default
    return best
    
  
