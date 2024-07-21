def count_words(file_path):
    my_dict = {}
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            sorted_words = sorted(content.split())  # Split the content into words and sort them
            sorted_sentence = ' '.join(sorted_words)  # Join the sorted words back into a string
            
            for word in sorted_words:
                if word in my_dict:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {str(e)}")
    
    return my_dict

# Example usage:
file_path = 'Q19/test.txt'
word_count_dict = count_words(file_path)
print(word_count_dict)
