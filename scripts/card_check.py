#!/usr/bin/env python3
"""Mechanical part of the send gate of the author walk (references/author-walk.md, stage 4).

Reports markers to inspect in a drafted passage. It never certifies writing: exit 0 means the
measurement ran and found no marker; exit 1 means at least one marker; exit 2 is a usage or input error.

    card_check.py DRAFT [--before BEFORE] [--rise] [--actors PRON:NAME[,PRON:NAME...]] [--max-ratio 1.0]

--rise     the passage is meant to build a surprise: every sentence after the first should open
           with a linking word, and a turn ("Yet"/"But"/"However") should be present.
--actors   e.g. she:buyer,she:seller: if two named actors that share a pronoun
           both occur, each sentence using that pronoun is listed for inspection.
--before   the paper's current text; reports the length ratio AFTER/BEFORE.
"""

import argparse
import re
import sys

COUNTING = re.compile(
    r"\b(two|three|four|five|several) (results|things|facts|objects|features|steps|points|forces|channels) "
    r"(emerge|matter|stand out|follow)\b|\bin turn:|\bFirst,.{0,400}\bSecond,",
    re.I | re.S,
)
ENUM = re.compile(r"(?<![A-Za-z0-9])(?<![Pp]anel )(?<![Pp]anels )\((i|ii|iii|iv|v|a|b|c)\)\s")
CLEAR = re.compile(
    r"\b(clearly|obviously|of course|it is clear that|the clear(er|est)? one|needless to say|"
    r"it is easy to see|as is well known)\b",
    re.I,
)
JARGON = re.compile(
    r"\b(slot|conjectur\w*|inherits?|pins? down|pinned|floored|in miniature|"
    r"filters? out|shades? its|put(s)? probability|sits (at|in|on|one|below|above))\b",
    re.I,
)
HEDGE = re.compile(
    r"\b(by assumption|to first order|arguably|it should be noted|we note that|importantly|"
    r"more importantly|interestingly|notably)\b",
    re.I,
)
RECAP = re.compile(r"\bfor reference\b|\brecall that\b.{0,200}\bare the\b", re.I | re.S)
PROOF_PTR = re.compile(
    r"(derivations?|proofs?|details?) (is|are) (in|deferred to|given in|relegated to) "
    r"(the )?(appendix|\\cref|appendices)",
    re.I,
)
DASH = re.compile(r"\u2014|---| -- |\u2013 | - (?=[a-z])")
LINKS = (
    "yet",
    "but",
    "however",
    "surprisingly",
    "more surprisingly",
    "thus",
    "therefore",
    "hence",
    "so ",
    "because",
    "since",
    "by contrast",
    "moreover",
    "nor",
    "instead",
    "judged",
    "this ",
    "that ",
    "these ",
    "the same",
    "it ",
    "its ",
    "she ",
    "he ",
    "they ",
    "her ",
    "their ",
    "then",
    "consequently",
    "indeed",
    "in turn",
    "as a result",
    "for example",
    "finally",
    "without",
    "with ",
    "after",
    "before",
    "once",
    "when",
    "if ",
    "whereas",
    "while",
    "to see",
    "to establish",
    "one would",
    "who",
    "what",
    "why",
    "how",
    "both",
    "each",
    "neither",
    "either",
    "part of",
    "the more",
    "the lower",
    "the higher",
    "and ",
    "or ",
    "we ",
    "in equilibrium",
    "in the baseline",
    "at ",
    "here",
    "there",
    "such",
    "another",
    "a second",
)


