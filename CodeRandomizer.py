# Program that analyzes the code and replaces it with gibberish symbols
# The code is used to modify C / C++ code
# Code must first be in the same folder as this Python file
# By: Matas Sabaliauskas
# Email: sabaliauskas.matas@yahoo.com

import random
import string


def randomize_code():
    # Insert your code file name here:
    file = 'code_2.cpp'
    file_split = file.split('.')
    file_new = file_split[0] + '_randomized' + '.' + file_split[1]

    # random_char = string.ascii_lowercase # You can use this to have random strings instead
    random_char = 'e' # You can use this to replace all code with increments of this character (e.g. e, ee, eee, etc.)
    random_char_new = ''
    unchanged_lines = []
    define_lines = []
    code_lines = []

    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        if line == '#include <iostream>\n' or line == '#include <string>\n':
            print('unchanged line: ', line.strip())
            unchanged_lines.append(line)
        elif line == '\n':
            print('empty line found!')
            line = line
        else:
            line_split = line.split()
            print('line to be changed: ', line.strip())

            # This ensures that the words in quote marks "" are grouped together
            remaining_word, comment_search = search(line, str('//'))
            if comment_search != '':
                print('Comment Line! No line will be written.')

            else:
                remaining_word, quotation_mark_search = search(line, str('"'))
                if quotation_mark_search != '':
                    print('Quotation Mark Symbol Found!')
                    line_split = remaining_word.copy()
                    print('Updated line_split: ', line_split)
                for word in line_split:
                    # random_char_new = (''.join(random.choice(random_char) for i in range(5))) # You can use this to have random strings instead
                    random_char_new += random_char # You can use this to replace all code with increments of this character (e.g. e, ee, eee, etc.)
                    text_temp = '#define ' + random_char_new + ' ' + word + '\n'
                    define_lines.append(text_temp)
                    code_lines.append(random_char_new + ' ')
                code_lines.append('\n')

    with open(file_new, 'w') as f:
        for unchanged_line in unchanged_lines:
            f.write(f'{unchanged_line}')

        for define_line in define_lines:
            f.write(f'{define_line}')

        f.write('\n')

        for code_line in code_lines:
            f.write(f'{code_line}')

        f.write('\n//Old code: \n\n/*\n')
        for line in lines:
            f.write(f'{line}')
        f.write('\n*/')


def search(word_list, search_char):
    # This function looks for a string which contains "" symbols
    # e.g.
    # line to be changed: cout << "Main: Input Array Size = " << size << "\n";
    # Would normally become ['cout << ', '"Main: ', 'Input Array Size = ','"', '<< size << ', '"\n";']
    # This splits it into:
    # Remaining word list:  ['\tcout << ', '"Main: Input Array Size = "', ' << size << ', '"\\n"', ';\n']

    word_list = word_list.split(search_char)
    new_word_list = []
    new_word = ''
    for index, item in enumerate(word_list):
        if (index + 1) % 2 == 0:
            new_word_list.append(search_char + item + search_char)
            new_word += item
        else:
            new_word_list.append(item)

    # print('word_list_final = ', new_word_list)
    return new_word_list, new_word


if __name__ == '__main__':
    randomize_code()
