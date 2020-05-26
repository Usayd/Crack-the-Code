infile = open("intercepted.txt", "r")
outfile = open("translated.txt", "w")

linesList = infile.readlines()


for line in linesList:
    giving_me_the_splits = line.split()
    
    for number in giving_me_the_splits:

        asciiNo = int(number)
        character = chr(asciiNo)
        asciiNo = ord(character)
        
        
        #outfile.write(str(asciiNo) + " ")   
        outfile.write(str(character))
        
    print(line, end="")

infile.close()
outfile.close()
