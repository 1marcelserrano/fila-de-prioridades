# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [Não lançado]

### Adicionado
- Página de apresentação em `page/index.html`, com a saída de exemplo ao lado.
- Imagem de compartilhamento do repositório em `assets/social-preview.png`, com a fonte em HTML.
- Pacote `fila-de-prioridades.skill`, para instalar sem terminal.

## [0.2.3] - 2026-11-27

### Alterado
- Removidas as menções ao Cowork, que não existe mais.
- A frase sobre o estudo "The Mere Urgency Effect" (Zhu, Yang e Hsee, 2018) agora diz que a regra sobre a palavra "urgente" é uma aplicação da skill, por precaução. O estudo trata de prazos curtos, não de assuntos de e-mail.

## [0.2.2] - 2026-11-26

### Adicionado
- Primeira versão pública: modos setup, rodada e ajuste, matriz Urgente × Importante em HTML com Lista, Matriz e minimapa, tema claro e escuro.
- Modo nuvem opcional, que roda a rodada numa rotina na nuvem a partir de um repositório privado.
- Validações no `render.py`, 14 testes e uma saída de exemplo com dados fictícios.

### Segurança
- A skill avisa que "somente leitura" é uma regra do prompt, não um bloqueio técnico, nos dois modos.
- Pedidos de pagamento de remetente desconhecido viram "possível golpe". Links de e-mails não são abertos nem reproduzidos.
