import os
def merge_files():
    base_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(base_dir, "file1.txt")
    file_path2 = os.path.join(base_dir, "file2.txt")
    file_rezult = os.path.join(base_dir, "rezult.txt")
    def read_matches(filename):
        matches = set()
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith("Team: "):
                    match = line.split(", ")[0]  # Витягуємо тільки назву команд
                    matches.add(match)
        return matches

    # Зчитуємо матчі з двох файлів
    file1_matches = read_matches(file_path1)
    file2_matches = read_matches(file_path2)

    # Знаходимо спільні матчі
    common_matches = file1_matches.intersection(file2_matches)

    # Записуємо результати у третій файл
    with open(file_rezult, 'w', encoding='utf-8') as output_file:
        with open(file_path1, 'r', encoding='utf-8') as file1:
            for line in file1:
                if any(match in line for match in common_matches):
                    output_file.write(line)

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    file_path1 = os.path.join(base_dir, "file1.txt")
    print(file_path1)