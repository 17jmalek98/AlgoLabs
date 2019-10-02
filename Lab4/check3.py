dataset =[[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]];
W = 200
n = len(dataset)
# K = [[0 for i in range(n+1)] for j in range(W+1) ]
K = [[0 for p in range(W+1)] for q in range(n+1) ]

for j in range(1, n+1):
  for w in range(1, W+1):
	  v_j = dataset[j-1][1]
	  w_j = dataset[j-1][0]
	  if w_j > w:
		K[j][w] = K[j-1][w]
	  else:
		K[j][w] = max(K[j-1][w], K[j-1][w-w_j]+v_j)

print K
