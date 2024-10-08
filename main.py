# Required libraries
import time
import random
import datetime
import os

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
    
    # Give a welcome to typing test screen
    print("Welcome to the Typing Test!")
    print("===========================")
    print("Your task is to type the following sentence as quickly and accurately as you can.")
    print()
    
    # Gives the sentence
    print("Here is the sentence:")
    print(sentence)
    print()
    
    # Make the input work properly now
    input("Press Enter when you are ready to start typing")
    print("Start typing now!")
    
    # Declaring all vars
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
    # Check mismatches
    if not mismatches:
        print("Congratulations! Your typing was perfect!")
    else:
        print("There were some mistakes:")
        for index, orig_word, user_word in mismatches:
            print(f"Word {index + 1}: Original '{orig_word}' - Your input '{user_word}'")
    
    accuracy = (1 - len(mismatches) / len(sentence.split())) * 100
    print(f"Typing accuracy: {accuracy:.2f}%")
    
    # Add better functionality
    print()
    print("Additional Features:")
    
    # Give Advice
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
    
def display_instructions():
    print("Instructions:")
    print("1. Read the sentence carefully before you start typing.")
    print("2. Type the sentence as accurately as possible.")
    print("3. Press Enter to submit your typing.")
    print("4. Review your results and try to improve with each attempt.\n")

def track_typing_speed(start_time, end_time):
    typing_duration = end_time - start_time
    if typing_duration < 10:
        return "Excellent speed!"
    elif typing_duration < 30:
        return "Good speed!"
    else:
        return "You can improve your speed!"

def save_best_score(score):
    with open("best_score.txt", "w") as file:
        file.write(f"{score:.2f}")

def display_best_score(best_score):
    print(f"Your best score is: {best_score:.2f} seconds\n")

def show_typing_statistics(user_input, original_sentence):
    total_chars = len(original_sentence)
    typed_chars = len(user_input)
    percent_accurate = (typed_chars / total_chars) * 100
    print(f"Characters typed: {typed_chars}/{total_chars}")
    print(f"Typing accuracy: {percent_accurate:.2f}%")

# Display mistakes function
def display_mistake_details(mismatches):
    if mismatches:
        print("Mistake Details:")
        for index, orig_word, user_word in mismatches:
            print(f"Word {index + 1}: Original '{orig_word}' - Your input '{user_word}'")
    else:
        print("No mistakes found.")

# Get current time
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save the test function
def log_typing_test(session_details):
    with open("typing_test_log.txt", "a") as log_file:
        log_file.write(f"{session_details}\n")

# Generate a report
def generate_summary_report(elapsed_time, accuracy, mismatches):
    report = f"Typing Test Summary Report\n"
    report += f"=========================\n"
    report += f"Test Date and Time: {get_current_time()}\n"
    report += f"Time Taken: {elapsed_time:.2f} seconds\n"
    report += f"Typing Accuracy: {accuracy:.2f}%\n"
    if mismatches:
        report += "Mistakes:\n"
        for index, orig_word, user_word in mismatches:
            report += f"  Word {index + 1}: Original '{orig_word}' - Your input '{user_word}'\n"
    else:
        report += "No mistakes found.\n"
    return report

# Display how long session was
def display_session_duration(start_time, end_time):
    duration = end_time - start_time
    print(f"Total session duration: {duration:.2f} seconds")

# Display word count
def display_word_count(sentence, user_input):
    original_word_count = len(sentence.split())
    typed_word_count = len(user_input.split())
    print(f"Original sentence word count: {original_word_count}")
    print(f"Typed sentence word count: {typed_word_count}")

# Suggest typing software 
def suggest_typing_software():
    print("\nFor further improvement, you might consider using specialized typing software.")
    print("Some popular ones include TypingClub, NitroType, and Fast.com")

# Show typing performance
def review_typing_performance():
    review = input("Would you like to review your typing performance statistics? (yes/no): ").strip().lower()
    return review == 'yes'

# Function to select a random sentence
def select_sentence():
    return random.choice(sentences)

# Function to get user input and track elapsed time
def get_user_input(sentence):
    print("Here is the sentence:")
    print(sentence)
    input("Press Enter when you are ready to start typing")
    print("Start typing now!")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    return user_input, end_time - start_time

# Function to calculate typing accuracy
def calculate_accuracy(original, mismatches):
    return (1 - len(mismatches) / len(original.split())) * 100

# Function to provide feedback based on mismatches and accuracy
def provide_feedback(mismatches, accuracy):
    if not mismatches:
        print("Congratulations! Your typing was perfect!")
    else:
        print("There were some mistakes:")
        for index, orig_word, user_word in mismatches:
            print(f"Word {index + 1}: Original '{orig_word}' - Your input '{user_word}'")
    print(f"Typing accuracy: {accuracy:.2f}%")

# Function to prepare for a new typing test
def prepare_for_new_test():
    print("\nPreparing for a new typing test...")
    time.sleep(2)
    print("You are now ready for a new test!\n")

# Function to handle replay logic
def replay_test():
    return input("Would you like to take another typing test? (yes/no): ").strip().lower() == 'yes'

# Main function
def typing_test():
    best_score = float('inf')
    if os.path.exists("best_score.txt"):
        with open("best_score.txt", "r") as file:
            best_score = float(file.read().strip())

    while True:
        sentence = select_sentence()
        user_input, elapsed_time = get_user_input(sentence)
        mismatches = check_accuracy(sentence, user_input)
        accuracy = calculate_accuracy(sentence, mismatches)
        
        print("\nThank you for typing!")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(track_typing_speed(0, elapsed_time))
        print("Test Summary")
        print("============")
        print(f"Sentence: {sentence}")
        print(f"Your input: {user_input}")
        
        provide_feedback(mismatches, accuracy)
        show_typing_statistics(user_input, sentence)
        display_mistake_details(mismatches)
        
        if elapsed_time < best_score:
            save_best_score(elapsed_time)
            print("Congratulations! You've set a new best time!")
        
        display_word_count(sentence, user_input)
        display_session_duration(0, elapsed_time)
        
        if review_typing_performance():
            report = generate_summary_report(elapsed_time, accuracy, mismatches)
            print("\n" + report)
            log_typing_test(report)
        
        suggest_typing_software()
        
        if not replay_test():
            print("Goodbye! Have a great day!")
            break
        prepare_for_new_test()

# Run the main function 
if __name__ == "__main__":
    typing_test()
