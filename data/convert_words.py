def main():
    input_file_path = "data/word_source_5_characters.txt"
    input_file_path_2 = "data/word_source_3_to_4_characters.txt"
    output_file_path = "wordle_words_3.txt"
    output_file_path_2 = "wordle_words_4.txt"
    output_file_path_3 = "wordle_words_5.txt"
    three_letter_words = []
    four_letter_words = []
    five_letter_words = []

    with open(input_file_path, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 5:
                five_letter_words.append(word)

    with open(input_file_path_2, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 3:
                three_letter_words.append(word)
            elif len(word) == 4:
                four_letter_words.append(word)

    with open(output_file_path, 'w') as f:
        for word in three_letter_words:
            f.write(word + "\n")

    with open(output_file_path_2, 'w') as f:
        for word in four_letter_words:
            f.write(word + "\n")

    with open(output_file_path_3, 'w') as f:
        for word in five_letter_words:
            f.write(word + "\n")     

    print(f"Found {len(three_letter_words)} three-letter words, "
          f"{len(four_letter_words)} four-letter words, and "
          f"{len(five_letter_words)} five-letter words.")

if __name__ == "__main__":
    main()