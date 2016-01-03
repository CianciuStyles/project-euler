from time import time

class PokerHand:
	def __init__(self, list_of_cards):
		self.points = ["High Card", "One Pair", "Two Pairs", "Three Of A Kind", "Straight", "Flush", "Full House", "Four Of A Kind", "Straight Flush", "Royal Flush", "Not Valid"]
		self.value = -1

		self.createCards(list_of_cards)
		self.sortCards()
		# print(str(self.cards))
		self.evaluateHand()
		# print(self.value)
		# print(self.points[self.value])

	def createCards(self, list_of_cards):
		self.cards = []
		for card in list_of_cards:
			value = card[0]
			suit = card[1]

			new_card = Card(value, suit)
			self.cards.append(new_card)

	def sortCards(self):
		self.cards.sort(key=lambda x: x.value, reverse=True)

	def evaluateHand(self):
		flush = self.checkFlush()
		maxFlush = self.checkMaxFlush()

		# Check for Royal Flush
		if flush is True and maxFlush is True:
			self.value = 9
			return

		straight = self.checkStraight()

		# Check for Straight Flush
		if straight is True and flush is True:
			self.value = 8
			self.args = [self.cards[0].value]
			return

		fourOfAKind, fourOfAKindIndex = self.checkFourOfAKind()

		# Check for Four of a Kind
		if fourOfAKind is True:
			self.value = 7
			self.args = [self.cards[fourOfAKindIndex].value]
			if fourOfAKindIndex is 0:
				self.args.append(self.cards[4].value)
			else:
				self.args.append(self.cards[0].value)
			return

		threeOfAKind, threeOfAKindIndex, threeOfAKindNumber = self.checkThreeOfAKind()
		onePair, onePairIndex, onePairNumber = self.checkOnePair(threeOfAKindNumber)

		# Check for Full House
		if threeOfAKind is True and onePair is True:
			self.value = 6
			self.args = [threeOfAKindNumber, onePairNumber]
			return

		# Check for Flush
		if flush is True:
			self.value = 5
			return

		# Check for Straight
		if straight is True:
			self.value = 4
			self.args = [self.cards[0].value]
			return

		# Check for Three Of A Kind
		if threeOfAKind is True:
			self.value = 3
			self.args = [threeOfAKindNumber]
			if threeOfAKindIndex == 0:
				self.args.append(self.cards[3].value)
				self.args.append(self.cards[4].value)
			elif threeOfAKindIndex == 1:
				self.args.append(self.cards[0].value)
				self.args.append(self.cards[4].value)
			else:
				self.args.append(self.cards[0].value)
				self.args.append(self.cards[1].value)
			return

		onePair, onePairIndex, onePairNumber = self.checkOnePair()
		anotherPair, anotherPairIndex, anotherPairNumber = self.checkOnePair(onePairNumber)

		#Check for Two Pairs
		if onePair is True and anotherPair is True:
			self.value = 2
			self.args = [onePairNumber, anotherPairNumber]

			cards = [card.value for card in self.cards]
			cards.remove(self.args[0])
			cards.remove(self.args[1])
			self.args.append(cards[0])
			return

		# Check for One Pair
		if onePair is True:
			self.value = 1
			self.args = [onePairNumber]

			cards = [card.value for card in self.cards]
			cards.remove(self.args[0])
			self.args.append(cards[0])
			self.args.append(cards[1])
			self.args.append(cards[2])
			return

		# Check for High Cards
		self.value = 0
		self.args = [card.value for card in self.cards]
		return


	def checkFlush(self):
		suitToCheck = self.cards[0].suit

		for index in range(1, len(self.cards)):
			if self.cards[index].suit != suitToCheck:
				return False

		return True

	def checkMaxFlush(self):
		return (self.cards[0].value is 14 and 
			    self.cards[1].value is 13 and
		        self.cards[2].value is 12 and
		        self.cards[3].value is 11 and
		        self.cards[4].value is 10)

	def checkStraight(self):
		for index in range(len(self.cards)-1):
			if (self.cards[index].value - self.cards[index+1].value) != 1:
				return False

		return True

	def checkFourOfAKind(self):
		for index in range(2):
			if (self.cards[index].value   == self.cards[index+1].value and
			    self.cards[index+1].value == self.cards[index+2].value and
			    self.cards[index+2].value == self.cards[index+3].value):

			   return True, index

		return False, -1

	def checkThreeOfAKind(self):
		for index in range(3):
			if (self.cards[index].value   == self.cards[index+1].value and
			    self.cards[index+1].value == self.cards[index+2].value):

			   return True, index, self.cards[index].value

		return False, -1, -1

	def checkOnePair(self, numberToExclude=0):
		for index in range(len(self.cards)-1):
			if self.cards[index].value == self.cards[index+1].value and self.cards[index].value != numberToExclude:
				return True, index, self.cards[index].value

		return False, -1, -1

	def compareTo(self, pokerHand):
		difference = self.value - pokerHand.value

		if difference != 0:
			return difference
		else:
			for index in range(len(self.args)):
				player_1_next_arg = self.args[index]
				player_2_next_arg = pokerHand.args[index]
				difference = player_1_next_arg - player_2_next_arg
				if difference != 0:
					return difference

class Card:
	def __init__(self, value, suit):
		self.suit = suit

		if value is "A":
			self.value = 14
		elif value is "K":
			self.value = 13
		elif value is "Q":
			self.value = 12
		elif value is "J":
			self.value = 11
		elif value is "T":
			self.value = 10
		else:
			self.value = int(value)

	def __repr__(self):
		return "Value: " + str(self.value) + ", Suit: " + self.suit


def read_hands_file():
	file = open("054.txt", "r")
	lines = [line.strip() for line in file]

	player_1_stack = []
	player_2_stack = []
	for line in lines:
		cards = line.split(" ")
		player_1_cards = cards[0:5]
		player_2_cards = cards[5:10]

		player_1_stack.append(player_1_cards)
		player_2_stack.append(player_2_cards)

	return player_1_stack, player_2_stack

def analyze_hands(player_1_stack, player_2_stack):
	player_1_points = 0
	player_2_points = 0

	for index in range(len(player_1_stack)):
		current_player_1_hand = player_1_stack[index]
		current_player_2_hand = player_2_stack[index]

		hand_winner = compare_hands(current_player_1_hand, current_player_2_hand)
		if hand_winner > 0:
			player_1_points += 1
		else:
			player_2_points += 1

	return player_1_points, player_2_points

def compare_hands(player_1_hand, player_2_hand):
	return PokerHand(player_1_hand).compareTo(PokerHand(player_2_hand))
	return 0

def main():
	start_time = time()

	player_1_stack, player_2_stack = read_hands_file()
	player_1_points, player_2_points = analyze_hands(player_1_stack, player_2_stack)
	print("Player 1 has won " + str(player_1_points) + " hands.")

	finish_time = time()
	elapsed_time = finish_time - start_time

	print("Solved in %.4f seconds." % elapsed_time)

if __name__ == '__main__':
	main()