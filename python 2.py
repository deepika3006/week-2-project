def count_words(text):
    """
    Function to count the number of words in a given text.
    
    Args:
    text (str): The input text to count words from.
    
    Returns:
    int: The number of words in the input text.
    """
    # If the input text is empty or contains only whitespace, return 0
    if not text.strip():
        return 0
    
    # Split the text into words using whitespace as delimiter
    words = text.split()
    
    # Return the number of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Check if the input is empty
    if not user_input:
        print("Error: Input cannot be empty.")
        return
    
    # Count the number of words in the input
    word_count = count_words(user_input)
    
    # Print the word count
    print("The number of words in the input:", word_count)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
