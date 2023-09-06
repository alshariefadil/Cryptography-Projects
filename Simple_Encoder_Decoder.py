#ASCII Value for 'a'. Used in the Encoding portion. 
value = 97

#User Input for decoding or encoding
DeOrEn = int(input("Decode or Encode (Enter 0 or 1):"))

#Decoding Portion.
if DeOrEn == 0: 
    rt = int(input("Input or Read from File (Enter 1 or 0): "))
    actual_words = open('words_alpha.txt', 'r')
    actual_words = actual_words.read().splitlines()
    #Decode - Text File
    if rt == 0:
        filename = input("Input filename here (ie: Fruits.txt):\n")
        file = open(filename, 'r')
        file = file.read().splitlines()
        decode_dict = {}
        for i in file:
            possible = []
            for j in actual_words:
                if (len(j) == len(i)):
                    encode_string = ""
                    encode_dict = {}
                    for ch in j:
                        if encode_dict == {}:
                            encode_dict.update({ch : chr(value)})
                            encode_string += chr(value)
                            value += 1
                        else:
                            if ch in encode_dict:
                                encode_string += encode_dict.get(ch)
                            else:
                                encode_dict.update({ch : chr(value)})
                                encode_string += chr(value)
                                value += 1
                    if encode_string == i:
                        possible.append(j)
                    value = 97
            decode_dict.update({i : possible})
        see = input("Do you want to see the list (Yes or No): ")
        if (see == 'Yes'):        
            print(decode_dict)
        with open('decode_text.txt','w') as f:
            for x,y in decode_dict.items():
                f.write(x + " :  [")
                for n in y:
                    f.write(n + ', ')
                f.write(" ]\n")
    #Decode - Input Pattern
    else:
        possible = []
        f = open('decode_written.txt', 'w')
        written = input("Enter Letter pattern in lowercase:\n")
        for i in actual_words:
            if (len(i) == len(written)):
                encode_string = ""
                encode_dict = {}
                for ch in i:
                    if encode_dict == {}:
                        encode_dict.update({ch : chr(value)})
                        encode_string += chr(value)
                        value += 1
                    else:
                        if ch in encode_dict:
                            encode_string += encode_dict.get(ch)
                        else:
                            encode_dict.update({ch: chr(value)})
                            encode_string += chr(value)
                            value += 1
                if encode_string == written:
                    possible.append(i)
                value = 97
        print(possible)
        for line in possible:
            f.write(line)
            f.write('\n')

#Encoding Portion
else: 
    rt = int(input("Input or Read from File (Enter 1 or 0): "))
    #Encode - Text File
    if rt == 0:
        filename = input("Input filename here (ie, fruit.txt):")
        #Read a file, we'll change this to be generic later.
        file = open(filename, 'r')
        #Make a list of all the lines without newline characters
        read_list = file.read().splitlines()
        encode_list =[]
        #Go through each line
        for i in read_list:
            #Copy and pasted from Encode - User Input. Read that instead.
            read = i.lower()
            encode_dict = {}
            encode_string = ""
            for c in read:
                if encode_dict == {}:
                    encode_dict.update({c : chr(value)})
                    encode_string += chr(value)
                    value += 1
                else:
                    if c in encode_dict:
                        encode_string += encode_dict.get(c)
                    else:
                        encode_dict.update({c: chr(value)})
                        encode_string += chr(value)
                        value += 1
            #Add a newline to the end of each line. and place it in the encoded list and reset value back to 'a'.
            encode_list.append(encode_string)
            value = 97
        see = input("Do you want to see the list (Yes or No): ")
        if (see == 'Yes'):
            print(encode_list)
        with open('encode_file.txt', 'w') as f:
            for line in encode_list:
                f.write(line)
                f.write('\n')
            
    #Encode - User Input
    else:
        written = input("Enter a word or sentence: ")
        #Turn the word lowercase, to remove working with Caps
        written = written.lower()
        encode_dict = {}
        encode_string = ""
        for c in written:
            #For each character in a word, when we start
            if encode_dict == {}:
                #...Place the first char in the dictionary with it's letter
                encode_dict.update({c : chr(value)})
                #Update the encoded string and increment value to next letter
                encode_string += chr(value)
                value += 1
            else:
                #If the letter has an ASCII value already, we just place it in the string
                if c in encode_dict:
                    encode_string += encode_dict.get(c)
                else:
                    #Else, we add it to the dictionary, assign it a value and increment the next letter
                    encode_dict.update({c: chr(value)})
                    encode_string += chr(value)
                    value += 1
                    print(encode_string)
            with open('encoded_input.txt','w') as f:
                f.write(encode_string)
                f.write('\n')