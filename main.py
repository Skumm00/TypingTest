#required libraries
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
    "Slowly, the slope of the hill declines leading into a cliff.",
    "The greater the challenge, the greater the reward",
    "How much wood can a woodchucker chuck if he chucks and chucks and chucks",
    "How is a rat possible to make such remarks", 
    "The weird farmer came from Arizona and planted eggplants"
]

def check_accuracy(original, user_input):
    # Highlight mismatches in the user's input
    mismatches = []
    original_words = original.split()
    user_words = user_input.split()
    
    for i, (orig_word, user_word) in enumerate(zip(original_words, user_words)):
        if orig_word != user_word:
            mismatches.append((i, orig_word, user_word))
    
    return mismatches

def typing_test():
    # Generate a random number to select a sentence
    rannum = random.randint(0, len(sentences) - 1)
    sentence = sentences[rannum]
    
    #Give a welcome to typing test screen
    print("Welcome to the Typing Test!")
    print("===========================")
    print("Your task is to type the following sentence as quickly and accurately as you can.")
    print()
    
    #Gives the sentence
    print("Here is the sentence:")
    print(sentence)
    print()
    
    #Make the input work properly now
    input("Press Enter when you are ready to start typing")
    print("Start typing now!")
    
    #declaring all vars
    start_time = time.time()
    
    user_input = input()
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    # Check if user input matches the original sentence
    mismatches = check_accuracy(sentence, user_input)
    
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
    #check mismatches
    if not mismatches:
        print("Congratulations! Your typing was perfect!")
    else:
        print("There were some mistakes:")
        for index, orig_word, user_word in mismatches:
            print(f"Word {index + 1}: Original '{orig_word}' - Your input '{user_word}'")
    
    accuracy = (1 - len(mismatches) / len(sentence.split())) * 100
    print(f"Typing accuracy: {accuracy:.2f}%")
    
    #add better functionality
    print()
    print("Additional Features:")
    

    #Give Advice
    if accuracy < 80:
        print("Tip: Try practicing with simpler sentences or use typing practice tools.")
    else:
        print("Great job! Keep practicing to maintain and improve your skills.")
    
    # Replay
    replay = input("Would you like to take another typing test? (yes/no): ").strip().lower()
    if replay == 'yes':
        typing_test()
    else:
        print("Goodbye! Have a great day!")
    
declareall()
#run the main function 
if __name__ == "__main__":
    typing_test()
