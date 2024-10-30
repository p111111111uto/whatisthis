def reverse_ambiguous_letters(phrase):
    replacements = {
        'I': 'i',
        'l': 'L',
        '1': 'one',
        '0': 'zero'
    }

    converted_phrase = ''

    for char in phrase:
        if char in replacements:
            converted_phrase += replacements[char]
        else:
            converted_phrase += char

    return converted_phrase

def main():
    phrase = input('Enter a phrase: ')
    converted = reverse_ambiguous_letters(phrase)
    print('\nConverted phrase:\n', converted)

if __name__ == '__main__':
    main()