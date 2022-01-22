import random


class card:
    '''This is the face value of the card from 1-13
    
    The reposibility of the card Ace (1) will be lowest and King (13) will be highest
    
    Playing cards usually have suits but this will not apply in Hilo due to it has no value or interaction in the game.'''

    def __init__(self) -> None:
        '''This constructs pulling a card.
    
        Args:
        self (Draw_Card): an instance of card
        '''
        ## I started this but I feel this data is going to go into the dirctor.class. 
        #self.first_card_value = 0
        #self.second_card_value = 0
        #self.points = 0

        self.card_value = 0
        
    
    def draw_card(self):
        '''Generates a new random'''
        #self.first_card_value = random.randint(1, 13)
        #self.second_card_value = random.randint(1, 13)
        self.card_value - random.randint(1, 13)