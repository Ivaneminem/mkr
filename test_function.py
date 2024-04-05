import pytest
import tempfile
from МКР import count_words_and_sentences, write_counts_to_file

@pytest.fixture
def sample_text():
    return "This is a sample text. It has multiple words and sentences! Let's test it."

def test_count_words_and_sentences(sample_text):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(sample_text)

    word_count, sentence_count = count_words_and_sentences(temp_file.name)

    assert word_count == 14
    assert sentence_count == 3

@pytest.mark.parametrize("word_count, sentence_count", [
    (10, 2),
    (15, 4),
    (8, 1)
])
def test_write_counts_to_file(tmp_path, word_count, sentence_count):
    output_file_path = tmp_path / "counts.txt"
    write_counts_to_file(word_count, sentence_count, output_file_path)

    with open(output_file_path, 'r') as file:
        content = file.readlines()

    assert len(content) == 2
    assert content[0].strip() == f"Кількість слів у файлі: {word_count}"
    assert content[1].strip() == f"Кількість речень у файлі: {sentence_count}"
