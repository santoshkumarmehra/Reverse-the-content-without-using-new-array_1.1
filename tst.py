arr=[5,10,15,20,25,30,35,40]
i=0
j=len(arr)-1
while i<=j:
	x=arr[i]
	arr[i]=arr[j]
	arr[j]=x
	i=i+1
	j=j-1
print(arr)
