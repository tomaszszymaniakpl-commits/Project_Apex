# WORLD BIBLE - STATUS TRACKER

> Central status map for all world bible elements  
> **Use this to check what can be treated as final vs what may change**

*Last updated: 2026-02-16*

---

## STATUS LEGEND

- APPROVED - Final decisions, safe to reference
- DRAFT - Needs review/corrections before finalization
- EXAMPLE - Concept illustration, not final (will be replaced)
- PLACEHOLDER - Requires user decision
- IN PROGRESS - Currently being created
- PAUSED - Postponed for later

---

## CANON & FOUNDATIONS

| Element | File | Status | Confidence | Notes |
|---------|------|---------|------------|--------|
| Zootopia Film 1 Facts | `canon/zootopia_base.md` | APPROVED | HIGH | Established canon reference |
| Zootopia 2 Updates | `canon/zootopia2_update.md` | APPROVED | HIGH | Nick+Judy platonic confession |

---

## STORY PLAN

| Element | File | Status | Confidence | Notes |
|---------|------|---------|------------|--------|
| **Master Story Plan** | `plot/story_plan.md` | APPROVED | HIGH | Full 3-act structure with milestones |
| Project Title | - | APPROVED | HIGH | "PROJECT APEX" |
| Logline | `plot/story_plan.md` | APPROVED | HIGH | Infiltration / betrayal / redemption |

---

## STYLE & WRITING GUIDELINES

| Element | File | Status | Confidence | Notes |
|---------|------|---------|------------|--------|
| Style Analysis | `style/` (Take A Stand + Out of Woods) | APPROVED | HIGH | Complete reference analysis |
| Style Specification | `style/style_specification.md` | APPROVED | HIGH | LLM writing rules |
| Character Design Patterns | `style/character_design_patterns.md` | APPROVED | HIGH | Character archetypes |
| Social Dynamics Guide | `style/social_dynamics_guide.md` | APPROVED | HIGH | Social norms |

---

## LOCATIONS & WORLDBUILDING

| Element | File | Status | Confidence | Dependencies |
|---------|------|---------|------------|--------------|
| Rainforest District | `locations/rainforest_district.md` | APPROVED (expandable) | HIGH | Used in M1.0, M1.3, M2.6 |
| Port Docks | `locations/port_docks.md` | APPROVED (expandable) | HIGH | Used in M1.6 (Fake Death) |
| ZPD Headquarters | `locations/zpd_precinct1.md` | APPROVED (expandable) | HIGH | Used throughout |
| Sahara Square | `locations/sahara_square.md` | APPROVED (expandable) | HIGH | Potential Act II/III use |
| Tundratown | `locations/tundratown.md` | APPROVED (expandable) | HIGH | Used in M2.3 (Heist) |

---

## ORGANIZATIONS & INSTITUTIONS

| Element | File | Status | Confidence | Dependencies |
|---------|------|---------|------------|--------------|
| **ZPD - Hierarchy** | `organizations/zpd.md` | APPROVED | HIGH | Includes Buck Antler, Delgato |
| **ZPD - Strike Force** | `organizations/zpd.md` | APPROVED | HIGH | Final team: Wolford, Fangmeyer, McHorn, Leni, Clawhauser |
| **ZPD - Procedures** | `organizations/zpd.md` | APPROVED | MEDIUM | - |
| **ZIA - Structure v2** | `organizations/zia_v2.md` | APPROVED | HIGH | Moss confirmed as mole |
| **Apex Society** | `organizations/apex_society.md` | APPROVED | HIGH | A.7 COMPLETE - Triad + Insiders |

---

## TECHNOLOGY FRAMEWORK

| Element | File | Status | Confidence | Dependencies |
|---------|------|---------|------------|--------------|
| Tech Level Specification | `technology/tech_specification.md` | DRAFT | MEDIUM | Awaits review |
| Canon Tech Baseline | tech_spec (Part I) | APPROVED | HIGH | Based on films |
| **Analog Chip** | `plot/story_plan.md` | APPROVED | HIGH | John Wilde's fail-safe, key McGuffin |

---

## CHARACTERS

