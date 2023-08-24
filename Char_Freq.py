from matplotlib import pyplot as plt

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','o','m','n','p','q','r','s','t','u','v','w','x','y','z','1','2','0','9','3','4','5','6','7','8']


ASCIIorAlpha = int(input("All ASCII Characters or Just alpha-numeric? (Type 0 or 1 respectively):\n"))
filename = input("Input file name (i.e, fruit.txt): ")

#ASCII Frequency Distribution
if (ASCIIorAlpha == 0):
    file = open(filename, 'r')
    text = file.read().lower()
    ascii_dict = {}
    
    for ch in text:
        if ch not in ascii_dict:
            ascii_dict.update({ ch : 1})
        else:
            ascii_dict[ch] = ascii_dict.get(ch) + 1
    print("Frequency of Each Ascii Character:\n")       
    print(ascii_dict)
    
    total = 0
    for i in ascii_dict.values():
        total += i
    
    for i in ascii_dict.keys():
        ascii_dict[i] = ascii_dict.get(i) / total
    
    
    #Histogram
    x= list(ascii_dict.keys())
    y= list(ascii_dict.values())

    #plotting histogram for characters
    plt.title(filename)
    plt.bar(range(len(ascii_dict)),y,tick_label=x)
    plt.savefig('ascii_freq.png')
    
    #Frequency Distribution Ascii
    
#Alpha Numeric Histogram 
else:
    #Get a file and remove the newlines
    file = open(filename, 'r')
    alpha_list = file.read().splitlines();
    
    #Go through the string and remove any non-alpha numeric character
    culled_string = ""
    for i in alpha_list:
        culled_string += ''.join(ch for ch in i if ch.isalnum())
    culled_string = culled_string.lower()
    
    #Start counting each occurence and print out a dictionary of the frequency
    dict_alpha = {}
    total = 0
    for i in alphabet:
        dict_alpha.update({i : culled_string.count(i)})
        total += culled_string.count(i)
    print("Frequency of Each Alpha-Numeric Character:\n")
    print(dict_alpha)
    
    
    for i in alphabet:
        dict_alpha[i] = dict_alpha.get(i) / total
    
    
    #Histogram
    x= list(dict_alpha.keys())
    y= list(dict_alpha.values())

    #plotting histogram for characters
    plt.title(filename)
    plt.bar(range(len(alphabet)),y,tick_label=x)
    plt.savefig('alpha_numeric_histogram.png')