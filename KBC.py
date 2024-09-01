import random

# Define the questions for each difficulty level
QUESTIONS = {
    "easy": [
        # Level 1
        [
            ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "C"],
            ["What is 2 / 2?", "1", "4", "5", "6", "A"],
            ["Which of these is a primary color?", "Green", "Purple", "Red", "Orange", "C"],
            ["What is the boiling point of water at sea level in Celsius?", "90", "100", "110", "120", "B"],
            ["Which ocean is the largest?", "Atlantic", "Indian", "Arctic", "Pacific", "D"]
        ],
        # Level 2
        [
            ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "B"],
            ["What is the largest organ in the human body?", "Heart", "Liver", "Skin", "Lung", "C"],
            ["Who was the first President of the United States?", "Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams", "B"],
            ["What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Pb", "A"],
            ["What year did the Titanic sink?", "1910", "1911", "1912", "1913", "C"]
        ],
        # Level 3
        [
            ["Who wrote 'Romeo and Juliet'?", "Shakespeare", "Dante", "Homer", "Chaucer", "A"],
            ["What is the smallest prime number?", "0", "1", "2", "3", "C"],
            ["In what year did World War I begin?", "1912", "1913", "1914", "1915", "C"],
            ["What element has the atomic number 1?", "Helium", "Hydrogen", "Lithium", "Beryllium", "B"],
            ["Who was the first person to step on the Moon?", "Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins", "B"]
        ]
    ],
    "medium": [
        # Level 1
        [
            ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", "C"],
            ["Who painted the Mona Lisa?", "Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "C"],
            ["What gas do plants use for photosynthesis?", "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", "C"],
            ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", "C"],
            ["Which planet is closest to the Sun?", "Venus", "Earth", "Mercury", "Mars", "C"]
        ],
        # Level 2
        [
            ["What is the smallest continent by land area?", "Africa", "Australia", "Europe", "South America", "B"],
            ["Who is the author of 'To Kill a Mockingbird'?", "Ernest Hemingway", "Harper Lee", "F. Scott Fitzgerald", "J.D. Salinger", "B"],
            ["What is the capital of Canada?", "Toronto", "Vancouver", "Ottawa", "Montreal", "C"],
            ["Which element is represented by the symbol 'Na'?", "Neon", "Sodium", "Nitrogen", "Nickel", "B"],
            ["What year did the Berlin Wall fall?", "1987", "1988", "1989", "1990", "C"]
        ],
        # Level 3
        [
            ["What is the longest river in the world?", "Nile", "Amazon", "Yangtze", "Mississippi", "B"],
            ["Who developed the theory of relativity?", "Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei", "B"],
            ["What is the largest desert in the world?", "Sahara", "Gobi", "Kalahari", "Antarctic", "D"],
            ["In which city would you find the Colosseum?", "Athens", "Rome", "Paris", "London", "B"],
            ["What is the name of the galaxy that contains our solar system?", "Andromeda", "Milky Way", "Whirlpool", "Sombrero", "B"]
        ]
    ],
    "hard": [
        # Level 1
        [
            ["What is the value of Planck’s constant?", "6.626 × 10^-34 J·s", "6.626 × 10^-34 kg·m^2·s^-1", "6.022 × 10^23 mol^-1", "9.81 m/s^2", "A"],
            ["Who formulated the laws of motion and universal gravitation?", "Niels Bohr", "Isaac Newton", "Galileo Galilei", "Albert Einstein", "B"],
            ["What is the most abundant gas in the Earth’s atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Argon", "C"],
            ["Which composer wrote the 'Four Seasons'?", "Ludwig van Beethoven", "Johann Sebastian Bach", "Antonio Vivaldi", "Wolfgang Amadeus Mozart", "C"],
            ["What is the chemical formula for table salt?", "NaCl", "KCl", "CaCO3", "H2SO4", "A"]
        ],
        # Level 2
        [
            ["What is the name of the effect where light bends around a massive object?", "Doppler Effect", "Gravitational Lensing", "Photoelectric Effect", "Compton Effect", "B"],
            ["Which scientist is known for the uncertainty principle?", "Werner Heisenberg", "Erwin Schrödinger", "Max Planck", "Albert Einstein", "A"],
            ["What is the main ingredient in traditional Japanese miso soup?", "Tofu", "Seaweed", "Miso Paste", "Soy Sauce", "C"],
            ["What is the capital of Mongolia?", "Ulaanbaatar", "Beijing", "Seoul", "Astana", "A"],
            ["In which century did the French Revolution occur?", "16th", "17th", "18th", "19th", "C"]
        ],
        # Level 3
        [
            ["What is the primary function of the mitochondria in a cell?", "Protein synthesis", "Energy production", "DNA replication", "Cell division", "B"],
            ["Which physicist is known for his work on quantum mechanics and quantum entanglement?", "Richard Feynman", "Erwin Schrödinger", "Max Born", "John Bell", "D"],
            ["What is the capital of the ancient empire of Sumer?", "Babylon", "Nineveh", "Ur", "Lagash", "C"],
            ["Who proposed the theory of evolution by natural selection?", "Gregor Mendel", "Charles Darwin", "Louis Pasteur", "Francis Crick", "B"],
            ["What mathematical constant is known as Euler's number?", "π", "e", "φ", "√2", "B"]
        ]
    ]
}


# Define the prize amounts for each level and difficulty
PRIZES = {
    "easy": [100, 200, 500, 1000, 2000],
    "medium": [1000, 2000, 5000, 10000, 20000],
    "hard": [10000, 20000, 50000, 100000, 200000]
}

# Function to play each level
def play_level(level, questions, prizes):
    for i in range(len(questions)):
        question = questions[i]
        print(f"\n\nQuestion for Rs. {prizes[i]}")
        print(f"{question[0]}")
        print(f"a. {question[1]}          b. {question[2]}")
        print(f"c. {question[3]}          d. {question[4]}")
        
        reply = input("Enter your answer: ").upper()
        
        if reply == question[-1]:
            print(f"Correct answer! You have won Rs. {prizes[i]}")
        else:
            print(f"Incorrect answer! You take home Rs. {prizes[i-1] if i > 0 else 0}")
            return prizes[i-1] if i > 0 else 0

    print(f"Congratulations! You have won Rs. {prizes[-1]}")
    return prizes[-1]

# Main game logic
def main_game():
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    
    if difficulty not in QUESTIONS:
        print("Invalid difficulty level selected!")
        return

    total_winnings = 0

    for level in range(3):
        print(f"\nLEVEL {level + 1} ({difficulty.upper()} MODE)")
        total_winnings = play_level(level, QUESTIONS[difficulty][level], PRIZES[difficulty])
        
        if total_winnings < PRIZES[difficulty][-1]:
            break
        
        if level < 2:
            if input("Press Enter to proceed to the next level or type 'quit' to exit with your winnings: ").lower() == "quit":
                break

    print(f"Thank you for playing! You take home Rs. {total_winnings}")

# Start the game
main_game()
