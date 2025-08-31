# -------------------------------
# Step 1: Edit Distance Function
# -------------------------------

# Function to calculate edit distance between two strings
def edit_distance(s1, s2):
    # Step 1: Create a 2D matrix of size (len(s1)+1) x (len(s2)+1)
    # m[i][j] will hold the edit distance between s1[0..i-1] and s2[0..j-1]
    m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Step 2: Initialize base cases
    # If second string is empty, remove all characters from first string
    for i in range(len(s1) + 1):
        m[i][0] = i

    # If first string is empty, insert all characters of second string
    for j in range(len(s2) + 1):
        m[0][j] = j

    # Step 3: Fill the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # Step 4: Cost of substitution
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            # Step 5: Calculate minimum of
            # a) substitution (diagonal)
            # b) deletion (up)
            # c) insertion (left)
            m[i][j] = min(
                m[i - 1][j - 1] + cost,  # substitution
                m[i - 1][j] + 1,         # deletion
                m[i][j - 1] + 1          # insertion
            )

    # Step 6: Return the edit distance (bottom-right cell)
    return m[len(s1)][len(s2)]


# -------------------------------
# Step 2: Lemmatizer Using Edit Distance
# -------------------------------

# Function to lemmatize a word using a dictionary of root words
def lemmatize(word, dictionary):
    # Initialize minimum distance to infinity
    min_distance = float('inf')
    # Default lemma is the original word
    lemma = word

    # Step 1: Compare input word with each word in the dictionary
    for dict_word in dictionary:
        # Step 2: Compute edit distance
        dist = edit_distance(word.lower(), dict_word.lower())
        # Step 3: Update lemma if this dictionary word is closer
        if dist < min_distance:
            min_distance = dist
            lemma = dict_word

    # Step 4: Return both the best matching lemma and the number of steps required
    return lemma, min_distance


# -------------------------------
# Step 3: Main Program
# -------------------------------

if __name__ == "__main__":
    # Step 1: Ask user to input dictionary words separated by space
    dict_input = input("Enter dictionary words (root words) separated by space: ")
    lemma_dict = dict_input.strip().split()

    # Step 2: Ask user to input words to lemmatize
    user_input = input("Enter words to lemmatize (separated by space): ")
    words = user_input.strip().split()

    # Step 3: Display lemmatization results
    print("\nLemmatization Results (using Edit Distance):")
    for word in words:
        lemma, steps = lemmatize(word, lemma_dict)
        print(f"{word} → {lemma} (Steps required: {steps})")