import card
import random
import pygame
from pygame.locals import *


# 버린 카드 클래스
class DiscardPile:
    def __init__(self):
        self.cards = [] 
        self.font = pygame.font.Font(None, 20)

    def createPile(self,deck): #게임을 시작하기 위해 첫번째 카드 생성
        self.cards = []
        self.cards.append(deck.drawCard())

    def addCard(self, card): 
        self.cards.insert(0, card)

    def show(self, x, y, screen):
        for i in range(len(self.cards)-1, -1, -1):
            self.cards[i].show(x, y - i)

        nowColor = self.font.render(self.cards[0].color, True, (255, 255, 255))
        screen.blit(nowColor, (x + 60, y))
        


# 플레이어 클래스
class Player:
    def __init__(self, name):
        # 플레이어 패 생성
        self.name = name
        self.handsOnCard = []

    #마지막 카드에 기반해 플레이어 패에서 낼 수 있는 카드 리스트 생성
    def playableCard(self, discardPileCard):
        playableCard=[]
        if discardPileCard[-1].color=="None": #마지막 카드가 색이 없는 기술카드일 경우 현재색과 같은 카드 추가
            for card in self.handsOnCard:
                 if card.color == "red": #현재색이 빨강색이라 가정
                    playableCard.append(card)   
        else:
            for card in self.handsOnCard:
                if card.color == discardPileCard[-1].color or card.value == discardPileCard[-1].value or card.color=="None":
                    playableCard.append(card)   
        return playableCard
    
    
                

# 사용자 플레이어 클래스
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.time=3000

    def showHandsOnCard(self, x, y):
        for i in range(len(self.handsOnCard)):
            self.handsOnCard[i].faceUp = True
            self.handsOnCard[i].show(x + (i * 30), y)
    
    def addCard(self, card):
        card.faceUp = True
        self.handsOnCard.append(card)

        
       
# 컴퓨터 플레이어 클래스 
class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.time=2000
        self.font = pygame.font.Font(None, 20)

    def showHandsOnCard(self, x, y, screen):
        self.handsOnCard[0].faceUp = False
        self.handsOnCard[0].width = 30
        self.handsOnCard[0].height = 50
        name = self.font.render(self.name, True, (128, 128, 128))
        num = self.font.render('X' + str(len(self.handsOnCard)), True, (128, 128, 128))
        screen.blit(name, (x, y))
        screen.blit(num, (x + 50, y + 40))
        self.handsOnCard[0].show(x, y + 25)
        



if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("카드 게임")

    bg_color = pygame.Color("green")
    screen.fill(bg_color)


    # 카드덱 생성
    deck = card.Deck()

    human_plyr = HumanPlayer(deck) #사용자 객체 
    pc_plyr = ComputerPlayer(deck) # 컴퓨터 객체

    discardPile = DiscardPile(deck) # 버린 카드 객체
    discardPileCard = discardPile.cards # 버린 카드 리스트


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            


    # Pygame 종료
    pygame.quit()





