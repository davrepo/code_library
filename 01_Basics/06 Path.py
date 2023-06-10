import random 

class Card:
    # class attribute / class variable: shared by all objects of a class
    # representes class-wide info, belongs to the class, not to specific object of the class
    # define class attributes by declare + assign inside class definition, 
    # but outside class's methods or properties. 
    # Class attributes exist as soon as you import their class's definition
    # Constants are named with all caps by convention
    FACES = ['Ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        # face, suit, image_name are read-only properties bc no setter methods
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    # image_name property is created dynamically by getting the Card object's
    # string representation with str(self)
    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'  #str(self) calls __str__ special method

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"     

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    # special method __format__ is called when a card object is formatted as a string,
    # such as in an f-string. When DeckOfCards __str__ method uses f-string on card,
    # card's __format__ method is invoked with format specifier passed as format parameter
    def __format__(self, format):
        """Return formatted string representation."""
        return f'{str(self):{format}}'


class DeckOfCards:
    """Deck class represents a deck of Cards."""
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):  
            self._deck.append(Card(Card.FACES[count % 13], 
                Card.SUITS[count // 13]))

    def shuffle(self):
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)    

    def deal_card(self):
        """Return one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None  

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        
        return s

deck_of_cards = DeckOfCards()

print(deck_of_cards)

deck_of_cards.shuffle()

print(deck_of_cards)

deck_of_cards.deal_card()
# Card(face='Queen', suit='Diamonds')

card = deck_of_cards.deal_card()
str(card)
# 'Jack of Diamonds'

card.face = '10'    # card object is immutable because has no setter method, i.e. read-only
# AttributeError: can't set attribute
card._face = '10'   # but can manipulate card's private attribute
print(card)         
# 10 of Hearts

card.image_name
# '10_of_Hearts.png'




# Display card images with Matplotlib
deck_of_cards = DeckOfCards()

# Enable Matplotlib in IPython with magic, see
# https://ipython.readthedocs.io/en/stable/interactive/magics.html
%matplotlib

# Create the Base `Path` for Each Image
from pathlib import Path

path = Path('.').joinpath('card_images')

# Import the Matplotlib Features
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Create the `Figure` and `Axes` Objects
figure, axes_list = plt.subplots(nrows=4, ncols=13)

# Configure the `Axes` Objects and Display the Images
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

# Maximize the Image Sizes
figure.tight_layout()

### Shuffle and Re-Deal the Deck
deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)
