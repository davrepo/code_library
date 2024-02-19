import torch.nn as nn
import torch.optim as optim
import torch
torch.manual_seed(8446)

def load_langid(path):
    text = []
    labels = []
    for line in open(path):
        tok = line.strip().split('\t')
        labels.append(tok[0])
        text.append(tok[1])
    return text, labels

class LangId(nn.Module):
    def __init__(self, vocab_size):
        super(LangId, self).__init__()
        self.input = nn.Linear(vocab_size, 15)
        self.hidden1 = nn.Linear(15, 20)
        self.hidden2 = nn.Linear(20, 3)

    def forward(self, x):
        x = torch.tanh(self.input(x))
        x = torch.tanh(self.hidden1(x))
        x = self.hidden2(x)
        return x

label2idx = {'da':0, 'nl':1, 'en':2}
idx2label = ['da', 'nl', 'en']

def toMatrix(data, lookup):
    # convert data to matrix
    vocab_size = len(idx2char)
    matrix = torch.zeros((len(data),len(lookup)), dtype=torch.float)

    for sentenceIdx, sentence in enumerate(data):
        for char in sentence:
            charIdx = lookup[char]
            matrix[sentenceIdx][charIdx] = 1
    return matrix

wooki_train_text, wooki_train_labels = load_langid('langid-data/wookipedia_langid.train.tok.txt')

char2idx = {}
idx2char = []
for sent in wooki_train_text:
    for char in sent:
        if char not in char2idx:
            char2idx[char] = len(idx2char)
            idx2char.append(char)

print(char2idx)
print(idx2char)

train_data = toMatrix(wooki_train_text, char2idx)    
train_labels = torch.tensor([label2idx[entry] for entry in wooki_train_labels])

langClassifier = LangId(len(idx2char))

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(langClassifier.parameters(), lr=0.00001, momentum=0.9)

for epoch in range(20):  # loop over the dataset multiple times
    # zero the parameter gradients
    optimizer.zero_grad()
    for batchIdx in range(500):
        beg = batchIdx * 30
        end = (batchIdx+1) * 30

        # Run the forward pass
        outputs = langClassifier(train_data[beg:end])
        # Calculate the loss
        loss = criterion(outputs, train_labels[beg:end])
        # Do the backpropagation
        loss.backward()
        optimizer.step()
    print(epoch, loss.item())
        
torch.save(langClassifier, 'model.th')

wooki_dev_text, wooki_dev_labels = load_langid('langid-data/wookipedia_langid.dev.tok.txt')

dev_data = toMatrix(wooki_dev_text, char2idx)    
dev_labels = torch.tensor([label2idx[entry] for entry in wooki_dev_labels])

logit = langClassifier.forward(dev_data)
predicted = logit.argmax(dim=1)
cor = 0
for pred, gold in zip(predicted, dev_labels):
    if idx2label[pred] == idx2label[gold.item()]:
        cor += 1

print(cor/len(wooki_dev_labels)) 


