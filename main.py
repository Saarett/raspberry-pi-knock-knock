from gpiozero import LED, Button
from signal import pause
import pygame

def playDoorbellRing():
    pygame.mixer.init()
    pygame.mixer.music.load("doorbell-ring.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    return

def createAndEnterChatRoom():
    resp = requests.post('http://vmedu116.mtacloud.co.il:8080/chatRoom')
    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(resp.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    requests.post('http://vmedu116.mtacloud.co.il:8080/enter')
    webbrowser.open_new(x.chatRoom)
    return

def getNumOfParticipantsInActiveRoom():
    resp = requests.post('http://vmedu116.mtacloud.co.il:8080/chatRoom')
    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(resp.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    numOfParticipants = int(x.namOfParticipants)
    return numOfParticipants

def didConversationStart():
    start = time.time()
    end = time.time()
    maxTimeForWait = 10
    while end-start < maxTimeForWait:
        numOfParticipants = getNumOfParticipantsInActiveRoom()
        if numOfParticipants == 2:
            return true
        end = time.time()
    return false

def handleConversation():
    numOfParticipants = etNumOfParticipantsInActiveRoom()
    while numOfParticipants == 2:
        # conversation is still running
    # conversation had eneded
    return

def leaveChatRoom():
    requests.put('http://vmedu116.mtacloud.co.il:8080/leave')
    os.system("pkill chromium")
    return
    

def startChatRoom():
    print("Asking for a chat room")
    playDoorbellRing()
    createAndEnterChatRoom()
    conversationStartFlag = didConversationStart()
    if conversationStartFlag == true:
        handleConversation()
    leaveChatRoom()
    return

while True:
    button = Button(21)
    button.when_pressed = startChatRoom
