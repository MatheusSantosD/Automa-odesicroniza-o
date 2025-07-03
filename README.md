🎶📺 Automação PyAutoGUI: Spotify + YouTube
Descrição do projeto
Este repositório contém um script em Python utilizando PyAutoGUI para automatizar a abertura de uma música no Spotify e, em seguida, abrir um vídeo no YouTube em tela cheia, criando uma sincronização automática de áudio e vídeo.

O objetivo deste projeto é demonstrar na prática como usar automação de interface gráfica (GUI Automation) para abrir sites, interagir com botões na tela por imagem e controlar o navegador de forma automatizada, útil para aprendizado de automação ou para criar fluxos de produtividade e entretenimento automatizados.

📌 O que este script faz
✅ Abre o navegador Microsoft Edge utilizando comandos do sistema via PyAutoGUI.
✅ Acessa um link de música específica no Spotify.
✅ Procura automaticamente o botão de Play na tela usando reconhecimento de imagem (locateOnScreen) e clica quando localizado.
✅ Abre uma nova aba no navegador e acessa um vídeo específico no YouTube.
✅ Coloca o vídeo em tela cheia automaticamente.
✅ Exibe mensagens no console indicando o status da automação em cada etapa.

🚀 Tecnologias utilizadas
Python 3 – Linguagem principal para automação.

PyAutoGUI – Controle de mouse, teclado e reconhecimento de imagens na tela.

Time – Controle de delays entre as ações.

Webbrowser – (Comentado) possibilidade de abrir URLs via navegador padrão.

🧩 Estrutura do funcionamento
1️⃣ Abrir o navegador:

Pressiona a tecla win, digita edge e pressiona enter para abrir o navegador.

2️⃣ Acessar o Spotify:

Digita o link da música desejada no Spotify e pressiona enter.

Espera o carregamento da página.

3️⃣ Localizar e clicar no botão Play:

Usa pyautogui.locateOnScreen() com a imagem image.png do botão Play.

Faz a varredura até encontrar o botão e clica automaticamente no centro da imagem localizada.

4️⃣ Acessar o YouTube:

Usa ctrl + t para abrir nova aba.

Digita o link de um vídeo específico no YouTube e pressiona enter.

5️⃣ Ativar tela cheia:

Pressiona f para colocar o vídeo em tela cheia automaticamente.

6️⃣ Mensagens no console:

Durante o processo, exibe mensagens como:

Acessando o Spotify...

Procurando o botão play...

Botão play localizado

Acessando o YouTube...

Automação concluída!

⚠️ Pré-requisitos
✅ Python 3 instalado no sistema.
✅ Instalar o PyAutoGUI:

bash
Copiar
Editar
pip install pyautogui
✅ Instalar Pillow (para locateOnScreen funcionar corretamente):

bash
Copiar
Editar
pip install pillow
✅ Ter uma imagem image.png do botão Play do Spotify salva no mesmo diretório do script, bem recortada e clara, para facilitar a localização com pyautogui.locateOnScreen.

💡 Possíveis usos
✅ Treinar e entender automação de desktop com PyAutoGUI.
✅ Automatizar sua rotina para sincronizar áudio do Spotify com vídeos do YouTube.
✅ Aprender a utilizar locateOnScreen com confiança e eficiência.
✅ Criar outros fluxos automatizados similares, como automatização de login, abertura de sites para estudos, ou playlists personalizadas.

📄 Licença
Este projeto é de uso educacional e livre para modificações, contribuindo com seus estudos em automação com Python.
