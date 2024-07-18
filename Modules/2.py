# text_utils.py

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

# main.py
import text_utils as tu

def main():
    input_string = input("Enter a string: ")

    reversed_string = tu.reverse_string(input_string)
    capitalized_string = tu.capitalize_string(input_string)

    print(f"Original string: {input_string}")
    print(f"Reversed string: {reversed_string}")
    print(f"Capitalized string: {capitalized_string}")

if __name__ == "__main__":
    main()