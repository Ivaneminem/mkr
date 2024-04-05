def count_words_and_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    word_count = len(text.split())

    sentence_delimiters = ['.', '!', '?', '...']
    sentence_count = sum(text.count(delimiter) for delimiter in sentence_delimiters)

    return word_count, sentence_count

def write_counts_to_file(word_count, sentence_count, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("Кількість слів у файлі: {}\n".format(word_count))
        file.write("Кількість речень у файлі: {}\n".format(sentence_count))

input_file_path = 'C:/Універ/2 курс/2 семестр/cicd/МКР/cicd.txt'
output_file_path = 'counts.txt'

word_count, sentence_count = count_words_and_sentences(input_file_path)
write_counts_to_file(word_count, sentence_count, output_file_path)

print("Результати були записані у файл", output_file_path)









