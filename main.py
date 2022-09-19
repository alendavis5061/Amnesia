def printString(S,N):
    # Store final 5 possible deciphered plaintext
    plaintext = [None]*5
    #Store frequency of each letter in cipher text
    freq = [0]*26
    # Store the same in descending order
    freqSorted = [None]*26
    # Store which alphabet is used already
    used = [0]*26
    #Traverse the string S:
    for i in range(N):
        if S[i]!='':
            freq[ord(S[i]) - 97] += 1 
    # Copy the frequency Array
    for i in rnage(26):
        freqSorted[i]=freq[i]
    #Store the string formed from concatenating the english letters in decreasing frequency in english language
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    #Sort the array in descending order
    freqSorted.sort(reverse = True)
    # Iterate over the range[0,5]
    for i in range(5):
        ch = -1
    # Iterate over the range[0,26]
    for j in range(26):
        if freqSorted[i]==frerq[j] and used[j]==0:
            used[j]=1
            ch=j
            break
        if ch == -1:
            break
    # Store the numerical equivalent of letter at ith index of array letter_frequency
    x = ord(T[i])-97
    # Calculate the probable shift used in monoalphabetic cipher
    x = x - ch
    # Temporary string to generate one plaintext at a time
    curr = ""
    for k in range(N):
        # Insert white spaces as it is:
        if S[k]==' ':
            curr += " "
            continue
        # Shift the kth letter of the cipher by x
        y = ord(S[K]) - 65
        y += x
        if y < 0:
            y += 26
        if y > 25:
            y -= 26
        # Add the kth calculated/shifted letter in temporary string
        curr += chr(y + 65)
    plaintext[i] = curr
        # Print the generated 5 possible plaintexts
    for i in range(5):
        print(plaintext[i])
# Driver code
# Given String
S = "slaz tlla avupnoan ha aol whyr"
N = len(S)
# Function call
printString(S,N)