import re


def has_two_or_more_numbers(line):
    numbers = re.findall(r'\d', line)
    return len(numbers) >= 3


def remove_repeat():
    with open('list.txt', 'r+') as f:
        lines = f.readlines()
        exist_lines = {}
        new_lines = []
        for line in lines:
            if line in exist_lines:
                continue
            if has_two_or_more_numbers(line):
                continue
            exist_lines[line] = 1
            new_lines.append(line)
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)


if __name__ == '__main__':
    remove_repeat()
