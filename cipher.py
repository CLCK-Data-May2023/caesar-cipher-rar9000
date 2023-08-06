sentence = input("Type a sentence for encryption:")
sentence = sentence.lower()
encrypted_sentence = ""
shifted_keys = {"a" : "f", "b" : "g", "c" : "h", "d" : "i",
                "e" : "j", "f" : "k", "g" : "l", "h" : "m",
                "i" : "n", "j" : "o", "k" : "p", "l" : "q",
                "m" : "r", "n" : "s", "o" : "t", "p" : "u",
                "q" : "v", "r" : "w", "s" : "x", "t" : "y",
                "v" : "z", "x" : "a", "y" : "d", "z" : "e",
                "1" : "6", "2" : "7", "3" : "8", "4" : "9",
                "5" : "0", "6" : "1", "7" : "2", "8" : "3",
                "9" : "4", "0" : "5"}
for keys in sentence:
    if keys in shifted_keys:
        encrypted_sentence = encrypted_sentence + shifted_keys[keys]
    else:
        encrypted_sentence = encrypted_sentence + keys
print("The encrypted sentence is:", encrypted_sentence)