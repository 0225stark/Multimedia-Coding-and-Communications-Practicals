# -*- coding: utf-8 -*-

import json
import csv
import math

# declare structure node
class  node :
    def __init__(self) -> None:
        # for storing symbol
        self.sym=''
        # for storing probability or frequency
        self.pro=0.0
        self.arr=[0]*20
        self.top=0
p=[node() for _ in range(20)]
 
# function to find shannon code
def shannon(l, h, p):
    pack1 = 0; pack2 = 0; diff1 = 0; diff2 = 0
    if ((l + 1) == h or l == h or l > h) :
        if (l == h or l > h):
            return
        p[h].top+=1
        p[h].arr[(p[h].top)] = 0
        p[l].top+=1
        p[l].arr[(p[l].top)] = 1
         
        return
     
    else :
        for i in range(l,h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1) :
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k+1):
                pack1 = pack1 + p[i].pro
            for i in range(h,k,-1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1):
                break
            diff1 = diff2
            j+=1
         
        k+=1
        for i in range(l,k+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 1
             
        for i in range(k + 1,h+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 0
             
 
        # Invoke shannon function
        shannon(l, k, p)
        shannon(k + 1, h, p)
     
 
 
# Function to sort the symbols
# based on their probability or frequency
def sortByProbability(n, p):
    temp=node()
    for j in range(1,n) :
        for i in range(n - 1) :
            if ((p[i].pro) > (p[i + 1].pro)) :
                temp.pro = p[i].pro
                temp.sym = p[i].sym
 
                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym
 
                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym
             
# Driver code
if __name__ == '__main__':
    total = 0
 
    # Input number of symbols
    n=int(input("Enter the number of symbols: "))
    i=0
    # Input symbols
    for i in range(n):
        print("Enter symbol", i + 1," : ",end="")
        ch=input()
        # Insert the symbol to node
        p[i].sym += ch
     
 
    # Input probability of symbols
    x = []
    for i in range(n):
        print("\nEnter probability of", p[i].sym, ": ")
        ele=float(input())
        x.append(ele)
 
        # Insert the value to node
        p[i].pro = x[i]
        total = total + p[i].pro
 
        # checking max probability
        if (total > 1) :
            print("Invalid. Enter new values")
            total = total - p[i].pro
            i-=1
         
     
    i+=1
    p[i].pro = 1 - total
    # Sorting the symbols based on
    # their probability or frequency
    sortByProbability(n, p)
 
    for i in range(n):
        p[i].top = -1
 
    # Find the shannon code
    shannon(0, n - 1, p)

    # Output coding tree in JSON format
    coding_tree = {}
    for i in range(n):
      node_dict = {
          "symbol": p[i].sym,
          "probability": p[i].pro,
          "code": "".join(str(bit) for bit in p[i].arr[:p[i].top+1])
      }
      coding_tree[i+1] = node_dict
    with open('coding_tree.json', 'w') as f:
      json.dump(coding_tree, f, indent=4)

    # Output symbol code table in CSV format
    with open('symbol_code_table.csv', 'w', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(["Symbol", "Probability", "Code"])
      for i in range(n - 1, -1, -1):
        row = [p[i].sym, p[i].pro, "".join(str(bit) for bit in p[i].arr[:p[i].top+1])]
        writer.writerow(row)
    # display compression ratio
    size_original = n * sum([-p[i].pro * math.log2(p[i].pro) for i in range(n)])
    size_compressed = sum(sum(p[i].arr[j] == 1 for j in range(p[i].top + 1)) for i in range(n))
    compression_ratio = size_original / size_compressed
    print("\nCompression ratio: ")
    print(compression_ratio)

