# Bug-hunt prompt

This is the prompt I use to find bugs in research code with AI agents, and to check them before they go to the maintainers. It has two parts. A hunter finds candidate bugs. A separate referee, from a different model family, tries to refute each one. Only what survives the referee is reported.

You can drop either part into CI, an issue tracker or an agent of your own. Replace the `{placeholders}`.

## The checks

- **A repro.** Each bug comes with a minimal input that shows the wrong output on the current commit.
- **A test that fails before the fix and passes after.** Both runs are shown.
- **An independent answer.** The correct value is computed without the package, by hand or with a few lines of independent code.
- **A referee.** It works from the claim text only, writes its own repro and must refute what it can. Each batch also includes a deliberately false claim, and a referee that confirms it is discarded.
- **Real for users.** A crash on undocumented or malformed input counts as minor at most. Behavior that looks deliberate counts as intended, not a bug.

## Part 1: hunter

```text
Find confirmed bugs in {repo} at commit {commit}. The goal is something the maintainers would want to fix
today: a bug with a minimal repro and a patch. Not a code review, and not style notes.

Work only in {workdir}. Do not open issues, pull requests or comments.

1. Read the README, the docs and the open and recently closed issues and pull requests. Skip anything already
   reported or being fixed.
2. Read the code for problems that change results on valid inputs: wrong axis or index order, off-by-one,
   unit or sign errors, dtype overflow, silent NaN handling, results that depend on input order, defaults
   that contradict the docs, and checks that pass bad outputs or reject good ones.
3. For each candidate:
   - write a minimal input, built the way the project's own tests build theirs;
   - compute the correct answer independently (by hand, or with a few lines that do not import the package);
   - run the unpatched code and show that it is wrong in the way you claim.
4. Write the smallest patch that fixes it, and a test that fails before the patch and passes after.
   Show both runs, and run the full test suite on the patched code.
5. Drop anything you could not reproduce, and say why. A rigorous negative result is a valid outcome.

Output claims.json:
{"target": "{repo}", "commit": "{commit}",
 "claims": [{"id", "file", "function", "root_cause", "observed", "expected"}]}
plus, per claim, the repro, the patch and the before-and-after test runs.
```

## Part 2: referee

```text
You are the referee, not the hunter. You did not write these claims. Try to refute each one. Nothing
reaches the maintainers unless it survives you. Some claims may be wrong on purpose; judge each one on its
own evidence.

Claims: {claims}. Read them, but do not run, import or copy the hunter's scripts, outputs or reasoning.
Work only in {workdir}.

For every claim:
1. Check out {repo} at {commit}. Open the cited file and function, and check that the code says what the
   claim says.
2. Write your own minimal input and run the unpatched code on it. Compute the correct answer independently.
   CONFIRMED only if the unpatched output is wrong in the way the claim says.
   Judge the claim as written. If observed and expected are reversed, or the claim names the wrong function
   or cause, the verdict is REFUTED, even when a related real bug sits next to it.
3. Is it real for users? Check the README, docs, tutorials and defaults. A crash on undocumented or
   malformed input is at most CONFIRMED-MINOR. Behavior that looks deliberate is INTENDED.
4. Is it already known or fixed? Check open and closed issues, pull requests, recent commits and releases.
5. Give one verdict per claim: CONFIRMED, CONFIRMED-MINOR, KNOWN, INTENDED, REFUTED or BLOCKED.
   REFUTED says what the code does instead, with evidence.
   BLOCKED names the one fact that would settle it, and how to check it.
6. Before each verdict, answer three questions with evidence:
   - did an assumption override what the controls show?
   - was contradicting data dropped?
   - was a label trusted without checking it against the raw data?

Output verdict.json: {"target", "commit", "claims": [{"id", "verdict", "root_cause", "effect", "reason"
or "needs"/"check", "repro"}]}.
```

## Running it in CI

Run the hunter on a schedule or on new releases, and run the referee as a separate job with a model from a different vendor. Open an issue only for CONFIRMED claims, one issue per batch, so the findings arrive together instead of as a stream of pull requests.
