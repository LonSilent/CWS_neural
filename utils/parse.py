import json
import re

symbol = ['<br>', '●', '※', '★', '◆', '■']

if __name__ == '__main__':
    result = []
    with open('output2.json') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            position = line.find(',', 0, 60)
            line = '{' + line[position + 2:]
            print(line)
            item = json.loads(line.strip())
            title = item['Title']
            result.append(title)
            if 'Description' in item:
                desc = item['Description'].replace('<br>', ' ')
                result.append(desc)

    # print(result)
    with open('sentence.txt', 'w') as f:
        for r in result:
            print(r, file=f)
            