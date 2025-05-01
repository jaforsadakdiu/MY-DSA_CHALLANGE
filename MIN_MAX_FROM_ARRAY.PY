def bcr(ar):
    n = len(ar)
    if(n%2==0):
        if(ar[0]>ar[1]):
            max=ar[0]
            
            min= ar[1]
        else:
           min= ar[0]
           max=ar[1]
        i=2  
            
    else:
        max = min = ar[0]
        i=1
    
            
        while i < n-1:
        
          if ar[i]>ar[i+1]:
             dmax=ar[i] 
             dmin=ar[i+1]

          else:
             
              dmax=ar[i+1] 
              dmin=ar[i]
 
          if dmax> max:
             max =dmax
          if dmin< min:
             min=dmin
          i += 2
        return max,min
      
a=[2,35,5,56]
maxi,mini=bcr(a)
print (maxi,mini)


