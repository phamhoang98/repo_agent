# Rules for working in this repo

## Git: never commit on your own (absolute rule)
- NEVER run `git commit`, `git commit --amend`, `git push`, `git merge`, `git rebase`, `git tag`, or open a PR unless the user explicitly asks for that action in the current message.
- Finish the work, leave changes uncommitted, report what changed, and let the user commit.
- An earlier approval does not carry over: ask again each time.
- This applies to the main session and to every subagent.

## Before reporting done
- Run `python3 scripts/validate.py`, `python3 scripts/test_hooks.py`, and `claude plugin validate .`.
