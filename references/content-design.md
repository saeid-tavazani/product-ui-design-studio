# Content Design and Interface Writing

Interface words are functional design material.

## Standards

Every string should be:

- purposeful
- concise
- conversational for the product's audience
- clear before clever
- consistent with the product vocabulary

## Vocabulary system

Create a small vocabulary table for key objects, actions, roles, statuses, and forbidden synonyms. Use the same term through labels, buttons, dialogs, toasts, and documentation.

Example: `Publish` → confirmation asks about publishing → result says `Published`.

## Control labels

- start actions with specific verbs
- describe the immediate result
- avoid implementation language
- distinguish `Save changes`, `Save draft`, and `Publish`
- avoid generic `Submit`, `OK`, `Yes`, and `No` when a precise action fits

## Error anatomy

A recoverable error should state:

1. what happened
2. why, when known and useful
3. what the user can do next
4. whether their data was preserved

Do not apologize, blame the user, expose internal codes without explanation, or use `Something went wrong` as the entire message.

## Empty and loading states

- empty states explain what belongs here and provide the next useful action
- loading labels describe the object or action when waiting may be noticeable
- permission states explain the boundary and the available path
- offline states distinguish unavailable network work from locally preserved work

## Onboarding

Teach the minimum needed for the current step. Prefer contextual guidance, examples, and progressive disclosure over long introductory tours.

## Localization stress test

- test essential layouts with longer strings
- test mixed RTL/LTR values, numerals, dates, currency, phone numbers, URLs, and code
- avoid text baked into images
- do not concatenate translated fragments
- allow labels and buttons to wrap or grow without clipping
- verify icon directionality and culturally dependent metaphors
