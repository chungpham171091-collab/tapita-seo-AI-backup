# How SEO-Ops works (and how to change it)

> For people and for the config assistant (`seo-config-assistant`). Every rule below is enforced by the Projects page or by `python tools/seo_ops.py check`. Cross-client content rules stay in `Projects/SEO-OPS.md`; this file is about the machinery.

## 1. Four layers, each in its own files

| Layer | What it decides | File(s) | Change it from |
|---|---|---|---|
| Job type (playbook) | Which stages a job has, in what order, who does each, which fields you fill when you create it, which files count as the result | `Projects/_templates/playbooks.json` (all projects), `Projects/<slug>/playbooks.json` (one project) | Playbooks > Edit job type |
| Workflow | What the AI does in one stage: the chain of agents and the task text each one gets | `workflows/<name>.md`; a one-project copy is `workflows/<name>--<slug>.md` | Job > stage > Open workflow > Edit |
| Agent | Role, limits, model, reasoning level | `agents/<slug>.md` | Workflow editor (model), or the Javis Teams page |
| Skill | Writing rules for one content type | `skills/<name>/SKILL.md`, chosen per client in PROJECT.md | Javis Skills page |

Other settings: data sources `Projects/_templates/data_sources.csv`, the team `Projects/team.csv`, single-workflow forms `Projects/_templates/task_forms.json`.

## 2. Scope: every project or one project
- Saving with scope "all projects" changes the shared file.
- Scope "only this project":
  - job type: the whole job type is copied into `Projects/<slug>/playbooks.json` (same `id` replaces the shared one for that client; a new `id` adds a job type only that client sees);
  - workflow: copied to `workflows/<name>--<slug>.md`, and `Projects/<slug>/playbook_overrides.json` points that client's stages to the copy.
- A client file `Projects/<slug>/playbooks.json` has the same shape as the shared one (`{"playbooks": [...]}`) but holds only the job types that differ for that client, plus any job type only that client has. Do not copy job types that stay the same.
- Every save keeps the previous version (Versions button). Restore puts an old version back.

## 3. Job type format (one entry of `playbooks`)
```
id        lowercase id, unique             title   name shown on the page
group     Planning | Content | Maintain | Off-page | GEO | Report | Technical (or a new group)
task      word used in the job folder name (YYYY-MM-DD_<task>_<topic>)
what      one sentence shown when choosing the job type
start     fields asked when creating the job: {key, label, default, help, required, slug, type: "select", options}
          one field must have key "topic" (it names the folder). Defaults may use {month}, {prev_month}, {today}.
vars      optional derived values, for example {"target": "{collection_url}"}
stages    ordered list, see below
```
Stage kinds:
- `ai`: runs `workflow` with `input` (list of values, one per part of the workflow's "Đầu vào gồm:" line after the client slug). `outputs` = files that must exist after the run; `checks` = `verdict` (QA says đạt) or `serp_urls[:file]` (real URLs present); `pass_run: true` adds `run=<job folder>` to the input; `needs` = data source ids shown as ready or missing; `optional`/`enabled` for stages that can be switched off.
- `decision`: a person answers `ask` fields (same format as start fields) after reading `shows` files.
- `upload`: a person uploads one file, saved as `save_as`, types in `accept`.
- `upload_data`: a person uploads to the data source `slot` (an id from data_sources.csv).
- `approve`: the project owner approves `deliver` files (copied to deliverables/) or sends them back; `revise` = the workflow that applies the comment; `install_to` = also replace this data file on approval.
- `deliver`: a person makes a share link or downloads the approved file, sends it, and records who got it. Javis sends nothing.
- `publish`: a person publishes and records the live URL.
Values usable in `input`, `outputs`, `deliver`, `shows`: `{run} {country} {market} {today} {month} {prev_month} {owner}`, every start field key, every decision `ask` key, `{deliverable}`, `{feedback}`, and `latest:<pattern>` for the newest matching file.

## 4. Workflow format
YAML block at the top: `type: workflow`, `name`, `slug` (= file name), `status`, `description`, `steps` (list of `agent` + `task`), `updated`. In a task, `{{input}}` is the input line and `{{prev}}` the previous agent's answer. The first task must contain the line `Đầu vào gồm: slug khách | ...`; the number of parts after the slug must equal the stage's `input` count. A workflow that receives `run=<path>` writes only into that folder.

## 5. Decisions from a person in the middle of a stage
An agent that cannot finish without a person writes `needs.json` in the job folder (format in SEO-OPS.md). After the stage, the page shows each item as a question with choices, a text box or a file upload. "Send answers and run again" appends the answers to `decisions.md` in the job folder and reruns the stage; agents read `decisions.md` first. "Accept as is and continue" moves on and records the answers.

## 6. Rules the page enforces
- Only the project owner approves (others can, after a warning).
- A stage that needs something unavailable (System check) shows a red warning on the stage.
- Nothing sends email or messages; delivery is recorded by a person.
- Workflows run on the Javis server; closing the tab does not stop them.
- Client data never goes into another client's job (one client per job and per conversation).
