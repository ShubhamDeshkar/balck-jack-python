import random
import tkinter


def load_images(card_images):
    suits = ['club', 'diamond', 'heart', 'spade']
    face_card = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = 'cards\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        for card in face_card:
            name = 'cards\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        if score > 21 and ace:
            ace = False
            score -= 10
    return score


def deal_dealer():
    deal_card(dealerCardFrame)


def deal_player():
    playerHand.append(deal_card(playerCardFrame))
    player_score = score_hand(playerHand)

    playerScoreLabel.set(player_score)
    if player_score > 21:
        result_text.set('Dealer Wins!')

    # global playerScore
    # global playerAce
    # card_value = deal_card(playerCardFrame)[0]
    # if card_value == 1 and not playerAce:
    #     playerAce = True
    #     card_value = 11
    # playerScore += card_value
    #
    # if playerScore > 21 and playerAce:
    #     card_value -= 10
    #     playerAce = False
    # playerScoreLabel.set(playerScore)
    # if playerScore > 21:
    #     result_text.set('Dealer Wins!')
    # print(locals())


mainWindow = tkinter.Tk()
mainWindow.title('Black Jack')
mainWindow.geometry('640x480+400+200')
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
# result_text.set('Welcome to Black Jack setup')

cardFrame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=2, background='green')
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()

tkinter.Label(cardFrame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background='green', fg='white').grid(row=1, column=0)

dealerCardFrame = tkinter.Frame(cardFrame, background='green')
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

playerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background='green', fg='white').grid(row=3, column=0)

playerCardFrame = tkinter.Frame(cardFrame, background='green')
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

buttonFrame = tkinter.Button(mainWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')

dealerButton = tkinter.Button(buttonFrame, text='Dealer', command=deal_dealer)
dealerButton.grid(row=0, column=0)

playerButton = tkinter.Button(buttonFrame, text='Player', command=deal_player)
playerButton.grid(row=1, column=0)

cards = []
load_images(cards)
print(cards)

deck = list(cards)
random.shuffle(deck)

dealerHand = []
playerHand = []

mainWindow.mainloop()
