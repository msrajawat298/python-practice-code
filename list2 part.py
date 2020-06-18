#index method
#reverse method
#sort method
#sorted method


animals =['elephant','cow','dog','fox']
print(animals)
#=======================INDEX METHOD===================
x=animals.index('cow')#here we find the index number of cow
print(x)

#=======================reverse METHOD===================
animals.reverse()
print("Reverse of give list: - ", animals)

#=======================sort METHOD===================
animals.sort()
print("Arange in sort method: - " ,animals)

#=======================sort with reverse METHOD===================
animals.sort(reverse=True)
print("Arange in sort with reverse method: - " ,animals)
#=======================sorted METHOD==================
print("Arange in sorted method: - " ,sorted(animals))

#=======================sorted with reverse METHOD===================
x=sorted(animals)
x.reverse()
print("Arange in sorted with reverse method: - " ,x)


