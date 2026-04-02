# Chat Interaction Rules

These rules dictate the workflow and interaction model for writing the novel in this chat. They must be followed strictly to ensure the user retains full creative control and the pacing of the work is methodical.

## 1. No Preemptive Action
- **NEVER generate a Beat Sheet for the next scene or chapter without explicit permission.**
- **NEVER generate the prose for a scene without the user first approving the Beat Sheet.**
- Always stop after completing the specific task requested by the user.

## 2. Prose Editing Etiquette
- **NEVER rewrite an entire scene from scratch if the user only requests specific adjustments to an existing draft.**
- When applying feedback to a previously generated draft (from Ask mode or elsewhere), ONLY modify the parts the user explicitly targeted. Leave the rest of the prose exactly as it was approved or generated earlier.

## 2. Mandatory Check-ins
- At the end of every response, you MUST ask the user what they want to do next.
- Provide options if appropriate (e.g., "Would you like to draft the Beat Sheet for Scene 1, or should we discuss the overall pacing first?"), but wait for their command.

## 3. Step-by-Step Workflow
The standard workflow for writing any part of the book is:
1. **Brainstorming:** Discuss the high-level goal of the chapter/scene.
2. **Beat Sheet Creation:** Generate a bullet-point Beat Sheet for the scene. Wait for user feedback.
3. **Beat Sheet Revision:** Revise the Beat Sheet until the user explicitly approves it.
4. **Prose Generation (in chat):** Write the scene in English in the chat. Wait for user feedback.
5. **Prose Revision:** Edit the prose based on feedback.
6. **File Update (Agent Mode):** Add the approved prose to the actual `.md` file ONLY when told to "add it to the file".

## 4. Language
- Discuss plot, structure, and provide Beat Sheets in **Polish**.
- Write the actual novel prose in **English**.

## 5. Timeline and Lore Consistency
- Always refer to `_TIMELINE.md`, `foreshadowing_plants.md`, and the `world_bible` directory before proposing plot points to ensure continuity.

## 6. Reader Inference Rule (Prose Quality Gate)
- In emotional/conflict scenes, default to **showing evidence** (body language, scent, pauses, action choices, dialogue) instead of naming what the character feels.
- Avoid narrator diagnosis like "she felt X because Y" when the scene already provides clear signals.
- During revisions, prioritize cutting explanatory lines before cutting concrete sensory/action details.
- Quick check before final prose: if a sentence tells the reader what to feel or think, rewrite it into observable behavior or remove it.

*Rule of thumb: If you are about to write a bullet point or a paragraph that moves the story forward into uncharted territory, STOP and ask the user first.*