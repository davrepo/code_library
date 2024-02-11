import sys

if len(sys.argv) < 3:
    print('please provide gold file and your output file')
    exit(1)

def readTok(path):
    data = []
    for line in open(path):
        parts = line.strip().split('\t')
        data.append(parts[-1].split(' '))
    return data

gold_data = readTok(sys.argv[1])
pred_data = readTok(sys.argv[2])

assert len(gold_data) == len(pred_data), 'Files do not have same length'

def text2spans(wordlist):
    """
    gets as input a list of strings, and outputs their 
    start/end - character indices as a set. Exampe:
    input: ['this', 'is', 'a', 'test']
    output: {(0,4), (4,6), (6,7), (7,11)}
    """
    start_idx = 0
    spans = []
    for word in wordlist:
        end_idx = start_idx + len(word)
        spans.append((start_idx, end_idx))
        start_idx = end_idx
    return spans

def count(gold_tok, pred_tok):
    gold_spans = text2spans(gold_tok)
    pred_spans = text2spans(pred_tok)    
    tp = 0
    fp = 0
    fn = 0
    err_idxs_gold = set()
    err_idxs_pred = set()
    for gold_span_idx, gold_span in enumerate(gold_spans):
        if gold_span in pred_spans:
            tp += 1
        else:
            fn += 1
            err_idxs_gold.add(gold_span_idx)
        
    for pred_span_idx, pred_span in enumerate(pred_spans):
        if pred_span not in gold_spans:
            fp += 1
            err_idxs_pred.add(pred_span_idx)
    return tp, fp, fn, err_idxs_gold, err_idxs_pred

tps = 0
fps = 0
fns = 0
for gold_tok, pred_tok in zip(gold_data, pred_data):
    if ''.join(gold_tok) != ''.join(pred_tok):
        print('the character you returned are not the same as the ones in the gold tokenization. The character indices will not match, and you will get much lower scores. Please check your code and ensure that you return exactly the same characters (only the whitespaces may differ). Below we will print the gold tokenization and your tokenization without whitespaces for easier debugging:')
        print(''.join(gold_tok))
        print(''.join(pred_tok))
        exit(1)
    tp, fp, fn, error_idxs_gold, error_idxs_pred = count(gold_tok, pred_tok)
    tps += tp
    fps += fp
    fns += fn

    #print(tp, fp, fn)
    if fp != 0 or fn != 0:
        for word_idx, word in enumerate(gold_tok):
            if word_idx in error_idxs_gold:
                print("\033[91m{}\033[00m" .format(word), end = ' ')
            else:
                print(word, end = ' ')
        print()
        for word_idx, word in enumerate(pred_tok):
            if word_idx in error_idxs_pred:
                print("\033[91m{}\033[00m" .format(word), end = ' ')
            else:
                print(word, end = ' ')
        print('\n')

precision = tps / (tps+fps)
recall = tps / (tps+fns)
f1 = 2 * ((precision*recall)/(precision+recall))

print()
print('precision: {:.2f}'.format(precision * 100)) 
print('recall: {:.2f}'.format(recall * 100)) 
print('f1: {:.2f}'.format(f1 * 100)) 


