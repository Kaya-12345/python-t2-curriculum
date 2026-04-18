# "xxx" -> "x-x-x-"
name = "xxx"
result = ""
for ch in name:
  result = result + ch + "-"
print(result)

letter = ["p", "y", "t", "h", "o", "n"]
# Dumb way
result = ""
for ch in letters:
  result = result + ch
print(result)
# Smart way
built = "".join(letters)
print(built)
