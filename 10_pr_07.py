def remove_and_split(string , word):
    newStr =  string.replace(word , "")
    return newStr.strip()




this = "       Aadil is a good"
n = remove_and_split(this , "Aadil")
print(n)
# print(this)
# print(this.strip())