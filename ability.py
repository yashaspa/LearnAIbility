def bold_first_letters(text, num_of_characters=2):
    '''
    Purpose: Edits all of the words in a given text. It makes the first few characters of all words bolded.
    Parameter: text to be edited
    Return Value: String with specified number of characters at the start of each word bolded.
    '''
    try:
        new_text = []
        for word in text.split():
            if len(word) < num_of_characters:
                bolded_part = '**' + word + '**'
            else:
                bolded_part = '**' + word[:num_of_characters] + '**' + word[num_of_characters:]
            new_text.append(bolded_part)
        
        return ' '.join(new_text)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def bold_terminal(text, num_of_characters=2):
    '''
    Purpose: Edits all of the words in a given text. It makes the first few characters of all words bolded for terminal display.
    Parameter: text to be edited
    Return Value: String with specified number of characters at the start of each word bolded.
    '''
    try:
        BOLD = '\033[1m'
        END = '\033[0m'
        
        new_text = []
        for word in text.split():
            if len(word) < num_of_characters:
                bolded_part = BOLD + word + END
            else:
                bolded_part = BOLD + word[:num_of_characters] + END + word[num_of_characters:]
            new_text.append(bolded_part)
        
        return ' '.join(new_text)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
text = "Hello there world"
print(bold_first_letters(text, 3))
print(bold_terminal(text, 2))
