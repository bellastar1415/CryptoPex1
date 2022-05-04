import hashlib
from colorama import Fore, Style

def tinyHash(content):
    originalHash = hashlib.md5(content).hexdigest()  # identify original hash of file
    return originalHash[0:5]


def FindingHash():
    found = 0
    count = 0

    for w in dictWords:
        hash = tinyHash(contents + w)
        if hash == originalHash:
            found = found + 1
            print(found)
            print("Found TinyHash collision #",found,"after trying",count,"words.")
            print(f"\tSaving file as Contract{found}.txt")
            filepath = "contract" + str(found) + ".txt"
            with open(filepath, "wb") as f:
                f.write(contents + w)
            if found >= 5:
                f.close()
                return
        count = count + 1

    for w1 in dictWords:
        for w2 in dictWords:
            count = count + 1
            hash = tinyHash(contents + w1 + w2)
            if hash == originalHash:
                found = found + 1
                print("Found TinyHash collision #",found,"after trying",count,"words.")
                print(f"\tSaving file as Contract{found}.txt")
                filepath = "contract" + str(found) + ".txt"
                with open(filepath, "wb") as f:
                    f.write(contents + w1 + w2)
                if found >= 5:
                    f.close()
                    return

def ChangeContract(num):
    with open("contract.txt", "rb") as fb:
        bcontents = fb.read()
        fb.close()
    with open("contract.txt", "r") as f:
        print("Running hash collision for file:", Style.BRIGHT + f"contract.txt{Style.RESET_ALL}")
        contents = f.read()
        originalHash = hashlib.md5(bcontents).hexdigest()
        print("Full MD5 digest is:", originalHash)
        tinyhash = tinyHash(bcontents)
        print("TinyHash digest is:", tinyhash)
        for k in range(num):
            if (k == 0):
                contents = contents.replace(str(num), str(k), 1)
            else:
                contents = contents.replace(str(k-1), str(k), 1)
            binContents = (contents)
            binContents = binContents.encode()
            bhash = tinyHash(binContents)
            if bhash == tinyhash:
                print("Found TinyHash collision using this number:", k)
                with open("newContract.txt", "w") as newf:
                    newf.write(contents)
                    print("New contract saved to file: newContract.txt")
                    return

if __name__ == '__main__':

    print()
    print(Style.BRIGHT + Fore.MAGENTA + f"Starting Task 1...{Style.RESET_ALL}")
    f = open("samplefile.txt", "rb")           #open the sample file to read from
    contents = f.read()
    print("Running hash collision for file:", Style.BRIGHT + f"samplefile.txt{Style.RESET_ALL}")
    fileLength = len(contents)
    int(fileLength)
    f.close()

    originalHash = tinyHash(contents)
    fullHash = hashlib.md5(contents).hexdigest()
    print("Full MD5 digest is:", fullHash)
    print("TinyHash digest is:", originalHash)

    #print("TinyHash = ", originalHash)
    dictWords = []

    with open("dictionary.txt", "rb") as f:
        for line in f.readlines():
            dictWords.append(line[: len(line) - 2])

    FindingHash()

    print()
    print(Style.BRIGHT +  Fore.MAGENTA +  f"Starting Task 2...{Style.RESET_ALL}")
    num = 100000
    ChangeContract(num)
    """
 m,m    dictf = open("dictionary.txt", "rb")
    appendf = open("samplefiles.txt", "ab")
    for i in range(len(dict.f)):                        #do this for length of dictionary file
        newWord = dictf.readline(i)                     #read a word from dictionary.txt
        appendf.write(newWord)                          #add that word to the samplefile
        newContents = f.read()                          #read the file with appended word
        print(hashlib.md5(newContents).hexdigest())     #get the hash of the contents of the file

        with open("samplefiles.txt", "wb") as revertf:  #open a writable file again
            for line in lines:                          #migrate through the lines
                if line.strip("\n") != newWord:         #look for the previously appended word
                    revertf.write(line)                 #if found rewrite over it with """

