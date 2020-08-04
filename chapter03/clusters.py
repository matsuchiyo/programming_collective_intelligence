def readfile(filename):
  with open(filename) as file:
    lines = [line for line in file]

  colnames = lines[0].strip().split('\t')[1:]

  rownames = []
  data = []
  for line in lines[1:]:
    p = line.strip().split('\t')
    rownames.append(p[0])
    data.append([float(x) for x in p[1:]])
  return rownames, colnames, data


from math import sqrt

def pearson(vector1, vector2):
  sum1 = sum(vector1)
  sum2 = sum(vector2)

  sum1Sq = sum([pow(vector, 2) for vector in vector1])
  sum2Sq = sum([pow(vector, 2) for vector in vector2])

  pSum = sum([vector1[i] * vector2[i] for i in range(len(vector1))])

  num = pSum - (sum1 * sum2 / len(vector1))
  den = sqrt((sum1Sq - pow(sum1, 2) / len(vector1)) * (sum2Sq - pow(sum2, 2) / len(vector1)))
  if den == 0: return 0

  return 1.0 - num / den
  
class bicluster:
  def __init__(self, vec, left = None, right = None, distance = 0.0, id = None):
    self.left = left
    self.right = right
    self.vec = vec
    self.id = id
    self.distance = distance

def hcluster(rows, distance = pearson):
  distances = {}
  currentclustid = -1

  clust = [bicluster(rows[i], id = i) for i in range(len(rows))]

  while len(clust) > 1:
    lowestpair = (0, 1)
    closest = distance(clust[0].vec, clust[1].vec)

    for i in range(len(clust)):
      for j in range(i + 1, len(clust)):
        if (clust[i].id, clust[j].id) not in distances:
          distances[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)
      
        d = distances[(clust[i].id, clust[j].id)]
      
        if d < closest:
          closest = d
          lowestpair = (i, j)

    mergevec = [(clust[lowestpair[0]].vec[i] + clust[lowestpair[1]].vec[i]) / 2.0 for i in range(len(clust[0].vec))]
    newcluster = bicluster(mergevec, left = clust[lowestpair[0]], right = clust[lowestpair[1]], distance = closest, id = currentclustid)

    currentclustid -= 1
    del clust[lowestpair[1]]
    del clust[lowestpair[0]]
    clust.append(newcluster)
  
  return clust[0]

def printclust(clust, labels = None, n = 0):
  for i in range(n): print(' ', end = ''),

  if clust.id < 0:
    print('-')
  else:
    if labels == None: print(clust.id)
    else: print(labels[clust.id])

  if clust.left != None: printclust(clust.left, labels = labels, n = n + 1)
  if clust.right != None: printclust(clust.right, labels = labels, n = n + 1)