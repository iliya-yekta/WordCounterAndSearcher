def openFile(f):
    dic = {}
    try:
        with open(f,'r',encoding="utf-8") as file:
            file1 = file.read().split()
            for i in file1:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
            print("Succeeded to open the file")
    except FileNotFoundError:
        print("File not found. Try again.")
    except LookupError:
        print("Could not read the file. Try again.")
    except Exception:
        print("Something went wrong. Try again.")
    return dic


def showsRepeatedWords(words):
    for word,count in words.items():
        if count > 1:
            print(f"{word}:{count}",end=" | ")
        else:
            continue

def showQuantityOfWord(w,words):
    if w in words:
        print(f"{w} has written {words[w]} time(s)")
    else:
        print("This word does not exist")


def main():
    while 1:
        try:
            print("""\n
            put the text file -> 1
            show the repeated word -> 2
            show a word counted -> 3
            end task -> 0
                    """)
            choice = int(input("choose the option: "))
            if choice == 1: 
                filePath = str(input("Write the file path: "))
                words = openFile(filePath)
                if not words:
                    filePath = None
                    words = {}

            elif choice == 2: 
                showsRepeatedWords(words) if filePath else print("Enter the file path first.")
                if showsRepeatedWords(words) == None:
                    print("There's no repeated word.")

            elif choice == 3:
                if filePath:
                    word = str(input("Enter sth to count: "))
                    showQuantityOfWord(word,words)
                else: 
                    print("Enter the file path first.")


            elif choice ==  0: break

            else: print("Invalid choice!")
        except ValueError:
            print("Enter a valid choice.")

main()


