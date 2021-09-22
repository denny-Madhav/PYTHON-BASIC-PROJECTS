import wikipedia

search_result = wikipedia.summary("Python features", 5)
search = search_result.split(".")

print(*search, sep=" \n")
