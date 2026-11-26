---
name: setup
parent: fila-de-prioridades
description: Entrevista a pessoa, uma pergunta por vez, conecta as fontes, gera a prévia com dados reais e agenda a rodada. Primeira vez ou "configurar minha matriz".
---

# Modo setup

Meta: ao final, a pessoa tem uma matriz real na mão, um perfil salvo e a rodada agendada. Leva de 10 a 20 minutos, mais se for preciso conectar contas ou criar um repositório. Tom: direto, caloroso, sem jargão. Os termos técnicos deste arquivo e de `references/conectores.md` são para você; à pessoa vão frases simples.

A skill precisa estar instalada na pasta de skills do app, senão uma tarefa agendada não a encontra (conectores.md, item 5). Se a pessoa chegou aqui pelo nome da skill, ela está.

## Antes da primeira pergunta

1. Leia `references/criterios.md` e `references/conectores.md`.
2. Detecte o ambiente (Desktop/Cowork ou Claude Code) e quais ferramentas de conector existem, **sem ler nenhum e-mail, evento ou arquivo**: a leitura de teste só acontece depois de a pessoa ter dito a conta, a regra de sensibilidade e o escopo (passos 2, 3 e 4 abaixo). Não pergunte o que dá para descobrir.
3. Confira se há Python com `python3 --version`, depois `python --version` e `py --version`, e grave em `python_cmd` o comando que respondeu. Se aparecer uma janela pedindo para instalar ferramentas de desenvolvedor, diga à pessoa que é o Python que está sendo instalado. Sem nenhum, diga em três linhas como instalar ou ofereça só a lista em texto, sem o HTML. Na nuvem o comando é sempre `python3`.
4. Abra com duas frases: o que ela vai receber (uma matriz Urgente × Importante com os dados dela, todo dia ou toda semana) e que as perguntas vão uma por vez.

## Entrevista (uma pergunta por vez, na ordem)

Cada pergunta: opções curtas (máx. 3) + a sua recomendação + "ou me conte de outro jeito". Anote a resposta no perfil assim que vier (crie o perfil já no passo 8; até lá, guarde as respostas e grave todas de uma vez).

1. **Fontes.** "De onde saem as coisas que você precisa decidir?" Gmail, Google Calendar, Google Drive/Docs, texto ou arquivo que você cola. Várias podem valer.
2. **Contas.** Uma pergunta: de qual conta vem cada fonte escolhida (Gmail e Calendar podem ser de contas diferentes). Grave em "Contas" no perfil.
3. **Sensibilidade.** Uma pergunta: itens pessoais (eventos **e e-mails** de saúde, terapia, família, finanças pessoais) entram na matriz? Recomende deixá-los de fora. Grave em "Sensibilidade" no perfil, nunca só em "Regras extras": a rodada agendada não tem a quem perguntar e lê exatamente essa seção. Sem resposta clara, o padrão é deixar esses itens de fora.
4. **Escopo de cada fonte** (só para as escolhidas, uma pergunta por fonte). Gmail: caixa de entrada inteira, só marcadas, ou só de certas pessoas; o que ignorar (promoções, newsletters; grave em "Exclusões do Gmail"). Calendar: quais agendas. Drive: quais pastas ou documentos.
   - Só agora, para cada fonte, **conecte e teste** (conectores.md, itens 2 e 3), com uma leitura limitada ao escopo e à sensibilidade que a pessoa acabou de definir. Faça por ela o que der; oriente só o clique que é da pessoa. Não avance sem o teste passar ou sem ela decidir pular a fonte.
