##__author__ = 's1669411'
#!/usr/bin/python
import cmath
import math
from bitarray import bitarray
import mmh3
import sys
class BloomFilter(object):
    def __init__(self,m):
        ##if not(0<false_positive_rate<0.1):
            ##raise ValueError("Error_rate must less than 1%")
        self.m=m
        self.bitarray=bitarray(self.m)
        self.bitarray.setall(0)              
        self.hash_seeds=[2, 3, 5, 7, 11, 13, 17] # 7 prime numbers
        # self.k=0.7*self.m/num_lines ##num of hash functions
        # self.k=int(self.k.real)+1   ###  in this case, by calculating by hand, we know the best num of hash is 7 when I use P(error_rate)=0.009


    def __add__(self, lines):
        for i in self.hash_seeds:
            index=mmh3.hash(lines,i)%self.m
            self.bitarray[index]=1
        return self
    def contains(self, lines):
        for i in self.hash_seeds:
            index=mmh3.hash(lines,i)%self.m
            if self.bitarray[index]==0:
                return False

        return True
num_lines=int(sys.argv[1]) ##since we know the num of lines is 1897987 from hw2.pdf
mfloat=-1*num_lines*math.log(0.009)/(math.log(2.0)*math.log(2.0))#mapsize 0.009 refers to error_rate(0<error_rate<0.01)
m=math.ceil(mfloat)
m=int(m)
bf=BloomFilter(m)
with open('webLarge.txt','r+b') as file_object:
    for line in file_object:
        line=line.strip()
        if bf.contains(line)==0:
            print line
            bf.__add__(line)

##########reference:http://www.maxburstein.com/blog/creating-a-simple-bloom-filter





