def p2_greedy (x, W):
    i = 0;
    w = 300;
    max = 0;
    maxval = 0;
    total = 0;
    totalval = 0;
    while(total < w):
        max = 0;
        maxval = 0;

        i = 0;
        while(i < len(x)):
            if(x[i][0] < w):
                if(x[i][1]/float(x[i][0]) > maxval):

                    maxval = x[i][1]/float(x[i][0]);

                    max = i;
            i+=1;

        if((total + x[max][0]) < w):
            totalval += x[max][1]
            total += x[max][0]
            del x[max]
        else:
            if(len(x) > 1):
                del x[max]
            else:
                break

    return totalval


def p2_dynamic (dataset, W):
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

  return K[n][W]

#========================================
def value_weight_comparison (data_1, data_2):
  vw_ratio(data_1[0], data_1[1]) > vw_ratio(data_2[0], data_2[1])

def vw_ratio (value, weight):
  return float(value/weight)

def vw_ratio_ (d):
  return vw_ratio(d[0], d[1])

X = [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]
D = [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]
print(p2_greedy(D, 300))
print("Answer:", p2_dynamic(X, 200))
