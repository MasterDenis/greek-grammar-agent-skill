# Sample Prompts for greek-grammar-agent-skill

Use these prompts to test whether Hermes activates the skill correctly and follows the intended response format.

## Correction

```text
/greek-grammar-agent-skill Correct this Greek sentence and explain the mistakes: Με ο φίλος μου πήγαμε σινεμά και μετά βλέπω μια ταινία.
```

Expected behavior:
- Gives corrected Greek first.
- Explains accusative after **με**.
- Explains verb tense/aspect issue if context requires past: **είδαμε** or **είδα**.

## Tonos

```text
Why does που sometimes become πού in Greek?
```

Expected behavior:
- Explains **πού** as question word and **που** as relative/complementizer.
- Gives direct and indirect question examples.

## Aspect

```text
Explain the difference between να γράφω and να γράψω with examples.
```

Expected behavior:
- Explains imperfective vs perfective aspect.
- Gives habitual/ongoing vs bounded/completed examples.

## Exercises

```text
Create 10 A2 Greek exercises about articles and accusative after prepositions, with answer key.
```

Expected behavior:
- Creates level-appropriate exercises.
- Provides answer key and short reasons.

## Register

```text
Make this more natural for a casual message: Θα ήθελα να σας ενημερώσω ότι δεν δύναμαι να παρευρεθώ.
```

Expected behavior:
- Provides a casual version.
- Explains formal-to-informal register changes.
