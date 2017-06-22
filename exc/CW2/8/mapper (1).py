__author__ = 's1669411'
N=1000000 #num of lines, given by the hw2.pdf
s=0.01 #threshold value
epsilon=0.001
w=1000#num of windows =1/epsilon

windows={}
#max_error=epsilon*N
current_N=0
D={}
result=[]
with open("queriesLarge.txt","r") as file_object:
    for line in file_object:
        line=line.strip()
        current_N+=1
	w_current=current_N/w+1

        if line in D:
            D[line]+=1
        else:
            D[line]=1
            windows[line]=w_current-1
        if current_N%int(w)==0:
            for line in D.keys():
                if D[line]+windows[line]<=w_current:
                    del D[line]
                    del windows[line]

            	elif D[line]+epsilon*N>=s*N:
                    result.append(line)
                    del D[line]
                     
            

    for x in result:
        print x

####reference:http://www3.cs.stonybrook.edu/~rezaul/Spring-2013/CSE638/Streaming-Algorithms-(Ajinkya-and-Hemanga).pdf
##https://gist.github.com/giwa/bce63f3e2bd493167d92





