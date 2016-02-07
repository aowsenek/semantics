 def main2():
179     from pickle import load
180     nbrs = load( open( 'nbrs.pkl' , 'rb' ) )
181     leng = len(nbrs) -1
182     neighs =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
183     while(leng >= 0):
184         x = nbrs.get(wordlist[leng])
185         y = 0
186         if(x != None):
187             while (y < len(x)):
188                 y+=1
189             neighs[y] += 1
190             if( y == 13):
191                 print(wordlist[leng], x)
192         else:
193             neighs[0] += 1
194         leng -= 1
195     print(neighs)
196
197 def main1():
198     dic = toDict(wordlist)
199     fout = open( 'nbrs.pkl' , 'wb' )
200     dump( di , fout , protocol = 2 )
201     fout.close()

