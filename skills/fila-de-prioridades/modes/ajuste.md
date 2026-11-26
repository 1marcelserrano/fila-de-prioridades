---
name: ajuste
parent: fila-de-prioridades
description: Revisa critérios, fontes, horário ou frequência do perfil a partir do feedback da pessoa e das dúvidas acumuladas.
---

# Modo ajuste

## Procedimento

1. Leia `perfil.md` e a última matriz (o `dados/` de data mais recente; semanais são `AAAA-Sxx`, e a data mais recente vale). Cheque o campo `duvida` das últimas rodadas: são perguntas pendentes.
2. Descubra o que incomodou, uma pergunta por vez. Casos comuns:
   - **Classificação errada** ("isso não era urgente"): pergunte o porquê em uma frase, transforme em regra curta e específica ("pedidos da loja X nunca são urgentes") e grave em "Regras extras".
   - **Falta de coisa** (fonte, pasta, pessoa): ajuste o escopo e teste a fonte (conectores.md).
   - **Ruído demais**: acrescente exclusões ao perfil.
   - **Horário ou frequência**: atualize o perfil **e a tarefa agendada** (crie a nova e remova ou desative a antiga se o ambiente permitir; senão, oriente a pessoa). Na nuvem (`execucao: nuvem`), use `RemoteTrigger update` com o cron em UTC e, se o fuso da pessoa muda de horário em alguma época do ano, confira o horário quando isso acontecer.
   - **Objetivos mudaram**: reescreva "Objetivos e projetos" e avise que o quadrante "importante" vai mudar.
3. Resolva as dúvidas acumuladas, uma por vez, e grave as respostas como regras.
4. Regere a matriz de hoje com o perfil novo e mostre o que mudou de quadrante e por quê.
5. Registre uma linha em "Histórico de ajustes" com a data e a mudança.
6. **Na nuvem, publique o ajuste.** Depois de **qualquer** mudança no `perfil.md` (fontes, contas, sensibilidade, exclusões, objetivos, urgente, cadência, regras), confira que o repositório continua `PRIVATE` e faça commit e push do perfil: a rotina lê do repositório, e sem isso ela segue com o perfil antigo. Compare também `versao_skill_no_repositorio` com a versão do `SKILL.md` que você tem, número por número; se a do repositório for menor, copie a skill de novo e atualize o campo (conectores.md, 5B.5).

## Cuidados

- Regra nova precisa ser específica o bastante para não contaminar outros casos. Se for ampla demais, proponha uma versão mais estreita e confirme.
- Não reescreva o perfil inteiro por causa de um ajuste pequeno.
- Se o pedido contradiz a regra de que urgente exige prazo real, atenda só com exceção estreita (uma pessoa, um remetente ou um tipo de pedido), nunca uma regra geral, e avise em uma frase o que se perde: sem prazo real, o urgente volta a ser o que parece urgente, não o que é.
