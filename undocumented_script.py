def process_numbers_by_parity(input_number_list):
    """
    Processes each number in a list based on its parity (even or odd).

    Even numbers are multiplied by 2.
    Odd numbers are multiplied by 3.
    """
    processed_list = [
        number * 2 if number % 2 == 0 else number * 3 
        # Multiplies by 2 if even, or 3 if odd.
        for number in input_number_list
    ]
    return processed_list



def generate_formatted_string(list_of_words):
    """
    Formats words based on its length.

    Strings that are longer than 5 characters are converted to uppercase.
    Strings that are 5 characters or shorter are converted to lowercase.

    Args:
        list_of_words (list[str]): A list of strings to be processed.

    Returns:
        str: A string containing all formatted words separated by a single 
        space
    """
    formatted_words = [
        word.upper() if len(word) > 5 else word.lower()
        for word in list_of_words
    ]
    return " ".join(formatted_words)

def main():
    '''
    The main function. Defines example data and prints the results 
    of the utility functions. 
    '''
    # Meaningful variable names following PEP 8 conventions. 
    integer_list = [1, 2, 3, 4, 5, 6, 7]
    word_list = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = process_numbers_by_parity(integer_list)
    processed_strings = generate_formatted_string(word_list)

    print("Processed Numbers:", processed_nums)
    print("Processed Sentence:", processed_strings)


if __name__ == "__main__":
    main()
