import time
import random

# List of sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Peter Piper picked a peck of pickled peppers.",
    "Now is the time for all good men to come to the aid of their country.",
    "She sells seashells by the seashore.",
    "Mary had a little lamb, its fleece was white as snow.",
    "Regs had a little dog, its fur was black as tar.",
    "Slowly, the slope of the hill declines leading into a cliff."
]

def typing_test():
    # Select a random sentence from the list
    sentence = random.choice(sentences)
    
    print("Welcome to the Typing Test!")
    print("===========================")
    print("Your task is to type the following sentence as quickly and accurately as you can.")
    print()
    
    print("Here is the sentence:")
    print(sentence)
    print()
    
    input("Press Enter when you are ready to start typing")
    print("Start typing now!")
    
    start_time = time.time()
    
    user_input = input()
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    # Output the results
    print()
    print("Thank you for typing!")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    
    # Providing a brief summary of the test
    print()
    print("Test Summary")
    print("============")
    print(f"Sentence: {sentence}")
    print(f"Your input: {user_input}")
    
    # End of the typing test
    print()
    print("We hope you enjoyed the test!")
    print("Feel free to run it back to improve your typing speed.")
    print("Goodbye!")

if __name__ == "__main__":
    typing_test()
