#!/usr/bin/env python3
"""Injeta os dados da rodada no template e grava o HTML final.

Uso: python3 render.py DADOS.json SAIDA.html [--titulo "Texto"] [--sem-trechos]
--sem-trechos rejeita qualquer evidence.text preenchido (perfil com trechos_de_fonte: so_referencia).
Valida os dados, grava o HTML e confere que o JSON embutido volta a ser lido.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "matriz.html"
REQUIRED_ITEM = ("id", "project", "action", "due", "stage", "urgent", "important",
                 "previous", "change", "reason")
TEXT_ITEM = ("project", "action", "due", "stage", "previous", "change", "reason")
TOP_TEXT = ("title", "headline", "clock", "periodo", "footer", "question")
MAX_ITEMS = 12
MAX_EVIDENCE = 240
MAX_FIELD = 600
MAX_EVIDENCE_ITEMS = 5
ID_RE = re.compile(r"^[A-Z]{1,2}$")


def fail(msg):
    raise SystemExit(f"erro: {msg}")


def check_text(value, label, limit=MAX_FIELD):
    if not isinstance(value, str):
        fail(f"{label} precisa ser texto")
    if len(value) > limit:
        fail(f"{label} passa de {limit} caracteres; encurte")


def check_deadline(item_id, sd):
    if sd is None:
        return
    if isinstance(sd, bool) or not isinstance(sd, int):
        fail(f"ação {item_id}: sortDeadline precisa ser número AAAAMMDDHHmm ou null")
    try:
        datetime.strptime(f"{sd:012d}", "%Y%m%d%H%M")
    except ValueError:
        fail(f"ação {item_id}: sortDeadline {sd} não é uma data e hora válida (AAAAMMDDHHmm)")
    if len(str(sd)) != 12:
        fail(f"ação {item_id}: sortDeadline precisa ter 12 dígitos (AAAAMMDDHHmm)")


def validate(data, sem_trechos=False):
    if not isinstance(data, dict):
        fail("o JSON precisa ser um objeto")
    for key in TOP_TEXT:
        if key in data:
            check_text(data[key], f"'{key}'")
    if "rules" in data:
        rules = data["rules"]
        if not isinstance(rules, dict):
            fail("'rules' precisa ser um objeto com textos")
        for k, v in rules.items():
            check_text(v, f"rules.{k}")
    items = data.get("items")
    if not isinstance(items, list):
        fail("'items' precisa ser uma lista")
    if len(items) > MAX_ITEMS:
        fail(f"{len(items)} ações; o limite é {MAX_ITEMS}. Mantenha as de maior peso")
    seen = set()
    for item in items:
        if not isinstance(item, dict):
            fail("cada ação precisa ser um objeto")
        for key in REQUIRED_ITEM:
            if key not in item:
                fail(f"ação {item.get('id', '?')} sem o campo '{key}'")
        if not isinstance(item["id"], str) or not ID_RE.fullmatch(item["id"]):
            fail(f"id inválido {item['id']!r}: use uma ou duas letras maiúsculas (A, B, AA)")
        if item["id"] in seen:
            fail(f"id repetido: {item['id']}")
        seen.add(item["id"])
        if not isinstance(item["urgent"], bool) or not isinstance(item["important"], bool):
            fail(f"ação {item['id']}: urgent e important precisam ser true/false")
        for key in TEXT_ITEM:
            check_text(item[key], f"ação {item['id']}: '{key}'")
        for key in ("owner", "duvida"):
            if key in item:
                check_text(item[key], f"ação {item['id']}: '{key}'")
        check_deadline(item["id"], item.setdefault("sortDeadline", None))
        item.setdefault("owner", "")
        ev = item.setdefault("evidence", [])
        if not isinstance(ev, list):
            fail(f"ação {item['id']}: evidence precisa ser uma lista")
        if not ev:
            fail(f"ação {item['id']}: sem evidence. Toda ação precisa de ao menos uma fonte real")
        if len(ev) > MAX_EVIDENCE_ITEMS:
            fail(f"ação {item['id']}: {len(ev)} fontes; o limite é {MAX_EVIDENCE_ITEMS}. Mantenha as mais fortes")
        for e in ev:
            if not isinstance(e, dict) or not isinstance(e.get("source"), str) or not isinstance(e.get("text"), str):
                fail(f"ação {item['id']}: cada evidence precisa de 'source' e 'text' em texto")
            if not e["source"].strip():
                fail(f"ação {item['id']}: evidence.source vazio")
            check_text(e["source"], f"ação {item['id']}: evidence.source", 200)
            if sem_trechos and e["text"].strip():
                fail(f"ação {item['id']}: --sem-trechos exige evidence.text vazio")
            if len(e["text"]) > MAX_EVIDENCE:
                fail(f"ação {item['id']}: evidence.text passa de {MAX_EVIDENCE} caracteres; encurte o trecho")


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail(f"não consegui ler {argv[1]} como JSON: {exc}")
    validate(data, sem_trechos="--sem-trechos" in argv)
    data.pop("headline", None)  # o template calcula a contagem certa
    titulo = data.get("title", "Matriz de prioridades")
    if "--titulo" in argv:
        i = argv.index("--titulo")
        if i + 1 >= len(argv):
            fail("--titulo precisa de um texto")
        titulo = argv[i + 1]
    blob = json.dumps(data, ensure_ascii=False, indent=1)
    blob = blob.replace("</", "<\\/").replace("<!--", "<\\u0021--")
    safe_title = titulo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    values = {"TITULO": safe_title, "DADOS_JSON": blob}
    # uma única passada: um marcador dentro dos dados não é substituído de novo
    html = re.sub(r"\{\{(TITULO|DADOS_JSON)\}\}",
                  lambda m: values[m.group(1)], TEMPLATE.read_text(encoding="utf-8"))
    # confere que o JSON embutido é lido de volta e é igual ao original
    embedded = html.split('id="scenario-data">')[1].split("</script>")[0]
    if json.loads(embedded) != data:
        fail("o JSON embutido não confere com os dados; HTML não gravado")
    out = Path(argv[2])
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
    except (OSError, UnicodeEncodeError) as exc:
        fail(f"não consegui gravar {out}: {exc}")
    print(f"ok: {len(data['items'])} ações -> {argv[2]}")


if __name__ == "__main__":
    main(sys.argv)
