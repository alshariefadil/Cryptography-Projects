# Cryptography-Projects
Contains projects done during my Spring 2022 Semester for my cryptography class.

  Char_Freq.py is able to perform two functions. First, it reads the contents of the text file and plots
the number of ascii characters on a histogram, and then saves it to a png file. The second function is the 
same but instead of ascii characters, it's alpha-numeric characters.

  The Simple Decoder/Encoder is able to accept inputs and text files and encode or decode them.
  Encoding is better told by an example, as an example the word cheese would be encoded into abccde
  as 'c' is the first letter encountered it becomes 'a', and since 'h' is the 2nd letter encountered it 
  becomes 'b'. since the third letter is 'e', it becomes 'c'. The fourth letter is also 'e', so it remains
  'c'. 's' is the fifth letter and hasn't been encoded yet, so 'd'. The last letter is an e, which has 
  already been encoded as a 'c'. The program also recognizes spaces as characters. After prompting the user
  if they would like to decode/encode and if they would like to manually input or read from a text file, it will
  leave a file with the result.

  The words_alpha.txt file contains a list of words to use when providing results for the simple decoder/encoder.
