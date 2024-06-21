# mood_responses.py

def mood_response(mood):
    if mood.lower() == 'happy':
        return "Great to hear that you're happy!"
    elif mood.lower() == 'sad':
        return "Cheer up! Tomorrow is another day."
    elif mood.lower() == 'excited':
        return "That's awesome! Exciting times ahead!"
    else:
        return "Interesting... Tell me more about that."

# main.py
import mood_responses

def main():
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))

if __name__ == "__main__":
    main()

