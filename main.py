from solution1 import NumberContainers

def main():
    input1 = ["NumberContainers","find","change","change","change","change","find","change","find"]
    input2 = [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]
    output = []

    for i in range(len(input1)):
        if input1[i] == "NumberContainers":
            nc = NumberContainers()
            output.append("null")
        elif input1[i] == "find":
            output.append(nc.find(input2[i][0]))            
        elif input1[i] == "change":
            nc.change(input2[i][0], input2[i][1])
            output.append("null")
        else:
            print("not mapped")
            output.append("null")
    print(output)
if __name__ == "__main__":
    main()