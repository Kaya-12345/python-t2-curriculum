text = " Hello, World! "
print("Raw text is:", text)

print("Length:", len(text)) # include spaces

print(text.lower()) # make everything lowercase
print(text.upeer()) # make everything uppercase
print(text.title()) # title case

print(text.strip())  # remove spaces on left and right
print(text.strip().lower())

message = "banana bread"
print("Count of a:", message.count("a"))
print("Find 'bread':", message.find("bread")) # index of first match (or -1 if nothing is found)

print(message.replace("banana", "pumpkin")) # replace first parameter with the second parameter
