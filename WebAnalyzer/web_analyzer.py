# Collaborators: Sebastian Silva & Erioluwa Temiloluwa
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status()     # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")
    
print(soup.prettify())
print()
print("-" * 100)
print()

# 3 -- Data Analysis --
# Count and display, the number of headings, links, and paragraphs
print("\n-- Data Analysis --")

# Number of headings
headings = soup.find_all('h')

for i in range(1, 7):  # Checking from h1 to h6
    headings.extend(soup.find_all(f'h{i}'))
headingCount = len(headings)
print(f"Total heading count: {headingCount}")

# Number of links
links = soup.find_all('a')
linkCount = len(links)
print(f"Total link count: {linkCount}")

# Number of paragraphs
paragraphs = soup.find_all('p')
paragraphCount = len(paragraphs)
print(f"Total paragraph count: {paragraphCount}")

# 4 -- Keyword Analysis --
print("\n-- Keyword Analysis --")
# Convert soup output to text
soupText = soup.get_text()

# Get user input for keyword
keyword = input("Enter keyword to search for: ").strip().lower()

# Get count and display keyword
soupTextWords = soupText.split()
keywordCount = 0

for word in soupTextWords:
    if word == keyword:
        keywordCount += 1
        

print(f"Total count for {keyword}: {keywordCount}")

# 5 -- Word Frequency Analysis --
print("\n-- Word Frequency Analysis --")
# Make dictionary to log word occurrences
wordCountAll = {}

for word in soupTextWords:
    if word in wordCountAll:
        wordCountAll[word] += 1
    else:
        wordCountAll[word] = 1
        
# Get top 5 most common words
sortedWords = sorted(wordCountAll.items(), key = lambda x: x[1], reverse=True)[:5]

print("Top 5 most frequently used words:")
for word, count in sortedWords:
    print(f"{word}: {count} times")

# 6 -- Finding the Longest Paragraph -- 
print("\n-- Finding the Longest Paragraph --")

longestParagraph = ""
maxWordCount = 0

for p in paragraphs:
    text = p.get_text(strip = True)
    wordCount = len(text.split())

    # Ignore empty and short paragraphs with less than 5 words
    if wordCount > maxWordCount and wordCount > 5:
        longestParagraph = text
        maxWordCount = wordCount

print("Longest paragraph:\n" + longestParagraph)
print()
print(f"Total word count: {maxWordCount}")

# 7 -- Visualizing Results --
labels = ['Headings', 'Links', 'Paragraphs']
values = [headingCount, linkCount, paragraphCount]

plt.bar(labels, values)
plt.title("Webpage Content Analysis")
plt.ylabel("Count")
plt.show()