5. **Objetivos e projetos.** "Quais são os 3 a 5 projetos ou metas que mais importam para você agora?" Isso define "importante". Se ela travar, proponha uma leitura dos e-mails e eventos recentes (dentro do escopo e da sensibilidade já definidos) para sugerir candidatos, e peça que confirme.
6. **O que é urgente para você.** Mostre a regra padrão (prazo ou custo de atraso real dentro do horizonte) e pergunte se há pessoas, clientes ou tipos de pedido que sempre contam como urgentes, e o que nunca conta mesmo vindo marcado "urgente". Se a regra dela divergir do padrão, adote a dela e registre.
7. **Frequência, dia e hora.** Três perguntas separadas, quando houver mais de uma: diária ou semanal (recomende diária para quem decide coisas todo dia, semanal para quem planeja por semana); o dia, se for semanal; a hora. O fuso vem da agenda da pessoa; confirme em uma frase. Lembre que a rodada roda um pouco antes de ela precisar ler.
   - **Onde rodar.** Primeiro dê o aviso do item 5C de `references/conectores.md` (não há trava técnica de somente leitura). Depois, **só se a nuvem for possível** (Claude Code, `gh` logado e `RemoteTrigger` disponível, ver 5B), pergunte: "A rodada roda no seu computador ou na nuvem?" Duas opções e a sua recomendação. *No computador*: mais simples, usa a pasta local; deve rodar no horário enquanto o Claude estiver aberto e, se estava fechado, na próxima abertura (não testado). *Na nuvem*: deve rodar com o computador desligado e o Claude fechado (só execuções manuais foram provadas); exige repositório privado no GitHub, conectores da conta e consentimento para os trechos de e-mail irem ao GitHub (5B.1). Recomende a nuvem só para quem quer autonomia total e já usa GitHub; o computador, para quem quer começar sem criar nada. Se a nuvem não for possível, **não pergunte nem a cite**. Registre a escolha em `execucao` no perfil.
8. **Onde guardar.** No computador: proponha `Fila de Prioridades` em Documentos (ou a pasta de trabalho da sessão no Cowork). Avise que os arquivos guardam trechos de e-mail em texto aberto e ofereça uma pasta fora de iCloud/Drive sincronizado. Crie a pasta, as subpastas `matrizes/` e `dados/` e o `perfil.md` (a partir de `templates/perfil.md`, com tudo que a pessoa já respondeu) você mesmo(a), sem pedir à pessoa. Na nuvem: o repositório privado (conectores.md, 5B.1) no lugar da pasta, com o perfil na raiz. Daqui em diante, atualize o perfil a cada resposta nova.

## Prévia com dados reais

1. Rode o fluxo de `modes/rodada.md` agora, com a pessoa presente, usando o horizonte da frequência escolhida.
2. Mostre o caminho do HTML e conte, em poucas linhas, as 3 ações com que começaria e por quê.
3. Para cada classificação duvidosa, **pergunte** (uma por vez) e grave a resposta como regra no perfil.
4. Pergunte: "Isso se parece com o que você queria?" Se não, ajuste o perfil (modes/ajuste.md) e gere de novo. No máximo duas voltas; depois disso, diga o que ainda está imperfeito, grave isso no perfil como ajuste pendente e siga para o agendamento.

## Agendamento

No computador: siga `references/conectores.md`, item 5. Na nuvem: item 5B inteiro (repositório, perfil final no repositório **antes** de criar a rotina, conectores limitados, primeira execução conferida pelo log e pelo commit). Crie a tarefa, rode-a uma vez para confirmar (ou explique por que não deu) e grave `tarefa_agendada` no perfil. Na nuvem, esse campo só existe depois da criação da rotina: faça um segundo commit e push do perfil.

## Fechamento

Confira que o `perfil.md` está completo e atualizado (na nuvem, com commit e push do perfil final). Diga em um bloco curto: o que ficou ligado (fontes, horário, pasta), o caminho da matriz de hoje, como pedir uma rodada na hora ("rodar a fila de prioridades"), como ajustar ("ajustar minha fila"), e o que ficou com a pessoa, se algo ficou. Diga também em qual estado a agenda está: criada, execução manual conferida, ou recorrência conferida (só depois de um disparo real no horário). Não diga "instalado" se algum passo falhou.
