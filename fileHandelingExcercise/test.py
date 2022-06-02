opCodes = ["AND ", "OR ", "WHEN "]
newFileList = []
with open("fileHandelingExcercise\sample.txt", "r") as reading_file:
    
    new_file_content = ""
    lines = reading_file.readlines()
    OpCodeLineNo = ''

    for lineNo, line in enumerate(lines):

        newFileList.append(line)
        stripped_line = line.strip()
        result = stripped_line.split("'")[1::2]
        
        if " IS NULL" in result:
            print(f"found quoted 'IS NULL' at line No {lineNo} and opcode to edit at {OpCodeLineNo} and Opcode is {OpCodeToReplace}") 
            var1 = lines[OpCodeLineNo].replace(OpCodeToReplace, OpCodeToReplace+" ISNull(")
            var2 = lines[lineNo].replace("IS NULL", "' ,'''')='''''")
            newFileList[OpCodeLineNo] = var1
            newFileList[lineNo] = var2
            
        for opCode in opCodes:
            if opCode in stripped_line:
                print(f"Found Opcode at line no {lineNo}")
                OpCodeToReplace = opCode
                OpCodeLineNo = lineNo
                newString = opCode + "IsNull("
                new_line = stripped_line.replace(opCode, newString)

reading_file.close()

writing_file = open("fileHandelingExcercise\sample.txt", "w")
for line in newFileList:
    writing_file.write(line)
writing_file.close()
