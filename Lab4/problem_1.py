def max_(A, B):
  if len(A) > len(B):
    return A
  elif len(B) > len(A):
    return B
  else:
    return A
    
def longest_palindrome_sequence (L):
  n = len(L)

  T = [[ [] for t in range(n) ] for i in range(n)]
  X = [[ 0 for t in range(n) ] for i in range(n) ]

  for i in range(n):
    X[i][i] = 1
    T[i][i] = [L[i]]

  for col in range(2, n+1):
    for i in range(0, n-col+1):
      j = i + col - 1;
      if L[i] == L[j] and col == 2:
        X[i][j] = 2
        T[i][j] = [L[i], L[j]]
      elif L[i] == L[j]:
        X[i][j] = X[i+1][j-1] + 2
        T[i][j] = [L[i]] + T[i+1][j-1] + [L[j]]
      else:
        X[i][j] = max(X[i][j-1], X[i+1][j])
        T[i][j] = max_(T[i][j-1], T[i+1][j])

  return (X[0][n-1], T[0][n-1])

  
print( longest_palindrome_sequence([9,14,9,5,10,6,15,6,13,9]) )