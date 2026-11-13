#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO-Ops helper for the Javis brain. Standard library only.

    python tools/seo_ops.py build   # rewrite the generated files
    python tools/seo_ops.py check   # find broken references, change nothing
    python tools/seo_ops.py new-run <slug> <task> <topic> <workflow> [owner]
                                    # create Projects/<slug>/runs/<today>_<task>_<topic>/RUN.md
    python tools/seo_ops.py set-run <run-folder> key=value [key=value ...]
                                    # change fields at the top of a RUN.md (updated is set to today)
    python tools/seo_ops.py xlsx <file.csv> [<file.csv> ...]
                                    # write an .xlsx copy next to each csv (needs openpyxl)
    python tools/seo_ops.py hypotheses <slug>
                                    # list hypothetical test files still in place (HYPOTHESIS.md)

Generated files (never edit by hand):
    Projects/_registry/projects.csv   from every Projects/<slug>/PROJECT.md
    Projects/_registry/board.csv      from every Projects/<slug>/runs/*/RUN.md
    Projects/CATALOG.md               from every workflows/*.md
"""
import csv
import datetime
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "Projects"
REGISTRY = PROJECTS / "_registry" / "projects.csv"
BOARD = PROJECTS / "_registry" / "board.csv"
CATALOG = PROJECTS / "CATALOG.md"

STAGES = {"prospect", "client", "paused", "lost"}
RUN_STATUS = {"open", "waiting", "qa", "approved", "published", "cancelled"}
RUN_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9-]+_[a-z0-9-]+$")

# registry column -> PROJECT.md field
REGISTRY_COLS = [
    ("slug", "slug"), ("client", "client"), ("stage", "stage"),
    ("domain", "domain"), ("market", "market"), ("type", "site_type"),
    ("platform", "platform"), ("scope", "scope"), ("owner", "owner"),
    ("approver", "approver"), ("priority", "priority"),
    ("compliance", "compliance"), ("content_skill", "skill_blog"),
    ("collection_skill", "skill_collection"),
    ("product_skill", "skill_product"), ("report_day", "report_day"),
    ("notes", "notes"),
]
PROJECT_REQUIRED = ["slug", "client", "stage", "market"]
PROJECT_SKILL_FIELDS = ["skill_blog", "skill_collection", "skill_product", "compliance"]
BOARD_COLS = ["client", "run", "task", "topic", "workflow", "status", "owner",
              "created", "updated", "next_step", "live_url", "published_on", "path"]
RUN_REQUIRED = ["client", "task", "topic", "workflow", "status", "owner", "next_step"]

# seo-* words that are not a workflow, agent or skill
SEO_WORD_OK = {"seo-ops"}


def read(path):
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def frontmatter(text):
    """Return (fields, raw_block, body). Flat `key: value` lines only."""
    if not text.startswith("---\n"):
        return None, "", text
    end = text.find("\n---", 4)
    if end == -1:
        return None, "", text
    raw = text[4:end]
    body = text[end + 4:].lstrip("\n")
    fields = {}
    for line in raw.split("\n"):
        if not line or line[0] in " \t#-":
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        fields[key.strip()] = value
    return fields, raw, body


def names(folder, dirs=False):
    path = ROOT / folder
    if not path.is_dir():
        return set()
    if dirs:
        return {p.name for p in path.iterdir() if p.is_dir()}
    return {p.stem for p in path.glob("*.md")}


def clients():
    if not PROJECTS.is_dir():
        return []
    return sorted(p for p in PROJECTS.iterdir()
                  if p.is_dir() and not p.name.startswith(("_", ".")))


def load_projects():
    out = []
    for folder in clients():
        pfile = folder / "PROJECT.md"
        fields = None
        if pfile.is_file():
            fields, _, _ = frontmatter(read(pfile))
        out.append((folder, fields))
    return out


def load_runs():
    out = []
    for folder in clients():
        runs = folder / "runs"
        if not runs.is_dir():
            continue
        for run in sorted(p for p in runs.iterdir() if p.is_dir()):
            rfile = run / "RUN.md"
            fields = None
            if rfile.is_file():
                fields, _, _ = frontmatter(read(rfile))
            out.append((folder.name, run, fields))
    return out


def load_workflows():
    out = []
    wdir = ROOT / "workflows"
    if not wdir.is_dir():
        return out
    for wfile in sorted(wdir.glob("*.md")):
        text = read(wfile)
        fields, raw, body = frontmatter(text)
        fields = fields or {}
        agents = re.findall(r"^\s*-?\s*(?:verify_)?agent:\s*([A-Za-z0-9_-]+)", raw, re.M)
        m = re.search(r"Đầu vào gồm:\s*(.+)", raw)
        out.append({
            "file": wfile, "text": text, "fields": fields, "agents": agents,
            "input": m.group(1).strip().rstrip(".") if m else "",
            "body": " ".join(body.split()),
        })
    return out


def to_csv(header, rows):
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return buf.getvalue()


def build_registry():
    rows = []
    for folder, fields in load_projects():
        if not fields:
            continue
        rows.append([fields.get(src, "") for _, src in REGISTRY_COLS])
    return to_csv([col for col, _ in REGISTRY_COLS], rows)


def build_board():
    rows = []
    for slug, run, fields in load_runs():
        if not fields:
            continue
        row = {c: fields.get(c, "") for c in BOARD_COLS}
        row["client"] = slug
        row["run"] = run.name
        row["path"] = run.relative_to(ROOT).as_posix()
        rows.append([row[c] for c in BOARD_COLS])
    return to_csv(BOARD_COLS, rows)


def skills_in(text, skills):
    found = []
    for skill in sorted(skills):
        if "-" not in skill:
            continue
        if re.search(r"(?<![\w-])" + re.escape(skill) + r"(?![\w-])", text):
            found.append(skill)
    return found


def build_catalog():
    skills = names("skills", dirs=True)
    cell = lambda s: s.replace("|", "\\|")
    lines = [
        "# CATALOG: danh sách tác vụ SEO-Ops",
        "",
        "> File tự sinh từ `workflows/*.md` bằng `python tools/seo_ops.py build`. Không sửa tay.",
        "> Muốn đổi bước của một tác vụ: sửa file workflow rồi chạy lại lệnh build.",
        "",
        "| Workflow | Tên | Trạng thái | Chuỗi agent | Đầu vào (một dòng, cách nhau bằng dấu \\|) | Skill được gọi |",
        "|---|---|---|---|---|---|",
    ]
    notes = []
    for wf in load_workflows():
        f = wf["fields"]
        slug = f.get("slug", wf["file"].stem)
        lines.append("| `%s` | %s | %s | %s | %s | %s |" % (
            slug, cell(f.get("name", "")), f.get("status", ""),
            " -> ".join(wf["agents"]), cell(wf["input"]),
            ", ".join(skills_in(wf["text"], skills)
                      + ["%s (PROJECT.md)" % f for f in PROJECT_SKILL_FIELDS
                         if re.search(r"\b%s\b" % f, wf["text"])])))
        if wf["body"]:
            notes.append("- `%s`: %s" % (slug, wf["body"]))
    lines += ["", "## Ghi chú từng workflow", ""] + notes + [""]
    return "\n".join(lines)


GENERATED = [(REGISTRY, build_registry), (BOARD, build_board), (CATALOG, build_catalog)]


def cmd_build():
    for path, builder in GENERATED:
        content = builder()
        path.parent.mkdir(parents=True, exist_ok=True)
        old = read(path) if path.is_file() else None
        if old == content:
            print("unchanged  %s" % path.relative_to(ROOT).as_posix())
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        print("written    %s" % path.relative_to(ROOT).as_posix())
    return 0


def check_path(ref):
    """True when a path written in a workflow, agent or rule file exists."""
    ref = ref.replace("<slug>", "_template")
    parts = [p for p in ref.split("/") if p]
    keep = []
    for part in parts:
        if re.search(r"[<>*{}\[\]]|YYYY|\.\.\.", part):
            break
        keep.append(part)
    return (ROOT / Path(*keep)).exists()


def hypothesis_files(folder):
    """Files listed in Projects/<slug>/HYPOTHESIS.md that are still on disk."""
    hfile = folder / "HYPOTHESIS.md"
    if not hfile.is_file():
        return []
    listed = re.findall(r"^\|\s*`([^`]+)`\s*\|", read(hfile), re.M)
    return [rel for rel in listed if (folder / rel).exists()]


def cmd_hypotheses(args):
    if len(args) != 1:
        print("usage: hypotheses <slug>")
        return 2
    folder = PROJECTS / args[0]
    if not (folder / "HYPOTHESIS.md").is_file():
        print("No HYPOTHESIS.md in Projects/%s" % args[0])
        return 0
    left = hypothesis_files(folder)
    for rel in left:
        print("HYPOTHESIS  Projects/%s/%s" % (args[0], rel))
    print("%d hypothetical file(s) still in place. Replace with real data, then remove the line from HYPOTHESIS.md." % len(left))
    return 0


def cmd_check():
    errors, warnings = [], []
    agents = names("agents")
    skills = names("skills", dirs=True)
    workflows = load_workflows()
    wf_slugs = {w["fields"].get("slug", w["file"].stem) for w in workflows}
    known_seo = agents | skills | wf_slugs | SEO_WORD_OK

    # 1. Workflows: agents exist, slug matches the file name
    for wf in workflows:
        rel = wf["file"].relative_to(ROOT).as_posix()
        slug = wf["fields"].get("slug", "")
        if slug != wf["file"].stem:
            errors.append("%s: slug '%s' differs from the file name" % (rel, slug))
        if not wf["agents"]:
            errors.append("%s: no step with an agent" % rel)
        for agent in wf["agents"]:
            if agent not in agents:
                errors.append("%s: agent '%s' is not in agents/" % (rel, agent))

    # 2. References inside workflows, agents, the rule file and templates
    scan = [w["file"] for w in workflows]
    scan += sorted((ROOT / "agents").glob("*.md")) if (ROOT / "agents").is_dir() else []
    scan += [PROJECTS / "SEO-OPS.md"]
    scan += sorted((PROJECTS / "_templates").glob("*.md")) if (PROJECTS / "_templates").is_dir() else []
    for path in scan:
        if not path.is_file():
            errors.append("%s: file is missing" % path.relative_to(ROOT).as_posix())
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = read(path)
        for word in sorted(set(re.findall(r"(?<![\w/.-])seo-[a-z0-9]+(?:-[a-z0-9]+)*(?![\w.-])", text))):
            if word not in known_seo:
                errors.append("%s: '%s' is not a workflow, agent or skill" % (rel, word))
        named = set(re.findall(r"(?:[Ss]kills?|chạy|Chạy)\s+`?/?([a-z0-9]+(?:-[a-z0-9]+)+)", text))
        named |= set(re.findall(r"(?<![\w/:.<])/([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w/.-])", text))
        for skill in sorted(named):
            if skill not in skills and skill not in wf_slugs and skill not in agents:
                errors.append("%s: skill '%s' is not in skills/" % (rel, skill))
        for ref in sorted(set(re.findall(r"(?<![\w/.-])(?:Projects|agents|workflows|skills|tools)/[^\s`\"'),;|]*", text))):
            ref = ref.rstrip(".:")
            if not check_path(ref):
                errors.append("%s: path '%s' does not exist" % (rel, ref))

    # 3. Client folders
    for folder, fields in load_projects():
        rel = folder.relative_to(ROOT).as_posix()
        if not (folder / "PROJECT.md").is_file():
            errors.append("%s: PROJECT.md is missing" % rel)
            continue
        if fields is None:
            errors.append("%s/PROJECT.md: no field block at the top (--- ... ---)" % rel)
            continue
        for key in PROJECT_REQUIRED:
            if not fields.get(key):
                errors.append("%s/PROJECT.md: field '%s' is empty" % (rel, key))
        if fields.get("slug") and fields["slug"] != folder.name:
            errors.append("%s/PROJECT.md: slug '%s' differs from the folder name" % (rel, fields["slug"]))
        if fields.get("stage") and fields["stage"] not in STAGES:
            errors.append("%s/PROJECT.md: stage '%s' is not one of %s" % (rel, fields["stage"], ", ".join(sorted(STAGES))))
        for key in PROJECT_SKILL_FIELDS:
            value = fields.get(key, "")
            if value and value not in skills:
                errors.append("%s/PROJECT.md: %s '%s' is not in skills/" % (rel, key, value))
        if fields.get("test_data") == "yes":
            if (folder / "HYPOTHESIS.md").is_file():
                left = hypothesis_files(folder)
                warnings.append("%s: test_data is yes, %d hypothetical file(s) still in place (python tools/seo_ops.py hypotheses %s)" % (rel, len(left), folder.name))
            else:
                warnings.append("%s: test_data is yes (test client, never deliver its files)" % rel)
        for sub in ("runs", "deliverables"):
            if not (folder / sub).is_dir():
                warnings.append("%s: folder %s/ is missing" % (rel, sub))

    # 4. Runs
    for slug, run, fields in load_runs():
        rel = run.relative_to(ROOT).as_posix()
        if not RUN_DIR.match(run.name):
            errors.append("%s: folder name is not YYYY-MM-DD_<task>_<topic>" % rel)
        if fields is None:
            errors.append("%s: RUN.md is missing or has no field block" % rel)
            continue
        for key in RUN_REQUIRED:
            if not fields.get(key):
                errors.append("%s/RUN.md: field '%s' is empty" % (rel, key))
        if fields.get("client") and fields["client"] != slug:
            errors.append("%s/RUN.md: client '%s' differs from the folder '%s'" % (rel, fields["client"], slug))
        if fields.get("status") and fields["status"] not in RUN_STATUS:
            errors.append("%s/RUN.md: status '%s' is not one of %s" % (rel, fields["status"], ", ".join(sorted(RUN_STATUS))))
        if fields.get("workflow") and fields["workflow"] not in wf_slugs:
            errors.append("%s/RUN.md: workflow '%s' is not in workflows/" % (rel, fields["workflow"]))
        if fields.get("status") == "published":
            for key in ("live_url", "published_on"):
                if not fields.get(key):
                    errors.append("%s/RUN.md: status is published but '%s' is empty" % (rel, key))

    # 5. Generated files in step with their sources
    for path, builder in GENERATED:
        rel = path.relative_to(ROOT).as_posix()
        if not path.is_file():
            errors.append("%s: missing, run: python tools/seo_ops.py build" % rel)
        elif read(path) != builder():
            errors.append("%s: out of step with its sources, run: python tools/seo_ops.py build" % rel)

    for line in warnings:
        print("WARN   " + line)
    for line in errors:
        print("ERROR  " + line)
    print("%d error(s), %d warning(s). Checked %d workflows, %d agents, %d client folders, %d runs." % (
        len(errors), len(warnings), len(workflows), len(agents), len(clients()), len(load_runs())))
    return 1 if errors else 0


RUN_FIELDS = ["client", "task", "topic", "workflow", "status", "owner", "created",
              "updated", "next_step", "live_url", "published_on"]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def today():
    return datetime.date.today().isoformat()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def set_fields(text, values):
    """Replace or add `key: value` lines in the field block of a RUN.md."""
    if not text.startswith("---\n"):
        raise ValueError("no field block at the top")
    end = text.find("\n---", 4)
    lines = text[4:end].split("\n")
    for key, value in values.items():
        value = " ".join(str(value).split())
        for i, line in enumerate(lines):
            if line.split(":", 1)[0].strip() == key:
                lines[i] = "%s: %s" % (key, value)
                break
        else:
            lines.append("%s: %s" % (key, value))
    return "---\n" + "\n".join(lines) + text[end:]


def cmd_new_run(args):
    if len(args) not in (4, 5):
        print("usage: new-run <slug> <task> <topic> <workflow> [owner]")
        return 2
    slug, task, topic, workflow = args[:4]
    owner = args[4] if len(args) == 5 else ""
    for name, value in (("slug", slug), ("task", task), ("topic", topic)):
        if not SLUG.match(value):
            print("ERROR  %s '%s': use lowercase letters, digits and single hyphens" % (name, value))
            return 1
    client = PROJECTS / slug
    if not (client / "PROJECT.md").is_file():
        print("ERROR  Projects/%s/PROJECT.md not found" % slug)
        return 1
    if not owner:
        fields, _, _ = frontmatter(read(client / "PROJECT.md"))
        owner = (fields or {}).get("owner", "")
    run = client / "runs" / ("%s_%s_%s" % (today(), task, topic))
    if run.exists():
        print("EXISTS %s" % run.relative_to(ROOT).as_posix())
        return 0
    template = PROJECTS / "_templates" / "RUN.md"
    text = read(template) if template.is_file() else "---\n---\n"
    text = set_fields(text, {"client": slug, "task": task, "topic": topic,
                             "workflow": workflow, "status": "open", "owner": owner,
                             "created": today(), "updated": today(),
                             "next_step": "đang chạy %s" % workflow})
    text = text.replace("<task> - <topic>", "%s - %s" % (task, topic), 1)
    run.mkdir(parents=True)
    write_text(run / "RUN.md", text)
    print("CREATED %s" % run.relative_to(ROOT).as_posix())
    return 0


def resolve_run(arg):
    path = Path(arg)
    if not path.is_absolute():
        path = ROOT / path
    if path.name == "RUN.md":
        path = path.parent
    return path


def cmd_set_run(args):
    if len(args) < 2:
        print("usage: set-run <run-folder> key=value [key=value ...]")
        return 2
    run = resolve_run(args[0])
    rfile = run / "RUN.md"
    if not rfile.is_file():
        print("ERROR  %s not found" % rfile)
        return 1
    values = {}
    for pair in args[1:]:
        if "=" not in pair:
            print("ERROR  '%s' is not key=value" % pair)
            return 1
        key, value = pair.split("=", 1)
        if key not in RUN_FIELDS:
            print("ERROR  '%s' is not a RUN.md field (%s)" % (key, ", ".join(RUN_FIELDS)))
            return 1
        values[key] = value
    if values.get("status") and values["status"] not in RUN_STATUS:
        print("ERROR  status must be one of %s" % ", ".join(sorted(RUN_STATUS)))
        return 1
    values.setdefault("updated", today())
    write_text(rfile, set_fields(read(rfile), values))
    print("UPDATED %s" % rfile.relative_to(ROOT).as_posix())
    return 0


def cmd_xlsx(args):
    if not args:
        print("usage: xlsx <file.csv> [<file.csv> ...]")
        return 2
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font
    except ImportError:
        print("ERROR  openpyxl is not installed: pip install openpyxl. The csv files are unchanged.")
        return 1
    status = 0
    for arg in args:
        src = Path(arg)
        if not src.is_absolute():
            src = ROOT / src
        if not src.is_file() or src.suffix.lower() != ".csv":
            print("ERROR  %s is not a csv file" % arg)
            status = 1
            continue
        with open(src, encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.reader(fh))
        wb = Workbook()
        ws = wb.active
        ws.title = src.stem[:31]
        for r, row in enumerate(rows):
            out = []
            for value in row:
                if r and re.fullmatch(r"-?\d+", value or ""):
                    out.append(int(value))
                elif r and re.fullmatch(r"-?\d+\.\d+", value or ""):
                    out.append(float(value))
                else:
                    out.append(value)
            ws.append(out)
        if rows:
            for cell in ws[1]:
                cell.font = Font(bold=True)
            ws.freeze_panes = "A2"
            for i, col in enumerate(ws.columns, 1):
                width = max(len(str(c.value or "")) for c in col)
                ws.column_dimensions[col[0].column_letter].width = min(max(width + 2, 8), 60)
        dst = src.with_suffix(".xlsx")
        wb.save(dst)
        print("WRITTEN %s" % (dst.relative_to(ROOT).as_posix() if dst.is_relative_to(ROOT) else dst))
    return status


def main(argv):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    commands = {"build": lambda a: cmd_build(), "check": lambda a: cmd_check(),
                "new-run": cmd_new_run, "set-run": cmd_set_run, "xlsx": cmd_xlsx,
                "hypotheses": cmd_hypotheses}
    if len(argv) < 2 or argv[1] not in commands:
        print(__doc__)
        return 2
    if argv[1] in ("build", "check") and len(argv) != 2:
        print(__doc__)
        return 2
    return commands[argv[1]](argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
