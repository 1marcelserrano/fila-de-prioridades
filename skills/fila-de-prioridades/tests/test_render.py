import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RENDER = ROOT / "scripts" / "render.py"
SAMPLE = ROOT / "tests" / "sample.json"


def run(data_path, out_path):
    return subprocess.run([sys.executable, str(RENDER), str(data_path), str(out_path)],
                          capture_output=True, text=True)


class RenderTest(unittest.TestCase):
    def test_renders_and_escapes_script_close(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "out.html"
            r = run(SAMPLE, out)
            self.assertEqual(r.returncode, 0, r.stderr)
            html = out.read_text(encoding="utf-8")
            self.assertNotIn("{{DADOS_JSON}}", html)
            self.assertNotIn("{{TITULO}}", html)
            self.assertEqual(html.count("</script>"), 2)  # só os dois reais
            block = html.split('id="scenario-data">')[1].split("</script>")[0]
            data = json.loads(block)
            self.assertEqual(len(data["items"]), 4)

    def test_rejects_non_boolean_flags(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        data["items"][0]["urgent"] = "sim"
        with tempfile.TemporaryDirectory() as d:
            bad = Path(d) / "bad.json"
            bad.write_text(json.dumps(data), encoding="utf-8")
            r = run(bad, Path(d) / "o.html")
            self.assertNotEqual(r.returncode, 0)

    def test_rejects_duplicate_ids_and_missing_fields(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        data["items"][1]["id"] = "A"
        with tempfile.TemporaryDirectory() as d:
            bad = Path(d) / "bad.json"
            bad.write_text(json.dumps(data), encoding="utf-8")
            self.assertNotEqual(run(bad, Path(d) / "o.html").returncode, 0)
            del data["items"][1]["reason"]
            data["items"][1]["id"] = "B"
            bad.write_text(json.dumps(data), encoding="utf-8")
            self.assertNotEqual(run(bad, Path(d) / "o.html").returncode, 0)

    def test_html_comment_opener_roundtrips(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        data["items"][0]["evidence"][0]["text"] = "<!-- oculto --> texto"
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "d.json"
            src.write_text(json.dumps(data), encoding="utf-8")
            out = Path(d) / "o.html"
            self.assertEqual(run(src, out).returncode, 0)
            block = out.read_text(encoding="utf-8").split('id="scenario-data">')[1].split("</script>")[0]
            self.assertEqual(json.loads(block)["items"][0]["evidence"][0]["text"], "<!-- oculto --> texto")

    def test_rejects_bad_ids_types_and_limits(self):
        base = json.loads(SAMPLE.read_text(encoding="utf-8"))
        cases = []
        d = json.loads(json.dumps(base)); d["items"][0]["id"] = "<img onerror=x>"; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["id"] = 1; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["sortDeadline"] = "amanhã"; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["evidence"] = ["texto"]; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["evidence"] = [{"source": "s", "text": "x" * 300}]; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"] = [dict(base["items"][0], id=chr(65 + i)) for i in range(13)]; cases.append(d)
        with tempfile.TemporaryDirectory() as t:
            for i, c in enumerate(cases):
                src = Path(t) / f"c{i}.json"
                src.write_text(json.dumps(c), encoding="utf-8")
                self.assertNotEqual(run(src, Path(t) / "o.html").returncode, 0, f"caso {i}")

    def test_rejects_missing_evidence_bad_deadline_and_bad_types(self):
        base = json.loads(SAMPLE.read_text(encoding="utf-8"))
        cases = []
        d = json.loads(json.dumps(base)); d["items"][0]["evidence"] = []; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["sortDeadline"] = 1; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["sortDeadline"] = 202613991200; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["sortDeadline"] = 99999999999999; cases.append(d)
        d = json.loads(json.dumps(base)); d["title"] = 5; cases.append(d)
        d = json.loads(json.dumps(base)); d["rules"] = {"urgent": {"a": 1}}; cases.append(d)
        d = json.loads(json.dumps(base)); d["footer"] = "x" * 700; cases.append(d)
        d = json.loads(json.dumps(base)); d["items"][0]["evidence"] = [{"source": " ", "text": "x"}]; cases.append(d)
        with tempfile.TemporaryDirectory() as t:
            for i, c in enumerate(cases):
                src = Path(t) / f"c{i}.json"
                src.write_text(json.dumps(c), encoding="utf-8")
                r = run(src, Path(t) / "o.html")
                self.assertNotEqual(r.returncode, 0, f"caso {i}")
                self.assertNotIn("Traceback", r.stderr, f"caso {i}: erro cru em vez de mensagem")

    def test_marker_inside_data_is_not_replaced_again(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        data["title"] = "{{DADOS_JSON}}"
        data["items"][0]["evidence"][0]["text"] = "{{TITULO}} fica literal"
        with tempfile.TemporaryDirectory() as t:
            src = Path(t) / "d.json"; src.write_text(json.dumps(data), encoding="utf-8")
            out = Path(t) / "o.html"
            self.assertEqual(run(src, out).returncode, 0)
            html = out.read_text(encoding="utf-8")
            self.assertIn("<title>{{DADOS_JSON}}</title>", html)
            block = html.split('id="scenario-data">')[1].split("</script>")[0]
            self.assertEqual(json.loads(block)["items"][0]["evidence"][0]["text"], "{{TITULO}} fica literal")

    def test_creates_missing_output_folder(self):
        with tempfile.TemporaryDirectory() as t:
            out = Path(t) / "matrizes" / "novo" / "o.html"
            r = run(SAMPLE, out)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue(out.exists())

    def test_page_script_has_valid_javascript(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node não está instalado")
        with tempfile.TemporaryDirectory() as t:
            out = Path(t) / "o.html"
            self.assertEqual(run(SAMPLE, out).returncode, 0)
            html = out.read_text(encoding="utf-8")
            scripts = re.findall(r"<script(?![^>]*application/json)[^>]*>(.*?)</script>", html, re.S)
            self.assertTrue(scripts, "nenhum script de página encontrado")
            js = Path(t) / "page.js"
            js.write_text("\n".join(scripts), encoding="utf-8")
            r = subprocess.run([node, "--check", str(js)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)

    def test_id_with_trailing_newline_is_rejected(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        data["items"][0]["id"] = "A\n"
        with tempfile.TemporaryDirectory() as t:
            src = Path(t) / "d.json"; src.write_text(json.dumps(data), encoding="utf-8")
            self.assertNotEqual(run(src, Path(t) / "o.html").returncode, 0)

    def test_bad_inputs_give_a_message_not_a_traceback(self):
        with tempfile.TemporaryDirectory() as t:
            bad = Path(t) / "bad.json"
            bad.write_text("{", encoding="utf-8")
            r = run(bad, Path(t) / "o.html")
            self.assertNotEqual(r.returncode, 0)
            self.assertNotIn("Traceback", r.stderr)
            data = json.loads(SAMPLE.read_text(encoding="utf-8"))
            data["items"][0]["action"] = "texto \ud800 quebrado"
            bad.write_text(json.dumps(data), encoding="utf-8")  # escapa o caractere inválido
            r = run(bad, Path(t) / "o2.html")
            self.assertNotEqual(r.returncode, 0)
            self.assertNotIn("Traceback", r.stderr)
            bad.write_text('{"items": [], "n": ' + "9" * 5000 + "}", encoding="utf-8")
            r = run(bad, Path(t) / "o3.html")
            self.assertNotEqual(r.returncode, 0)
            self.assertNotIn("Traceback", r.stderr)

    def test_sem_trechos_flag_and_evidence_cap(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as t:
            src = Path(t) / "d.json"; src.write_text(json.dumps(data), encoding="utf-8")
            r = subprocess.run([sys.executable, str(RENDER), str(src), str(Path(t) / "o.html"), "--sem-trechos"],
                               capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)  # o exemplo tem texto preenchido
            for it in data["items"]:
                for e in it["evidence"]:
                    e["text"] = ""
            src.write_text(json.dumps(data), encoding="utf-8")
            r = subprocess.run([sys.executable, str(RENDER), str(src), str(Path(t) / "o.html"), "--sem-trechos"],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            data["items"][0]["evidence"] = [{"source": f"s{i}", "text": ""} for i in range(6)]
            src.write_text(json.dumps(data), encoding="utf-8")
            self.assertNotEqual(run(src, Path(t) / "o2.html").returncode, 0)

    def test_headline_is_dropped_so_the_count_stays_right(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        data["headline"] = "Quatro ações. Por onde começar?"
        data["items"] = data["items"][:3]
        with tempfile.TemporaryDirectory() as t:
            src = Path(t) / "d.json"; src.write_text(json.dumps(data), encoding="utf-8")
            out = Path(t) / "o.html"
            self.assertEqual(run(src, out).returncode, 0)
            block = out.read_text(encoding="utf-8").split('id="scenario-data">')[1].split("</script>")[0]
            self.assertNotIn("headline", json.loads(block))

    def test_empty_items_renders(self):
        data = json.loads(SAMPLE.read_text(encoding="utf-8")); data["items"] = []
        with tempfile.TemporaryDirectory() as t:
            src = Path(t) / "e.json"; src.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(run(src, Path(t) / "o.html").returncode, 0)


if __name__ == "__main__":
    unittest.main()
