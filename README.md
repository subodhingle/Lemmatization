🌟 Lemmatizer Using Edit Distance

A simple and interactive Python lemmatizer that reduces words to their root forms using the Edit Distance algorithm.
Perfect for NLP beginners, students, or anyone curious about text processing! 🚀

🎯 Overview

Lemmatization is the process of reducing a word to its base or root form.
Unlike dictionary-based lookups or rule-based systems, this project uses edit distance to find the closest match dynamically.

For example:

Input Word	Lemma
running	run
carss	car
boyz	boy

💡 It also tells you how many operations (insertions, deletions, substitutions) were required!

🔧 Features

✅ Dynamic dictionary input – you choose the root words.

✅ Computes edit distance to measure similarity.

✅ Shows number of steps needed for conversion.

✅ Lightweight and no external dependencies.

✅ Educational: Understand dynamic programming in action.

🧠 How It Works

Edit Distance Calculation

Uses a 2D matrix to compute the minimum number of operations (insert, delete, substitute) to transform one word into another.

Lemmatization

Compares each input word against all dictionary words.

Selects the word with the minimum edit distance as the lemma.

Reports the steps required to transform the word.

User Interaction

Enter dictionary words (root words) separated by spaces.

Enter the words you want to lemmatize.

Receive lemmas with edit distances.

⚡ Example Usage
$ python lemmatizer.py

Enter dictionary words (root words) separated by space: run go eat boy car
Enter words to lemmatize (separated by space): running carss boyz

Lemmatization Results (using Edit Distance):
running → run (Steps required: 4)
carss → car (Steps required: 2)
boyz → boy (Steps required: 1)

🗂 File Structure
lemmatizer/
│
├── lemmatizer.py     # Main Python script
├── README.md         # Project explanation and usage
└── .gitignore        # Optional: Ignore unnecessary files

🚀 Getting Started

Clone the repository:

git clone https://github.com/yourusername/lemmatizer.git
cd lemmatizer


Run the Python script:

python lemmatizer.py


Enter your dictionary words and words to lemmatize.

📚 Why Use This?

Learn text processing and NLP basics.

Understand edit distance / dynamic programming through a practical example.

Build on it for larger NLP projects, chatbots, or spell checkers.
