# Project Apex — Agent onboarding & rules

Single source of truth for **how we work**, **what to read when**, and **non‑negotiable story facts**.  
Read this file at the start of a new chat (or after a long break). Do **not** load the whole repo into context—use the map below.

---

## 1. Read order (minimal vs full)

| Situation | Read |
|-----------|------|
| **Every new session** | This file (`AGENTS.md`), then `_HANDOFF.md` (where we stopped, decisions, next steps). |
| **Editing plot / continuity** | `plot/_TIMELINE.md`, `plot/foreshadowing_plants.md`, relevant slice of `plot/story_plan.md`. |
| **World bible health / approvals** | `world_bible/_STATUS_TRACKER.md` (optional; may be stale—verify against files). |
| **Writing or reviewing prose** | `world_bible/style/style_specification.md` (and §6 Reader inference below). |
| **Scene in a specific place** | Matching file under `world_bible/locations/` (see §4). |
| **Scene focused on specific characters** | Matching file under `world_bible/characters/` + org files if ZPD/ZIA/Apex (see §4). |
| **Gemini / external AI Studio** | Same rules as here; beat sheet → approve → prose workflow applies everywhere. |

---

## 2. File map (what lives where)

### Root (project)

| File | Purpose |
|------|---------|
| `AGENTS.md` | **This file** — rules + map + story facts. |
| `.cursorrules` | Short pointer; full detail is here. |
| `_HANDOFF.md` | Session handoff: last changes, next chapter/scene, open questions. **Update after significant work.** |

### Plot

| Path | Purpose |
|------|---------|
| `plot/story_plan.md` | Master structure: acts, milestones, twists. |
| `plot/_TIMELINE.md` | Chronology—check before changing dates/order. |
| `plot/foreshadowing_plants.md` | Plants/payoffs—don’t break established setups. |
| `plot/act_2_roadmap_v2.md` | Act II roadmap (use this; older roadmap variants may exist). |
| `plot/chapters/*.md` | Draft prose: `prologue.md`, `chapter_XX.md`, split parts (e.g. `chapter_17a.md`, `chapter_17b.md`). |

### World bible — canon & style

| Path | Purpose |
|------|---------|
| `world_bible/canon/zootopia_base.md` | Film 1 canon reference. |
| `world_bible/canon/zootopia2_update.md` | Zootopia 2 notes relevant to project. |
| `world_bible/style/style_specification.md` | Prose rules for LLM drafting. |
| `world_bible/style/character_design_patterns.md` | Archetypes / patterns. |
| `world_bible/style/social_dynamics_guide.md` | Social norms in-story. |
| `world_bible/technology/tech_specification.md` | Tech level / devices when plot needs detail. |

### World bible — organizations (load when scene involves them)

| Path | Purpose |
|------|---------|
| `world_bible/organizations/zpd.md` | ZPD, Strike Force, Antler, Delgato, Bogo, etc. |
| `world_bible/organizations/zia_v2.md` | ZIA structure, Moss, Jack, mole thread. |
| `world_bible/organizations/apex_society.md` | Apex, Magnus, Ragnar, Vesper, Triad, ideology. |

### World bible — locations (load **only** for scenes set there)

| Path | Setting |
|------|---------|
| `world_bible/locations/zpd_precinct1.md` | Precinct / HQ. |
| `world_bible/locations/rainforest_district.md` | Rainforest. |
| `world_bible/locations/port_docks.md` | Docks / port. |
| `world_bible/locations/sahara_square.md` | Sahara Square. |
| `world_bible/locations/tundratown.md` | Tundratown. |
| `world_bible/locations/bunnyburrow.md` | Bunnyburrow. |

### World bible — characters (load **only** for POV or heavy focus)

| Path | Focus |
|------|--------|
| `world_bible/characters/judy_hopps_voice.md` | Judy voice/character. |
| `world_bible/characters/nick_wilde_voice.md` | Nick. |
| `world_bible/characters/skye_winters_voice.md` | Skye. |
| `world_bible/characters/jack_savage_voice.md` | Jack. |
| `world_bible/characters/marian_wilde_baseline.md` | Marian. |

### World bible — meta

| Path | Purpose |
|------|---------|
| `world_bible/_STATUS_TRACKER.md` | What is APPROVED vs DRAFT (may lag behind repo—use as hint). |

### Ignored / heavy (see `.cursorignore`)

Long source texts, archives, duplicate analyses—**do not** load unless the user explicitly asks.

---

## 3. On-demand context (mandatory habit)

