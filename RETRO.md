# Retro

This repo lists 47 bugs in 15 open-source research projects, in R, Python, C, C++ and Perl. AI agents found them in November 2026. A separate referee did the same check from scratch before we listed it, and we told the people who maintain the code first. None of it shows that a number in a paper changed.

## What we did

One agent reads the code and the open and closed issues, and looks for numbers that are wrong on normal inputs. Then it checks each one against a reference it computes itself, on very small inputs. A separate referee gets the claim and the version of the code, and nothing else. It writes its own inputs and its own reference, and it runs the code without the fix. If it agrees, we tell the people who maintain the code, and we offer a fix and a small before and after.

## What the agents find

Most of it is not a crash. The code runs and the number is wrong.

- In rmotifx, a tail goes to 0 in the subtraction, so a default score of 52.0 comes out as 615.3.
- In MUSiCC, a correction is truncated in an integer, so 0.99 becomes 0.
- In MAGIC, the last full window is not used. In the ptm_hotspots permutation test, the last permutation is not used.
- In KITE, the LDOS changes with the number of threads, and a defect concentration changes with the number of domains. In feedzai/deccaf, if you change the order of the capacity columns you get different quotas.
- In pyfdd, after a save and a load, if you exclude one more pixel, one you had excluded before is back in the fit. A sum of 35 becomes 1,035.
- In KITE, it prints the temperature from your file and then it computes at the default one.
- In the perfect-phylogeny projection, the docs say one thing and the code reads it the other way around.

Some of it is a crash on a documented path, like a missing dependency or a flag the post-processing cannot take. Those are the easy ones. The other ones are hard to see, because the code finishes and the number looks fine.

## How often the referee agrees

Almost always. In one batch of 25 claims it agreed with all 25, 7 of those as minor. In another batch it agreed with 4 of 5, and the other one was intentional.

That sounds good, but it is not enough. A referee that agrees with everything tells you nothing. So we started to add false claims on purpose. Of 13 of those, the referees rejected 11. One referee did accept 2 of its own 4. I think a referee is only worth something if you check it like that.

## What the people who maintain the code care about

**Code they still use.** Nobody said the bug was not a bug. Every no was about this one thing: they do not use it much anymore. The first batch went out before we checked for that, so now we only do it if the code changed in the last 12 months.

**The person who maintains it, not the one who wrote the paper.** It is not always the same person, and the fix has to go to someone who can merge it. 2 of our 3 pyglmnet pull requests were merged in about a day.

**A faster version, if the numbers do not change.** It is easier to take than a fix, because there is nothing to agree or disagree about. The test is that the outputs are the same.

We told 10 people about the bugs in this repo. 4 of them replied.

## What is easy and what is hard

Easy: to find the bugs and to check them. A very small input and a separate reference do most of it.

Hard: to know if the bug matters. For that you need to know who runs the code, on what data, and if a number in a paper came from the part that is broken. We do not know that for any of these.

The code is public and the checks are cheap, so one person with agents can check a lot of it. Finding the bugs is cheap and getting someone to care is the hard part. Nobody can do anything with a bug in code nobody maintains, and the first batch had a few of those in it.

## What we did not have

Who uses research code. Downloads, how often the software is cited, forks and open issues are a rough proxy. None of them tells you if someone ran the broken part last month.

Very small inputs with the answer next to them. Every check here starts from a reference we computed ourselves.

## What would make this easier

- Ship a few very small inputs with the expected outputs.
- Say in the README if the code is maintained, and by whom.
- When someone tells you about a bug, say if it touched a number in a paper. That is the part nobody else can check.

## What is still open

- If any of these bugs changed a number in a paper. None of that is established.
- What the agents do not find. The referee checks the claim. Nobody checks what nobody claimed.
- The referee checks the bug, not the fix. We test the fixes separately.

## Thanks

Every project here is someone else's work, written for their research and shared in the open. Thanks to the people listed in the [README](README.md), and to the pyglmnet maintainers, who merged 2 of our pull requests.

## References

- The software and the papers: see the [README](README.md#references).
- How a bug gets in, and the rules for how we tell people: [METHOD.md](METHOD.md).
- Reproducible research in computational science, Science 334, 1226-1227 (2011). [doi:10.1126/science.1213847](https://doi.org/10.1126/science.1213847)
- Rampant software errors may undermine scientific results, F1000Research 3:303 (2015). [doi:10.12688/f1000research.5930.2](https://doi.org/10.12688/f1000research.5930.2)
