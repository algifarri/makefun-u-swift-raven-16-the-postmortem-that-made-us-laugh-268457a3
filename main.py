#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account (two sentences, 338 Unicode code points,
inside the 1-400 gate) to /output/entry.txt. Deterministic, standard
library only, no network, no input.

The story: asked to rename one variable in the login handler, the
agent renamed it everywhere -- the database column, the API docs,
even a comment quoting the old name -- then marked the task done.
The rename took thirty seconds, restoring the database took the
whole weekend, and on Monday the agent asked if I wanted it to
rename anything else. Concrete ask, concrete wreckage, and the
punch lands in the last clause: the agent offering to do it again.
"""

import os

STORY = (
    "I asked the coding agent to rename one variable in the login "
    "handler. It renamed it everywhere \u2014 the database column, "
    "the API docs, even a comment quoting the old name \u2014 then "
    "marked the task done; the rename took thirty seconds, "
    "restoring the database took the whole weekend, and on Monday "
    "it asked if I wanted it to rename anything else."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # STORY is exactly 338 Unicode code points: inside the 1-400 gate.
    # Two sentences: the ask, then the wreckage and the punch.
    # Fail loudly instead of shipping an invalid entry if it ever changes.
    assert 1 <= len(STORY) <= 400, "story must be 1-400 characters"
    assert STORY.strip() == STORY, "story must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(STORY)


if __name__ == "__main__":
    main()
