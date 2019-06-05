print("Hello my name is Dat and these are my ship sizes")
sizes = [5,7,300,90,24,50,75]
print(sizes)
print("Now my biggest sheep has size {0} let's shear it".format(max(sizes)))
sizes[2] = 8
print("after shearing, here is my flock")

print(sizes)
print("One month has passed, now here is my flock")
for i in sizes:
    i+=50
    print(i)
