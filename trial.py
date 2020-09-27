def func(word, char="A"):
    if(char=="A"):
        return len(word[1:])
    elif(char=="B"):
        return len(word[2:])
    else:
        return len(word)

print(func("Apple","A"),end=" ")
print(func("Apple","B"),end=" ")
print(func("Apple"),end=" ")
print(func("Apple","C"),end=" ")