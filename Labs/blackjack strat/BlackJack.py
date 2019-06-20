import random

# basic blackjack game that comes with 2 modes -> manual selection, vs automatic simulation.
# variables can be adjusted to your preference.
# blackjack

from random import shuffle


class Deck:
    newDeck = []
    cardCount = 52
    count = 0
    count2 = 0

    def __init__(self):
        self.reset()
        self.cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.cardsInPlay = []
        self.deckCards = []

    def reset(self):
        self.count = 0
        self.count2 = 0

    # populate the deck with the card names and suit names from the listed arrays.
    def populate(self):
        self.deckCards = ["" for x in range(0, 52)]
        for x in range(0, 4):
            for j in range(0, 13):
                stri = (self.cards[j])
                if self.suit[x] is "Clubs":
                    stri += " ♣"
                elif self.suit[x] is "Spades":
                    stri += " ♠"
                elif self.suit[x] is "Hearts":
                    stri = stri + " ♥"
                elif self.suit[x] is "Diamonds":
                    stri = stri + " ♦"
                self.deckCards[self.count] = stri
                self.count = self.count + 1
        if self.count == self.cardCount:
            print("Deck has been filled")

    # randomize the cards in the populated deck
    def shuffle(self):
        shuffle(self.deckCards)

    # return card from deck
    def getCard(self):
        if self.cardCount > 0:
            self.count2 = self.count2 + 1
            return self.deckCards[self.count2 - 1]
        else:
            return "No more cards!"

# house vs player.
# house draws a card from the deck, for itself and for the player
# house also checks for win state, each time a card is dealt


class Player:
    hand = []
    playerTotal = 0

    def __init__(self):
        pass

    def getCards(self):
        return self.hand


