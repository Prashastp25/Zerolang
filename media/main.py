arr_keywords = ['-', 'import', '*', '+']
arr_desire_wrds = ['minus', 'asd', 'asdd', 'asx']
temp_store = []
def main():
    keywords = input()
    desire_wrds = input()
    arr_desire_wrds.append(desire_wrds)
    arr_keywords.append(keywords)
    print(desire_wrds)
    fin = input()
    temp_store.append(fin)
    for index in range(0, len(arr_keywords)):
        print("this"+arr_desire_wrds[index],arr_keywords[index])
        print(fin.replace(arr_desire_wrds[index],arr_keywords[index]))
        temp_store.append(temp_store[-1].replace(arr_desire_wrds[index],arr_keywords[index]))
    exec(temp_store[-1])

while True:
    main()