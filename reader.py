import string

def main():
    file = "training.csv"
    f = open(file, 'r')
    
    data = []
    true = []
    
    for line in f:
        row = string.split(line, ",")
        data.append(row)
        if row[len(row) - 1] == "true\n":
            true.append(row[0])
            
    print data
    print len(data)
    print true    
    
if __name__ == "__main__":
   main()