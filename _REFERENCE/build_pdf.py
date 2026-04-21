"""Generate Beginners_Project_Guide.pdf from markdown source.

Uses fpdf2 with manual block-level rendering:
  - H1/H2/H3/H4 headings
  - Paragraphs (with **bold** inline)
  - Bulleted/numbered lists
  - Code blocks (fenced ```)
  - Tables (simple pipe)
  - Horizontal rules

Run: python _REFERENCE/build_pdf.py
"""
import re
from pathlib import Path
from fpdf import FPDF

SRC = Path(__file__).with_name("Beginners_Project_Guide.md")
OUT = Path(__file__).with_name("Beginners_Project_Guide.pdf")


class Guide(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Beginner's Project Guide", align="L")
        self.cell(0, 8, f"Page {self.page_no()}", align="R")
        self.ln(12)
        self.set_text_color(0, 0, 0)

    def footer(self):
        pass

    def h1(self, txt):
        self.add_page()
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(20, 40, 90)
        self.multi_cell(0, 10, txt)
        self.ln(2)
        self.set_draw_color(20, 40, 90)
        self.set_line_width(0.6)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_text_color(0, 0, 0)
        self.ln(5)

    def h2(self, txt):
        self.ln(4)
        self.set_font("Helvetica", "B", 15)
        self.set_text_color(20, 40, 90)
        self.multi_cell(0, 8, txt)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def h3(self, txt):
        self.ln(2)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(40, 60, 110)
        self.multi_cell(0, 7, txt)
        self.set_text_color(0, 0, 0)

    def h4(self, txt):
        self.set_font("Helvetica", "BI", 11)
        self.multi_cell(0, 6, txt)

    def para(self, txt):
        self.set_font("Helvetica", "", 11)
        self._render_inline(txt)
        self.ln(2)

    def bullet(self, txt, indent=0):
        self.set_font("Helvetica", "", 11)
        lm = self.l_margin + indent * 5
        self.set_left_margin(lm)
        self.set_x(lm)
        self.cell(4, 6, chr(149))   # bullet
        self._render_inline(txt, line_height=6)
        self.set_left_margin(self.l_margin if indent == 0 else self.l_margin)

    def numbered(self, n, txt):
        self.set_font("Helvetica", "", 11)
        self.cell(7, 6, f"{n}.")
        self._render_inline(txt, line_height=6)

    def checkbox(self, checked, txt):
        self.set_font("Helvetica", "", 11)
        mark = "[x]" if checked else "[ ]"
        self.cell(10, 6, mark)
        self._render_inline(txt, line_height=6)

    def hr(self):
        self.ln(3)
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def code_block(self, code):
        self.ln(1)
        self.set_fill_color(245, 245, 245)
        self.set_font("Courier", "", 9)
        lines = code.splitlines()
        for line in lines:
            self.cell(0, 5, " " + line, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font("Helvetica", "", 11)

    def table(self, rows):
        if not rows:
            return
        self.ln(1)
        cols = len(rows[0])
        avail = self.w - self.l_margin - self.r_margin
        col_w = avail / cols
        self.set_font("Helvetica", "B", 10)
        self.set_fill_color(220, 230, 245)
        for c in rows[0]:
            self.cell(col_w, 7, c.strip(), border=1, fill=True)
        self.ln(7)
        self.set_font("Helvetica", "", 10)
        for row in rows[1:]:
            y0 = self.get_y()
            x0 = self.l_margin
            heights = []
            for c in row:
                self.set_xy(x0, y0)
                self.multi_cell(col_w, 5.5, c.strip(), border=0)
                heights.append(self.get_y() - y0)
                x0 += col_w
            h = max(heights) if heights else 6
            x0 = self.l_margin
            for _ in row:
                self.rect(x0, y0, col_w, h)
                x0 += col_w
            self.set_y(y0 + h)
        self.ln(2)

    def _render_inline(self, txt, line_height=5.5):
        """Render text with **bold** and `code` segments, wrapping safely."""
        # split into (text, style) tokens
        tokens = []
        i = 0
        while i < len(txt):
            if txt.startswith("**", i):
                j = txt.find("**", i + 2)
                if j == -1:
                    tokens.append((txt[i:], ""))
                    break
                tokens.append((txt[i+2:j], "B"))
                i = j + 2
            elif txt[i] == "`":
                j = txt.find("`", i + 1)
                if j == -1:
                    tokens.append((txt[i:], ""))
                    break
                tokens.append((txt[i+1:j], "C"))
                i = j + 1
            else:
                nxt = len(txt)
                for mk in ("**", "`"):
                    p = txt.find(mk, i)
                    if p != -1 and p < nxt:
                        nxt = p
                tokens.append((txt[i:nxt], ""))
                i = nxt

        # render token-by-token with manual wrapping
        avail = self.w - self.r_margin
        for text, style in tokens:
            if style == "B":
                self.set_font("Helvetica", "B", 11)
            elif style == "C":
                self.set_font("Courier", "", 10)
            else:
                self.set_font("Helvetica", "", 11)
            words = re.split(r"(\s+)", text)
            for w in words:
                if not w:
                    continue
                width = self.get_string_width(w)
                if self.get_x() + width > avail:
                    self.ln(line_height)
                self.cell(width, line_height, w)
        self.ln(line_height)


def parse_table(lines, start):
    """Parse a contiguous block of pipe-delimited rows starting at `start`.
    Returns (rows, new_index). Skips the separator row (---|---)."""
    rows = []
    i = start
    while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
        row = [c for c in lines[i].strip().strip("|").split("|")]
        if all(re.fullmatch(r"\s*:?-+:?\s*", c) for c in row):
            i += 1
            continue
        rows.append(row)
        i += 1
    return rows, i


def render(pdf: Guide, md: str):
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # fenced code block
        if line.startswith("```"):
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            pdf.code_block("\n".join(buf))
            i = j + 1
            continue

        # table
        if line.strip().startswith("|") and "|" in line:
            rows, j = parse_table(lines, i)
            if rows:
                pdf.table(rows)
            i = j
            continue

        if not line.strip():
            pdf.ln(2)
            i += 1
            continue

        if line.startswith("# "):
            pdf.h1(line[2:].strip())
        elif line.startswith("## "):
            pdf.h2(line[3:].strip())
        elif line.startswith("### "):
            pdf.h3(line[4:].strip())
        elif line.startswith("#### "):
            pdf.h4(line[5:].strip())
        elif line.strip() == "---":
            pdf.hr()
        elif re.match(r"^\s*- \[[ x]\] ", line):
            m = re.match(r"^(\s*)- \[([ x])\] (.*)", line)
            indent = len(m.group(1)) // 2
            pdf.set_left_margin(pdf.l_margin)
            pdf.set_x(pdf.l_margin + indent * 5)
            pdf.checkbox(m.group(2) == "x", m.group(3))
        elif re.match(r"^\s*- ", line):
            m = re.match(r"^(\s*)- (.*)", line)
            indent = len(m.group(1)) // 2
            pdf.bullet(m.group(2), indent=indent)
        elif re.match(r"^\s*\d+\. ", line):
            m = re.match(r"^\s*(\d+)\. (.*)", line)
            pdf.numbered(m.group(1), m.group(2))
        else:
            pdf.para(line.strip())
        i += 1


UNICODE_FIX = {
    "—": " - ",   # em dash
    "–": "-",     # en dash
    "‘": "'", "’": "'",
    "“": '"', "”": '"',
    "…": "...",
    " ": " ",
    "→": "->",
    "←": "<-",
    "≥": ">=", "≤": "<=",
    "×": "x",
    "·": "*", "•": "*",
    "µ": "u",
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
    "ε": "eps", "η": "eta", "μ": "mu", "π": "pi",
    "ρ": "rho", "σ": "sigma", "τ": "tau", "φ": "phi",
    "χ": "chi", "ω": "omega",
    "Δ": "Delta", "Σ": "Sigma", "Π": "Pi", "Ω": "Omega",
    "≈": "~", "≠": "!=", "±": "+/-",
    "²": "^2", "³": "^3",
    "′": "'", "″": '"',
    "√": "sqrt", "∑": "Sum", "∏": "Prod",
    "∈": " in ", "⊆": " subset ",
    "×": "x",
}


def normalize(txt: str) -> str:
    for k, v in UNICODE_FIX.items():
        txt = txt.replace(k, v)
    return txt.encode("latin-1", "replace").decode("latin-1")


def main():
    md = normalize(SRC.read_text())
    pdf = Guide(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(left=18, top=18, right=18)

    # cover page
    pdf.add_page()
    pdf.set_y(60)
    pdf.set_font("Helvetica", "B", 26)
    pdf.set_text_color(20, 40, 90)
    pdf.multi_cell(0, 12,
        "A Beginner's Guide to Planning\nRobust, Secure, Reliable, and Scalable Projects",
        align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "I", 14)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 8,
        "...and keeping `main` independent of `develop`, always.",
        align="C")
    pdf.ln(40)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 6,
        "A practical, opinionated handbook for first-time project planners.",
        align="C")
    pdf.set_text_color(0, 0, 0)

    render(pdf, md)
    pdf.output(str(OUT))
    print(f"wrote {OUT} ({OUT.stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
