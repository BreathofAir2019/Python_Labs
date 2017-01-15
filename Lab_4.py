@@ -0,0 +1,21 @@
discret1 = raw_input("Please enter a string: ").lower()
test1 = raw_input("Please enter a String: ").lower()

words1 = test1.split()
words2 = discret1.split()


d = {}
for word in words2:
    d[word] = 0

def search(inp1, inp2):
    miss = 0
    for word in inp1:
        if not word in inp2:
            print("Unknown word " + word + " found.")
            miss+=1
    print("There were " + str(miss) + " misspelled words found.")


search(words1, d)
\ No newline at end of file
