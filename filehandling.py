try:
    # with open(file="SampleFile.txt", mode="r") as f:
    #     f.write("This line is added from code.\nThis is the second line.")
        
        # f.seek(0)
        # content = f.read()
        # print(content)

        # f.seek(0)
        # line = f.readline()
        # print(line)

        # f.seek(0)
        # lines = f.readlines()
        # print(lines)
    
    with open(file="SampleFile.txt", mode="r") as ff:
        for line in ff:
            print(line.strip())

except Exception as e:
    print(e)
else:
    print("Task Completed")
finally:
    print("Program Over")