- **Never** paste or read “all world bible” for a routine task.
- **Before** drafting or heavily editing a scene:
  - **Location:** open the matching `world_bible/locations/<name>.md` for that scene’s primary setting.
  - **Characters:** open voice/baseline files for every major POV or speaking character in the scene.
  - **Plot locks:** if the scene touches dates, parallel threads, or a plant: `plot/_TIMELINE.md` and/or `plot/foreshadowing_plants.md`.
  - **Organizations:** if ZPD/ZIA/Apex procedure or hierarchy matters: the relevant `world_bible/organizations/*.md` file(s).
- If unsure which file applies, search or ask the user—**do not invent** lore that contradicts existing markdown.

---

## 4. Language

- **`world_bible/` and `plot/` (including chapters):** English only.
- **Chat with the user:** Polish only.
- **Do not mix** languages in one sentence or in one in-project document.

---

## 5. Communication style (chat)

- Concise answers (roughly max 50–100 lines unless the user wants depth).
- Bullet points over long essays when listing.
- Don’t repeat what the user already said.
- **No new files** unless the user explicitly asks (this file and agreed housekeeping excepted).
- No emoji unless the user asks.
- Ending every reply with a forced “what next?” is **not** required; offer a clear next step only when it helps.

---

## 6. Modes & tools

- **Ask mode:** discussion, consistency checks, beat review—no file edits.
- **Agent mode:** edits to bible, plot, chapter `.md` files—batch related edits when possible.
- **External Gemini (optional):** planning/brainstorm; project rules still apply.

**Principle:** think and agree in Ask (cheap); switch to Agent when files must change.

---

## 7. Creative workflow (chapters / scenes)

### 7.1 No preemptive work

- Do **not** produce a beat sheet for the **next** scene/chapter without explicit permission.
- Do **not** produce scene prose without an **approved** beat sheet (or explicit user waiver).
- Stop after the task the user asked for.

### 7.2 Step-by-step (default)

1. Align on goal (short).
2. Beat sheet in **Polish** (bullets)—iterate until the user approves.
3. Prose in **English** in chat—iterate on feedback.
4. Write into `plot/chapters/...` **only** when the user says to add/commit it to the file.

### 7.3 Editing existing prose

- If the user asks for **targeted** fixes, change **only** those spots—do not rewrite the whole scene unless asked.

### 7.4 Reader inference (prose quality)

- Prefer **showing** (body language, scent, pause, action, dialogue) over naming emotions.
- Avoid narrator lines like “she felt X because Y” when the scene already shows it.
- When cutting, remove explanation before removing concrete sensory detail.
- If a story beat would **change canon** or **unlock new plot**: stop and confirm with the user first.

---

## 8. Timeline & lore

- Respect `plot/_TIMELINE.md`, `plot/foreshadowing_plants.md`, and established world bible text.
- If `_HANDOFF.md` disagrees with chapter files or `story_plan.md`, **prefer tracked manuscript + story plan** and flag the conflict to the user.

---

## 9. Handoff between sessions

When context is full or work stops:

1. Update `_HANDOFF.md`: what was done, decisions, **next concrete step** (e.g. “Chapter N beat sheet”).
2. Update `world_bible/_STATUS_TRACKER.md` if approval/status of a bible element changed.
3. Meaningful milestones: git commit (user’s repo).

---

## 10. Key story facts (do not contradict)

- Nick + Judy: close friends; unresolved romantic tension (**not** a couple at story start).
- Skye Winters = Nick’s **adopted sister**—not a romantic rival by design; Judy **misreads** Skye as rival.
- Nick’s father was murdered; criminal org + cover‑ups drive backstory.
- ZIA recruited Nick & Skye using the murder as leverage.
- Marian: alive; holds secrets about the murder.
- Jack Savage: Skye’s ZIA handler; feelings for her; reader/truth layers per `story_plan.md` (asymmetry rules).
- Mole inside ZIA: high‑ranking criminal asset.
- Macro arc: status quo → fake death → Strike Force vs Nick → truth and reunion (details in `story_plan.md`).

For **two‑stage revelation**, **information asymmetry**, **Trojan chip**, and **Act II/III beats**, follow `plot/story_plan.md` and `_HANDOFF.md`—do not override from memory.

---

## 11. Project phases (reference)

High-level pipeline: world bible + plan → detailed breakdown → chapter prose. Completed steps may be marked in `_HANDOFF.md`; use `story_plan.md` as structural source of truth.

---

## 12. Optional: Gemini two-stage reminder

If using Gemini for drafts: **beat sheet (PL) → user approval → prose (EN)**; same file discipline as Cursor. No duplicate rule files needed—everything is in this document.
