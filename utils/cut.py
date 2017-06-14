import jieba

jieba.set_dictionary('../../zh-dict/dict_zh_small.txt')
jieba.load_userdict('../../zh-dict/ec_item_zh.txt')
jieba.load_userdict('../../zh-dict/user_dict_zh.txt')
jieba.load_userdict('../../zh-dict/acg.txt')

result = []
with open('sentence.txt') as f:
    for line in f:
        line = line.strip()
        tokens = [x for x in jieba.cut(line) if x != ' ']
        # print(tokens)
        sent = ' '.join(tokens)
        result.append(sent)


with open('sent_cut.txt', 'w') as f:
    for r in result:
        print(r, file=f)