def str(xa):
    return xa
    
    
def str(xb):
    return xb
    
    
def str(xc):
    return xc
     
     
def str(xd):
    return xd
    
xa="Coding allows humans to communicate with these devices. Modern technology such as traffic lights, calculators, smart TVs, and cars use internal coding systems. Since computers do not communicate like humans, coding acts as a translator. Code converts human input into numerical sequences that computers understand."

xb = "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.It is used for:web development (server-side),software development,mathematics,system scripting." 

xc = "Data science combines math and statistics, specialized programming, advanced analytics, artificial intelligence (AI) and machine learning with specific subject matter expertise to uncover actionable insights hidden in an organizations data. These insights can be used to guide decision making and strategic planning."

xd = "Artificial intelligence: (AI) generally refers to processes and algorithms that are able to simulate human intelligence, including mimicking cognitive functions such as perception, learning and problem solving. Machine learning and deep learning (DL) are subsets of AI.Machine learning: (ML) is a subset of AI that falls within the (limited memory) category in which the AI (machine) is able to learn and develop over time."
print("Search")
print("1.What is coding?")
print("2.What is python?")
print("3.What is data science?")
print("4.What is AI/ML?")

while True:
    question = input("Ask a question(1/2/3/4): ")
    if question == '1':
        print(xa)
    elif question == '2':
        print(xb)
    elif question == '3':
        print(xc)
    elif question =='4':
        print(xd)
        
    next = input("Let's continue(yes/no): ")
    if next == 'no':
        break

output:
Search
1.What is coding?
2.What is python?
3.What is data science?
4.What is AI/ML?
Ask a question(1/2/3/4): 1
Coding allows humans to communicate with these devices. Modern technology such as traffic lights, calculators, smart TVs, and cars use internal coding systems. Since computers do not communicate like humans, coding acts as a translator. Code converts human input into numerical sequences that computers understand.
Let's continue(yes/no): yes
Ask a question(1/2/3/4): 2
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.It is used for:web development (server-side),software development,mathematics,system scripting.
Let's continue(yes/no): no

