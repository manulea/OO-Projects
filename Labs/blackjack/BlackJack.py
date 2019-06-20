import random


# BLACK JACK CLASS INCORPORATES RANDOM, AND SHUFFLE
# as of 3/2/2019 adding the suit, as in, uniquely identified 56 cards, works, but cannot be uniquely examined via suit.
#

class Deck:
    cards = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit = ["Spades", "Clubs", "Diamonds", "Hearts"]

    cardsInPlay = []
    cardCount = 56

    deckCards = ["" for x in range(cardCount)]

    count = 0
    count2 = 0

    def populate(self):
        for x in range(0, 4):
            for j in range(0, 14):
                self.deckCards[self.count] = ("" + self.cards[j])
                self.count = self.count + 1

        if self.count == self.cardCount:
            print("Deck has been filled")

    def shuffle(self):
        random.shuffle(self.deckCards)

    def getCard(self):
        if self.cardCount > 0:
            self.count2 = self.count2 + 1
            self.cardsInPlay.append(self.deckCards[self.count2 - 1])
            self.cardCount = self.cardCount - 1
            return self.cardsInPlay[self.count2 - 1]
        else:
            return "No more cards!"


class Player:
    hand = []
    playerTotal = 0

    # FUNCTIONS
    def __init__(self):
        pass

    def getCards(self):
        return self.hand


class House:
    def __init__(self):
        self.player = Player()
        self.deck = Deck()

        self.houseTotal = 0
        self.hand = []

    def play(self):
        hand = []
        houseTotal = 0
        player = Player()

        deck = Deck()
        deck.populate()
        deck.shuffle()

        play = True

        playerStand = False
        houseStand = False

        while play == True:

            # PLAYER FIRST
            validcharacter = False

            if playerStand == False:
                while validcharacter == False:
                    playerInput = input("Would you like a card? y/n: ")
                    if playerInput == 'y':
                        self.addCard("Player")
                        validcharacter = True
                    elif playerInput == 'n':
                        playerStand = True
                        validcharacter = True
                    else:
                        print("Invalid character.")

            elif playerStand == True:
                print("Player has stood")

            print("Player: " + self.printCards(self.player.hand) + " Total: " + str(self.player.playerTotal))
            if self.checkScore() == 0:
                play = False
                break

            # HOUSE
            if houseStand == False:
                self.addCard("House")
                print("House: " + self.printCards(self.hand) + " Total: " + str(self.houseTotal))
            if self.houseTotal >= 16:
                houseStand = True
            if self.checkScore() == 0:
                play = False
            break

    def checkScore(self):
        # DETERMINE THE SCORE AND RETURN THE APPROPRIATE STATUS
        if self.player.playerTotal == 21 or self.player.playerTotal > 21 or self.houseTotal == 21 or self.houseTotal > 21:
            if self.player.playerTotal == 21:
                print("Player has won!")
            if self.player.playerTotal > 21:
                print("Player has bust!")
            if self.houseTotal == 21:
                print("House has won!")
            if self.houseTotal > 21:
                print("House has bust!")
            return 0
        else:
            return 1

    def addCard(self, name):
        card = self.deck.getCard()
        number = card
        if card == "King" or card == "Queen" or card == "Jack":
            number = 10
        if name == "Player":
            if card == "Ace":
                isValid = False
                while isValid == False:
                    askforace = input("You scored an ace, would you like 1 or 11?: ")
                    if askforace == '1' or askforace == '11':
                        number = askforace
                        self.player.hand.append(card)
                        self.player.playerTotal = self.player.playerTotal + int(askforace)
                        isValid = True
                    else:
                        print("Not a valid number. Please enter 1 or 11: ")
            else:
                self.player.hand.append(card)
                self.player.playerTotal = self.player.playerTotal + int(number)

        if name == "House":
            if card == "Ace":
                if self.houseTotal > 16:
                    number = 1
                else:
                    number = 11

                self.hand.append(card)
                self.houseTotal = self.houseTotal + int(number)

            else:
                self.hand.append(card)
                self.houseTotal = self.houseTotal + int(number)

    # METHOD
    def printCards(self, hC):
        inputString = ""
        for x in hC:
            inputString = inputString + x + ", "

        return inputString

    def printTotal(self, opponent):
        print()


game = True

while game == True:
    house = House()
    house.play()
    game = False
