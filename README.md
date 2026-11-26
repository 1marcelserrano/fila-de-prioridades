# Fila de Prioridades

**Toda manhã, uma matriz Urgente × Importante feita com os seus e-mails e a sua agenda de verdade.**

[Instalar](#instalar) • [Como funciona](#como-funciona) • [Quando usar](#quando-usar) • [O que foi testado](#o-que-foi-testado) • [Comunidade](#comunidade-gratuita)

---

Uma skill para o Claude que lê o seu Gmail e o seu Google Calendar, separa o que você precisa decidir em quatro quadrantes (fazer agora, agendar, delegar, eliminar) e gera um arquivo HTML com Lista, Matriz e minimapa, em tema claro e escuro. Na primeira vez ela faz uma entrevista curta, uma pergunta por vez, roda uma prévia com os seus dados reais e agenda a rodada diária ou semanal.

## Como funciona

| Antes | Depois |
|-------|--------|
| Você abre a caixa de entrada e decide pelo que parece urgente: o assunto em maiúsculas, o último e-mail que chegou. | Você abre um arquivo com as ações separadas em quatro quadrantes, cada uma com prazo, motivo e o trecho do e-mail ou do evento que a sustenta. |

A skill não confia na palavra "urgente". Urgente é o que tem prazo ou custo de atraso real dentro da rodada. Importante é o que serve aos projetos que você declarou na entrevista. Quando ela fica em dúvida, marca a ação com "Confirmar" em vez de chutar.

## Instalar

Precisa de Python 3 no computador (o script que monta a página). Copie a pasta da skill para a pasta de skills do seu Claude:

```bash
git clone https://github.com/1marcelserrano/fila-de-prioridades.git
cp -r fila-de-prioridades/skills/fila-de-prioridades ~/.claude/skills/
```

Abra uma conversa nova no Claude Code ou no Claude Desktop, com o Gmail e o Google Calendar conectados, e peça:

> configurar minha fila

## Quando usar

Frases que ativam a skill:

- "fila de prioridades" ou "minha fila de prioridades"
- "matriz da manhã"
- "matriz urgente e importante"
- "resumo da manhã dos meus e-mails"
- "o que resolver primeiro"
- "configurar minha fila" e "ajustar minha fila"

Em linguagem natural também funciona, por exemplo: "me mostra o que eu preciso resolver primeiro hoje".

## Por que

- **Prazo real, não pressa aparente.** Cada ação traz a fonte que sustenta o prazo. Sem prazo na fonte, a skill escreve "sem prazo".
- **A fila aprende com você.** Se uma classificação estiver errada, o modo de ajuste transforma a sua correção numa regra curta e guarda no seu perfil.
- **Os arquivos são seus.** O perfil, os dados e as matrizes ficam numa pasta que você escolhe. Os trechos de e-mail ficam em texto aberto nessa pasta, então prefira uma que não seja sincronizada.

## O que ela faz e o que não faz

| Faz | Não faz |
|-----|---------|
| Lê Gmail e Calendar e monta a matriz com prazo, motivo e fonte | Não envia, apaga, arquiva nem marca e-mails, por regra da skill |
| Agenda a rodada diária ou semanal | Não promete rodar sozinha com o computador desligado, a não ser no modo nuvem, opcional e ainda em validação |
| Avisa quando uma fonte falha em vez de gerar uma matriz vazia | Não troca o seu julgamento: classifica pelo mais provável e deixa a dúvida visível |

## O que foi testado

Sem rodeio, para você saber no que está pisando:

- Rodada real no Claude Desktop, com Gmail e Calendar de uma conta de verdade, em execução manual: funcionou.
- Rotina de teste na nuvem, de uso único: leu Gmail e Calendar, gerou a página e fez o commit.
- **Ainda não provado:** o disparo recorrente por horário, o uso no Cowork e o setup completo por quem não é o autor.
- **Atenção:** "somente leitura" é uma regra da skill e do prompt, não um bloqueio técnico. A tarefa agendada enxerga as ferramentas de enviar e apagar e-mail. Leia o item sobre isso no arquivo `skills/fila-de-prioridades/references/conectores.md` antes de agendar.

## Comunidade gratuita

Esta skill é um presente para quem quer parar de decidir o dia pelo susto. Se você quer construir skills como essa, e conversar com quem está fazendo o mesmo, entre na comunidade gratuita:

**[Entrar na comunidade no Skool](https://www.skool.com/marcel-1662/about)**

## Origem

Baseada no jig "Morning inbox", do Brief 01 do d.AI, de Marcel Serrano (matriz Urgente × Importante, vistas Lista e Matriz, minimapa). O visual segue o design system Primer, do GitHub.

## Contribuir

Pull requests são bem-vindos. Veja o [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licença

MIT. Veja o [LICENSE](./LICENSE).

---

<sub>Forged at [MSCREATIVE.SYSTEMS™](https://mscreative.systems), Barcelona</sub>