def sentences(text):
    text = re.sub(r"\s+", " ", text.strip())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\\\[\(\"'`*])", text)
    return [p for p in parts if p]


def words(text):
    return len(re.findall(r"[A-Za-z0-9\\$]+", text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--before")
    ap.add_argument("--rise", action="store_true")
    ap.add_argument("--actors", default="")
    ap.add_argument("--max-ratio", type=float, default=None)
    a = ap.parse_args()
    try:
        text = open(a.draft, encoding="utf-8").read()
    except OSError as e:
        print(f"ERROR cannot read draft: {e}", file=sys.stderr)
        return 2
    if not text.strip():
        print("ERROR draft is empty", file=sys.stderr)
        return 2

    marks = []

    def scan(name, rx):
        for m in rx.finditer(text):
            s = max(0, m.start() - 40)
            marks.append((name, text[s : m.end() + 40].replace("\n", " ")))

    scan("DASH", DASH)
    scan("COUNTING_OPENER", COUNTING)
    scan("IN_TEXT_ENUMERATION", ENUM)
    scan("TELLS_READER_IT_IS_CLEAR", CLEAR)
    scan("JARGON_LIST", JARGON)
    scan("HEDGE_OR_FILLER", HEDGE)
    scan("NOTATION_RECAP", RECAP)
    scan("POINTER_TO_PROOF", PROOF_PTR)

    sents = sentences(text)
    long_s = [s for s in sents if words(s) > 45]
    for s in long_s:
        marks.append(("LONG_SENTENCE_OVER_45_WORDS", s[:110]))

    if a.rise:
        for s in sents[1:]:
            low = s.lower().lstrip("\\*`\"'(")
            if not low.startswith(LINKS):
                marks.append(("RISE_SENTENCE_WITHOUT_LINKING_OPENER", s[:90]))
        if not re.search(r"\b(Yet|But|However)\b", text):
            marks.append(
                ("RISE_WITHOUT_A_TURN", "no sentence turns with Yet/But/However")
            )
        if not (
            sents
            and (
                sents[0].rstrip().endswith("?")
                or re.search(
                    r"one would expect|is expected|" r"the natural|in a standard",
                    sents[0] + (sents[1] if len(sents) > 1 else ""),
                    re.I,
                )
            )
        ):
            marks.append(
                ("RISE_WITHOUT_EXPECTATION_OR_QUESTION", sents[0][:90] if sents else "")
            )

    if a.actors:
        groups = {}
        for item in a.actors.split(","):
            if ":" not in item:
                print(f"ERROR bad --actors item: {item}", file=sys.stderr)
                return 2
            pron, name = item.split(":", 1)
            groups.setdefault(pron.strip().lower(), []).append(
                name.strip().strip('"').lower()
            )
        poss = {
            "she": r"\b(she|her|hers)\b",
            "he": r"\b(he|him|his)\b",
            "it": r"\b(it|its)\b",
            "they": r"\b(they|them|their)\b",
        }
        for pron, names in groups.items():
            present = [n for n in names if n in text.lower()]
            if len(present) >= 2:
                rx = re.compile(poss.get(pron, rf"\b{re.escape(pron)}\b"), re.I)
                for i, s in enumerate(sents):
                    if not rx.search(s):
                        continue
                    here = [n for n in present if n in s.lower()]
                    prev = [n for n in present if i > 0 and n in sents[i - 1].lower()]
                    if len(here) != 1 and not (len(here) == 0 and len(prev) == 1):
                        marks.append(
                            (
                                f"PRONOUN_{pron.upper()}_AMBIGUOUS_BETWEEN_{'_AND_'.join(present)}",
                                s[:100],
                            )
                        )

    print(f"sentences={len(sents)} words={words(text)}")
    if a.before:
        try:
            b = open(a.before, encoding="utf-8").read()
        except OSError as e:
            print(f"ERROR cannot read before: {e}", file=sys.stderr)
            return 2
        ratio = words(text) / max(1, words(b))
        print(f"before_words={words(b)} ratio={ratio:.2f}")
        if a.max_ratio is not None and ratio > a.max_ratio:
            marks.append(("LONGER_THAN_ALLOWED", f"ratio {ratio:.2f} > {a.max_ratio}"))
    if not marks:
        print("NO_MARKER (measurement completed; this is not a quality verdict)")
        return 0
    for name, ctx in marks:
        print(f"MARK {name}: ...{ctx}...")
    print(f"markers={len(marks)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