class House:
    hand = []
    houseTotal = 0

    def __init__(self, gameMode, drawAt, houseDrawAt):
        self.player = Player()
        self.deck = Deck()
        self.gameMode = gameMode
        self.playerWinCount = 0
        self.playerBustCount = 0
        self.houseWinCount = 0
        self.houseBustCount = 0
        self.draws = 0
        self.drawAt = drawAt
        self.houseDrawAt = houseDrawAt

    def play(self):
        # deck
        self.deck = Deck()
        self.deck.decKCards = []
        self.deck.populate()
        self.deck.shuffle()
        # hands
        self.player.hand = []
        self.hand = []
        # totals
        self.player.playerTotal = 0
        self.houseTotal = 0
        # bools
        # stands
        playerstand = False
        housestand = False
        # enable
        startGame = True

        while startGame is True:
            # player draws
            # manual mode
            if self.gameMode == 1:
                validcharacter = False
                if playerstand is False:
                    while validcharacter is False:
                        playerinput = input("\nWould you like a card? y/n: ")
                        if playerinput is 'y':
                            self.addCard("Player")
                            validcharacter = True
                        elif playerinput is 'n':
                            playerstand = True
                            validcharacter = True
                        else:
                            print("Invalid character.")
            # player auto mode
            elif self.gameMode == 2:
                # player
                if self.player.playerTotal < self.drawAt or self.houseTotal > self.player.playerTotal:
                    # if you want the player to win more, give the player this logic ->
                    if self.houseTotal <= 20:
                        self.addCard("Player")
                elif self.player.playerTotal >= self.drawAt:
                    playerstand = True
            # player stand
            if playerstand is True:
                print("\nPlayer has stood\n")
            # player score print
            print("Player: " + self.printCards(self.player.hand) + " Total: " + str(self.player.playerTotal))
            # check score
            if self.checkScore(housestand, playerstand) == 0:
                startGAme = False
                break
            # house draws
            if housestand is False:
                if self.houseTotal < self.houseDrawAt:
                    self.addCard("House")
                elif self.houseTotal >= self.houseDrawAt or self.houseTotal > self.player.playerTotal:
                    housestand = True
            # house stand
            if housestand is True:
                print("House has stood for this round")
            # print score
            print("House: " + self.printCards(self.hand) + " Total: " + str(self.houseTotal))
            # check score
            if self.checkScore(housestand, playerstand) == 0:
                startGame = False
                break
    #

    # this method provides calculations every time a card is picked, to determine if the game should proceed.
    def checkScore(self, houseState, playerState):
        score = 1
        if houseState is True and self.player.playerTotal > self.houseTotal and self.player.playerTotal <= 21:
            print("Player has won!")
            self.playerWinCount += 1
            score = 0
        #
        elif self.player.playerTotal == 21 or self.houseTotal > 21:
            print("Player has won!")
            self.playerWinCount += 1
            score = 0
        #
        if self.player.playerTotal > 21:
            print("Player has bust!")
            self.playerBustCount += 1
            score = 0
        #
        if self.houseTotal == 21 or self.player.playerTotal > 21:
            print("House has won!")
            self.houseWinCount += 1
            score = 0
        #
        elif playerState is True and self.houseTotal > self.player.playerTotal and self.houseTotal <= 21:
            print("House has won!")
            self.houseWinCount += 1
            score = 0
        #
        if self.houseTotal > 21:
            print("House has bust!")
            self.houseBustCount += 1
            score = 0
        #
        if houseState is True and playerState is True:
            if self.houseTotal == self.player.playerTotal:
                print("It is a tie!")
                self.draws += 1

            score = 0

        return score

    # get card
    def addCard(self, name):
        card = self.deck.getCard()
        number = card.split()[0]

        if number == "King" or number == "Queen" or number == "Jack":
            number = 10

        if name == "Player":
            if number == "Ace":
                # manual
                if self.gameMode == 1:
                    isValid = False
                    while isValid is False:
                        askforace = input("You scored an ace, would you like 1 or 11?: ")
                        if askforace == '1' or askforace == '11':
                            number = askforace
                            isValid = True
                        else:
                            print("Not a valid number. Please enter 1 or 11: ")
                # auto mode
                elif self.gameMode == 2:
                    if self.player.playerTotal > 10:
                        number = str(1)
                    else:
                        number = str(11)
            self.player.playerTotal += int(number)
            self.player.hand.append(card)

        if name == "House":
            # when house card is ace
            if number == "Ace":
                if self.houseTotal > 10:
                    number = str(1)
                else:
                    number = str(11)
            self.houseTotal += int(number)
            self.hand.append(card)

    # print card
    def printCards(self, hC):
        inputString = ""
        for x in hC:
            inputString = inputString + x + " "
        return inputString

    # print score
    def printScore(self):
        print("Player: " + self.printCards(self.player.hand) + " Total: " + str(self.player.playerTotal))
        print("House: " + self.printCards(self.hand) + " Total: " + str(self.houseTotal))


#
gameAutomatic = False
gameManual = False
game = True

# set draw
drawAt = 16
houseDrawAt = 13

iterationCount = 1000

while game is True:
    # input
    ifValid = False
    while ifValid is False:
        playerinput = input("Game Mode 1: Manual\nGame Mode 2: Automatic\n> ")

        if playerinput == str(1):
            gameAutomatic = False
            gameManual = True
            ifValid = True
        elif playerinput == str(2):
            gameManual = False
            gameAutomatic = True
            ifValid = True
        else:
            print("invalid input")

    house = House(int(playerinput), drawAt, houseDrawAt)

    # automatic game mode
    if gameAutomatic is True:
        print("Automatic is now running 100 times.")
        for x in range(0, iterationCount):
            print("Game: " + str(x + 1) + "\n")
            house.play()
        scores = "\nPlayer wins: " + str(house.playerWinCount) + "\nHouse wins: " + str(house.houseWinCount) + "\nDraws: " + str(house.draws) + "\n"
        scores += "House bust count: " + str(house.houseBustCount) + "\nPlayer bust count: " + str(house.playerBustCount)
        print(scores)

    # manual mode
    elif gameManual is True:
        house.play()

    validCharacter = False
    while validCharacter is False:
        playerinput = input("\nRun through again? Y/N:\n > ")
        if playerinput == 'y':
            validCharacter = True

        elif playerinput == 'n':
            validCharacter = True
            print("thanks for playing :)!")
            game = False
#