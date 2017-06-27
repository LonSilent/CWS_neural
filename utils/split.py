if __name__ == '__main__':
    data_path = '../data/train-ec'
    ratio = 0.8
    line = 1000
    train = int(line * ratio)
    test = line - train

    sentences = []
    with open(data_path) as f:
        for line in f:
            sentences.append(line.strip())
    with open('../data/train/train_{}.txt'.format(train), 'w') as f:
        for s in sentences[:train]:
            print(s, file=f)
    with open('../data/test/test_gt_{}.txt'.format(test), 'w') as f:
        for s in sentences[train:]:
            print(s, file=f)