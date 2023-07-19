# README - Executando o projeto no Windows

Este é um guia passo a passo para executar o projeto no Windows. O projeto utiliza a biblioteca Spotipy, YoutubeSearch, MoviePy, Pytube e Tkinter para baixar músicas de uma playlist do Spotify a partir dos links do YouTube.

## Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python 3.x: É necessário ter o Python instalado em sua máquina. Você pode fazer o download da versão mais recente do Python no site oficial (https://www.python.org/downloads/).
- pip: O pip é o sistema de gerenciamento de pacotes do Python. Verifique se o pip está instalado executando o comando `pip --version` no prompt de comando. Se não estiver instalado, você pode seguir as instruções de instalação em (https://pip.pypa.io/en/stable/installing/).
- ffmpeg: O ffmpeg é uma ferramenta necessária para a manipulação de arquivos de áudio e vídeo. Você precisa instalá-lo para usar a biblioteca MoviePy. Siga as etapas abaixo para instalá-lo.

## Instalando o ffmpeg

1. Faça o download do ffmpeg: Acesse o site oficial do ffmpeg (https://ffmpeg.org/) e navegue até a página de download. Faça o download da versão adequada para o seu sistema operacional (Windows).

2. Extraia os arquivos: Após o download ser concluído, extraia o conteúdo do arquivo zip para um diretório de sua escolha. Por exemplo, você pode extrair os arquivos para `C:\ffmpeg`.

3. Adicione o ffmpeg ao PATH do sistema: Para que o ffmpeg possa ser executado a partir de qualquer localização no prompt de comando, você precisa adicionar o diretório do ffmpeg ao PATH do sistema. Siga as etapas abaixo:

   - Abra o Painel de Controle do Windows.
   - Clique em "Sistema e Segurança" e, em seguida, em "Sistema".
   - Clique em "Configurações avançadas do sistema".
   - Na guia "Avançado", clique no botão "Variáveis de Ambiente".
   - Na seção "Variáveis do Sistema", localize a variável "Path" e clique no botão "Editar".
   - Clique no botão "Novo" e adicione o caminho completo para o diretório do ffmpeg (por exemplo, `C:\ffmpeg\bin`).
   - Clique em "OK" para salvar as alterações.

4. Verifique a instalação: Para verificar se o ffmpeg foi instalado corretamente, abra uma nova janela do prompt de comando e execute o seguinte comando:

   ```bash
   ffmpeg -version
   ```

   Se a instalação estiver correta, você verá informações sobre a versão do ffmpeg.

## Instalando o ytmdl

O ytmdl é uma ferramenta de linha de comando que permite baixar músicas do YouTube. Para instalar o ytmdl, siga as etapas abaixo:

1. Abra uma nova janela do prompt de comando.

2. Execute o seguinte comando para instalar o ytmdl usando o pip:

   ```bash
   pip install ytmdl
   ```

   O pip irá baixar e instalar o ytmdl juntamente com suas dependências.

3. Verifique a instalação: Após a instalação ser concluída, execute o seguinte comando para verificar se o ytmdl foi instalado corretamente:

   ```bash
   ytmdl --version
   ```

   Se a instalação estiver correta, você verá informações sobre a versão do ytmdl.

## Configuração do ambiente

Siga estas etapas para configurar o ambiente e executar o projeto:

1. Faça o download do código-fonte do projeto e salve-o em um diretório de sua escolha.

2. Abra o prompt de comando e navegue até o diretório onde você salvou o código-fonte do projeto.

3. Crie um ambiente virtual (opcional): Embora não seja obrigatório, é recomendável criar um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando para criar um ambiente virtual chamado "env":

   ```bash
   python -m venv env
   ```

4. Ative o ambiente virtual (opcional): Se você optou por criar um ambiente virtual, ative-o executando o seguinte comando:

   - No Windows:

     ```bash
     .\env\Scripts\activate
     ```

5. Instale as dependências: Use o gerenciador de pacotes `pip` para instalar as dependências necessárias. Execute o seguinte comando para instalar as dependências:

   ```bash
   pip install spotipy youtube-search moviepy pytube
   ```

6. Configure as credenciais do Spotify: Antes de executar o projeto, você precisa configurar as credenciais do cliente do Spotify. Acesse o [Dashboard de Desenvolvedor do Spotify](https://developer.spotify.com/dashboard/) e faça login ou crie uma conta. Crie um novo aplicativo e obtenha o ID do cliente e o segredo do cliente. Substitua as variáveis `client_id` e `client_secret` no código-fonte pelo seu ID de cliente e segredo de cliente, respectivamente.

7. Configure o link da playlist do Spotify: No código-fonte, substitua o valor da variável `playlist_url` pelo link da playlist do Spotify que você deseja baixar.

8. Execute o projeto: Após concluir as etapas acima, você está pronto para executar o projeto. Use o seguinte comando para iniciar a execução:

   ```bash
   python seu_arquivo.py
   ```

   Certifique-se de substituir `seu_arquivo.py` pelo nome do arquivo que contém o código-fonte do projeto.

9. Selecione o diretório de download: Quando o projeto for iniciado, uma janela de diálogo será exibida para selecionar o diretório onde as músicas serão baixadas. Navegue até o diretório desejado e clique em "OK".

10. Aguarde o processo de download: O projeto começará a pesquisar os links do YouTube para cada faixa da playlist do Spotify e baixará as músicas correspondentes no diretório selecionado. Aguarde até que todas as músicas sejam baixadas.

11. Verifique as músicas baixadas: Após o término do processo de download, verifique o diretório selecionado para encontrar as músicas baixadas. As músicas serão nomeadas no formato `<nome_da_faixa>.mp3`.

Observação: O código está setada para buscar as músicas Extended version ( versão extendida ), se desejar a normal na linha 49 retire " - Extended mix audio" da string.
