import random
import time
def generate_random_text():
    text = "This is a simple Typing Speed Tester application. It calculates your typing speed in words per minute (WPM). Try to type the following text as quickly and accurately as possible. Good luck!"
    return text

def calculate_wpm(input_text, elapsed_time):
    words = input_text.split()
    num_words = len(words)
    seconds = elapsed_time / 60  # Convert milliseconds to seconds
    wpm = (num_words / seconds) if seconds > 0 else 0
    return wpm

def typing_speed_test():
    random_text = generate_random_text()
    print(random_text)
    input("Press Enter to start typing...")
    start_time = time.time()
    user_input = input("Type the above text: ")
    end_time = time.time()
    elapsed_time = end_time - start_time

    wpm = calculate_wpm(random_text, elapsed_time)
    accuracy = calculate_accuracy(random_text, user_input)

    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original_text, user_text):
    original_words = original_text.split()
    user_words = user_text.split()
    correct_words = 0

    for ow, uw in zip(original_words, user_words):
        if ow == uw:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100
    return accuracy

if __name__ == "__main__":
    typing_speed_test()