| Element | Status | Priority | Notes |
|---------|---------|----------|-------|
| Nick Wilde | APPROVED | HIGH | Updated with John Wilde backstory, Apex infiltration arc |
| Judy Hopps | APPROVED | HIGH | Updated with full arc: hero → hunter → rogue → redeemed |
| Skye Winters | APPROVED | HIGH | Updated with Code Blue, motorcycle chase, Chip insertion |
| Jack Savage | APPROVED | HIGH | Updated with double game, Omega Files exposure |
| Marian Wilde | APPROVED | HIGH | Updated with Analog Communicator, awareness of mission |
| **Magnus Volt** | APPROVED | HIGH | Apex leader - Jaguar. In `organizations/apex_society.md` |
| **Ragnar** | APPROVED | HIGH | Apex enforcer - Komodo Dragon. Venom. In `apex_society.md` |
| **Vesper** | APPROVED | HIGH | Apex tech/assassin - Caracal. In `apex_society.md` |
| **Moss (Ghost)** | APPROVED | HIGH | ZIA mole - Moose. In `zia_v2.md` + `apex_society.md` |
| **Delgato** | APPROVED | HIGH | ZPD traitor - Lion. In `zpd.md` + `apex_society.md` |
| **Buck Antler** | APPROVED | HIGH | Corrupt commissioner - Deer. In `zpd.md` + `apex_society.md` |
| **Strike Force** | APPROVED | HIGH | Wolford, Fangmeyer, McHorn, Leni, Clawhauser. In `zpd.md` |

---

## PLOT STRUCTURE

| Element | Status | Priority | Notes |
|---------|---------|----------|-------|
| Master Story Plan | APPROVED | HIGH | 3 acts, 20 milestones. In `plot/story_plan.md` |
| Scene Breakdown | PLACEHOLDER | HIGH | Next phase: break milestones into individual scenes |
| Information Asymmetry Map | PLACEHOLDER | MEDIUM | Who knows what when |
| Chapter Mapping | PLACEHOLDER | MEDIUM | How scenes map to chapters |

---

## DEPENDENCIES MAP

```
Story Plan (APPROVED)
├── Blocks: Scene Breakdown
├── Blocks: Chapter Mapping
└── Blocks: Writing

Scene Breakdown
├── Depends on: Story Plan (done)
├── Depends on: All character profiles (done)
└── Blocks: Chapter Writing

Information Asymmetry Map
├── Depends on: Story Plan (done)
├── Depends on: Character profiles (done)
└── Enhances: Scene Breakdown quality
```

---

## NEXT STEPS

1. ~~**World Bible sync pass**~~ — DONE (Session 6)
2. **Scene-by-scene breakdown** of each milestone (Gemini 2.5 Pro)
3. **Information Asymmetry Map** - what reader/characters know at each point
4. **Chapter mapping** - how scenes group into chapters, pacing
5. **Begin writing** - chapter by chapter (Cursor/Claude)

---

## CHANGE LOG

**2026-02-14 - Initial Setup**
- World Bible phases I-II created
- Language standardization (all docs to English)

**2026-02-14 - Infrastructure**
- Git initialized, handoff protocol established
- Workflow: Cursor + Gemini 2.5 Pro

**2026-02-16 - MAJOR UPDATE: Story Plan Complete**
- Master story plan created (PROJECT APEX) with full 3-act structure
- A.7 COMPLETED: Apex Society (Magnus Volt, Ragnar Drakov, Vesper Nyx)
- Insiders defined: Moss/Ghost (mole), Delgato (traitor), Buck Antler (corrupt)
- Strike Force finalized: Wolford, Fangmeyer, McHorn, Leni, Clawhauser
- All character files updated with story plan details
- ZIA mole confirmed as Antford "Ghost" Moss (Moose)
- ZPD updated with Delgato, Antler, final Strike Force roster

**2026-02-17 - Session 6: World Bible Sync + Details**
- Full names: Ragnar Drakov (Komodo Dragon), Vesper Nyx (Caracal), Antford "Ghost" Moss (Moose)
- World Bible sync pass: 7 character/org files updated to match story plan
- Eyes motif added to style_specification.md (emerald/lavender)
- M2.1 Fangmeyer scene added (Bogo asks her to watch Judy)
- All milestone numbers corrected across files
- Recruitment backstory aligned across Nick, Skye, Jack profiles
- STATUS: World Bible SYNCED with story plan. Ready for scene breakdown

---

**INSTRUCTIONS FOR AGENTS:**
1. Always check this tracker before referencing world bible elements
2. Only build on APPROVED elements for new content
3. All documents must be written in English
4. The story plan in `plot/story_plan.md` is the master reference for plot
5. Update this tracker when status changes
6. Check dependencies before starting new work
