from deck import deck
from card import card 

class players():
    def __init__(self):
        self.score = 0
        self.hand = deck()
        
    def draw_card(self,drawPile):
        card = drawPile.draw()
        self.hand.add_card(card)

    def AskCard (self, opponentDeck, drawPile, card):
        for opponent_card in opponentDeck.cards:
            if(opponent_card.rank == card.rank):
                self.hand.add_card(opponent_card)
                opponentDeck.deck.remove(opponent_card)
            else:
                self.draw_card(drawPile)

    def increase_score (self, cards, discardDeck):
        pass