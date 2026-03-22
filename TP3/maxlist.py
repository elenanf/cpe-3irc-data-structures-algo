l = [17,11,13,25,18,6]
def maxlist(l):
  if len(l) == 1:
    return l[0]
  else:
    maxLeft = maxlist(l[:len(l)//2])	# left part : ex. l[:5//2] (6/2 = 3) = [17,11,13]
    maxRight = maxlist(l[len(l)//2:])  # right part : ex. l[5//2:] = [25,18,6] etc...
    return max(maxLeft, maxRight)

print(maxlist(l))