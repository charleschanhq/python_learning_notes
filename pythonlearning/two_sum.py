new=[1,2,7,9,3,4]
new1=3
newlen=len(new)
for m in (0,newlen-1):
  for n in (0,newlen-1):
    if new[m]+new[n]==new1:
      print (m)
      