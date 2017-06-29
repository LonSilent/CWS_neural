# python3 env

if __name__ == '__main__':
    punc = []
    with open('../data/symbol_zh.txt', 'r') as f:
        for line in f:
            punc.append(line.strip())

    sentence = []
    lines = []
    # raw data
    with open('../data/sentence_desc.txt') as f:
        for line in f:
            l = line.strip().replace(' ', '').replace('　','')
            sentence.append(l)
            lines.append(line.strip())

    result = []
    flag = 0
    count = 0
    # train data
    with open('desc_1000.txt') as f:
        for line in f:
            flag = 0
            s = line.strip().replace(' ', '').replace('　','')
            for i, l in enumerate(sentence):
                if s == l:
                    result.append(lines[i])
                    flag = 1
                    break
            count += 1
            if flag == 0 :
                print(line.strip())
                print(count)

    # test data
    with open('test_desc_1000.txt', 'w') as f:
        for r in result:
            print(r, file=f)
