import sys

if len(sys.argv) < 3:
    print('please provide original and annotated file:')
    print('python3 check-pos.py 12345.pos.txt 12345.pos.ann.txt')
    exit(1)

tags = {'ADJ', 'ADP', 'PUNCT', 'ADV', 'AUX', 'SYM', 'INTJ', 'CCONJ', 'X', 'NOUN', 'DET', 'PROPN', 'NUM', 'VERB', 'PART', 'PRON', 'SCONJ'}

numErrs = 0
lineCounter = 1
for lineOrig, lineAnn in zip(open(sys.argv[1]), open(sys.argv[2])):
    if numErrs > 10:
        print('More than 10 errors found, this probably means that you mixed up the order of the file or removed/added a line somewhere (try to find it in the errors printed above).')
        exit(1)

    lineOrig = lineOrig.strip()
    lineAnn = lineAnn.strip()
    # if line that does not need annotation
    if lineOrig.startswith('# text = ') or len(lineOrig.strip()) == 0:
        if lineOrig != lineAnn:
            print('ERROR: line ' + str(lineCounter) + ' annotation differs from original file, but should be kept untouched:')
            print('orig:       ' + lineOrig)
            print('annotation: ' + lineAnn)
            print()
            numErrs += 1
    # line needs annotation
    else:
        ann = lineAnn.split()
        ori = lineOrig.split()
        if len(ann) < 2:
            print('ERROR: no annotation provided for token at line ' + str(lineCounter) + ':')
            print('orig: ' + lineOrig)
            print()
            numErrs += 1
        elif len(ann) > 2:
            print('ERROR: too many annotations found for token at line ' + str(lineCounter) + ' every token can only be assigned one POS tag')
            print('annotation: ' + lineAnn)
            print()
            numErrs += 1
        else:
            if ann[1].upper() not in tags:
                print('ERROR: tag ' + ann[1] + ' is not part of the UPOS-tagset (line ' + str(lineCounter) + '):')
                print('annotation: ' + lineAnn)
                print()
                numErrs += 1
            if ann[0] != ori[0]:
                print('ERROR: a word is changed in the annotated file at line ' + str(lineCounter) + '. You are not supposed to edit the words:')
                print('orig:       ' + lineOrig)
                print('annotation: ' + lineAnn)
                print()
                numErrs += 1
                
    lineCounter += 1 

if numErrs != 0:
    print('please fix these errors')
else:
    print('Succesfully passed check!')

