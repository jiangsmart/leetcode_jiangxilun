x=-12
xs=str(abs(x))
length=len(xs)
news=list('')
for i in range(length):
   news.append(xs[length-i-1])
news=int(''.join(news))
if x>0:
    return news
else:
    return -news
