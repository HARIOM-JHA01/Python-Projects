from statistics import mean
estimates = []
c = 1
while(c!=0):
    estimates.append(int(input("Enter Data : ")))
    print("continue : 1")
    print("End : 0")
    c = int(input("Enter choice : "))
estimates.sort()
tv = int(0.1*len(estimates))
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]
print(mean(estimates))