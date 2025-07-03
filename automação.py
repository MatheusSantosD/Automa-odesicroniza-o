import pyautogui 
import time 
import webbrowser

pyautogui.PAUSE = 1

#webbrowser.open('https://open.spotify.com/intl-pt/track/2UREu1Y8CO4jXkbvqAtP7g')

pyautogui.press('win')
time.sleep(0.5)

pyautogui.write('edge')
time.sleep(0.5)

pyautogui.press('enter')
time.sleep(2)

pyautogui.write('https://open.spotify.com/intl-pt/track/2UREu1Y8CO4jXkbvqAtP7g')
print('Acessando o Spotify...')
time.sleep(1)

pyautogui.press('enter')

time.sleep(5)

# Aqui ele vai localizar o botão play na tela.
button_location = None
while button_location is None:
    button_location = pyautogui.locateOnScreen('image.png', confidence=0.8)
    print('procurando o botão play...')
    time.sleep(3)

# Aqui ele vai localizar o centro do button_location e vai clicar nele.
button_point = pyautogui.center(button_location)
print('Botão play localizado')
pyautogui.click(button_point)
time.sleep(1)

# Abrir o navegador e acessar o youtube
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://youtu.be/6CF29TtxU2c?si=uR-mfQQ_JbuPZEr8')
pyautogui.press('enter')
print('Acessando o Youtube...')
time.sleep(2)

# Abrir em tela cheia
pyautogui.press('f')
print('Automação concluída!')