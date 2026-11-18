![Research software bug hunt](assets/banner.png)

# research-software-bug-hunt: the full record

AI agents look for correctness bugs in open-source research software. A separate referee rebuilds each claim from scratch. Only bugs the referee confirms are listed here. Each bug was reported to the authors before it appears here.

| Project | Language | Pinned version or commit | Bugs confirmed | Minor | Status |
|---|---|---|---:|---:|---|
| [omarwagih/rmotifx](https://github.com/omarwagih/rmotifx) ([report](omarwagih-rmotifx/README.md)) | R | `f13775f07679b86df173ccc2a9112263a1a9052f` | 1 | 0 | reported to the authors, Nov 2026 |
| [evocellnet/funscoR](https://github.com/evocellnet/funscoR) ([report](evocellnet-funscoR/README.md)) | R | `1ed6c74f112fd381626295245da327453d70cbe2` | 1 | 0 | reported to the authors, Nov 2026 |
| [evocellnet/ksea](https://github.com/evocellnet/ksea) ([report](evocellnet-ksea/README.md)) | R | `126a64541a11df9d8dc16a00cd9ea3ab9f16147f` | 2 | 0 | reported to the authors, Nov 2026 |
| [evocellnet/ptm_hotspots](https://github.com/evocellnet/ptm_hotspots) ([report](evocellnet-ptm_hotspots/README.md)) | Python | `15b4b256f7f2945eebe72f622d68115d4bdd5e70` | 1 | 1 | reported to the authors, Nov 2026 |
| [bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model) ([report](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/README.md)) | C | `769ccd389a559085df8fa628047eba2f2d850c15` | 2 | 0 | reported to the authors, Nov 2026 |
| [edbosne/pyfdd](https://github.com/edbosne/pyfdd) ([report](edbosne-pyfdd/README.md)) | Python | `6aba44c5c4aaed278e08691f28abe79c724cf1da` | 7 | 3 | reported to the authors, Nov 2026 |
| [borenstein-lab/MUSiCC](https://github.com/borenstein-lab/MUSiCC) ([report](borenstein-lab-MUSiCC/README.md)) | Python | `478c9244cf406935e67abdf7622bdb05421ab1fb` | 1 | 0 | reported to the authors, Nov 2026 |
| [borenstein-lab/mimosa2](https://github.com/borenstein-lab/mimosa2) ([report](borenstein-lab-mimosa2/README.md)) | R | `581b307dee48577117ac42599a07b33a51b0822d` | 2 | 1 | reported to the authors, Nov 2026 |
| [borenstein-lab/MAAMOUL](https://github.com/borenstein-lab/MAAMOUL) ([report](borenstein-lab-MAAMOUL/README.md)) | R | `54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9` | 1 | 0 | reported to the authors, Nov 2026 |
| [glarue/intronIC](https://github.com/glarue/intronIC) ([report](glarue-intronIC/README.md)) | Python | `0db1d54274f1ffdbbc95dea6589a75a833eb831d` | 5 | 1 | reported to the authors, Nov 2026 |
| [feedzai/deccaf](https://github.com/feedzai/deccaf) ([report](feedzai-deccaf/README.md)) | Python | `b910b48d7e146d53b5f145224b819bdb0962d40a` | 3 | 2 | reported to the authors, Nov 2026 |
| [weissmanlab/magic](https://github.com/weissmanlab/magic) ([report](weissmanlab-magic/README.md)) | Python | `87fd0923480d28399c5078ff4efd60c3205c22a0` | 4 | 0 | reported to the authors, Nov 2026 |
| [GO::TermFinder](https://metacpan.org/release/SHERLOCK/GO-TermFinder-0.86) ([report](cpan-GO-TermFinder/README.md)) | Perl | `0.86` | 6 | 2 | reported to the authors, Nov 2026 |
| [glm-tools/pyglmnet](https://github.com/glm-tools/pyglmnet) ([report](glm-tools-pyglmnet/README.md)) | Python | `9339c5c71c908ec31cf4bebda5d9fe47dfed4f1c` | 3 | 0 | [#399](https://github.com/glm-tools/pyglmnet/pull/399) merged, [#400](https://github.com/glm-tools/pyglmnet/pull/400) open, [#401](https://github.com/glm-tools/pyglmnet/pull/401) merged |

Minor defects are included in the confirmed counts. Reports preserve the limits of each finding; they do not establish changes to published scientific results.

## How a bug gets in

The full rules, and the numbers so far, are in [METHOD.md](METHOD.md). The retro is [RETRO.md](RETRO.md).

1. Hunt for a correctness bug in a pinned upstream version.
2. An independent referee rebuilds the claim from scratch.
3. Prepare a patch and a small before/after example.
4. Check normal inputs and record the limits of the fix.

## Hunt, then an independent referee

_Source: [METHOD.md](METHOD.md)_

1. An AI agent clones a pinned commit, reads the open and closed issues and PRs first, and looks for correctness bugs: numbers that are wrong on normal inputs. It checks each number against a reference it computes separately, using tiny inputs on a CPU.
2. A separate referee gets only the claim and the pinned commit. It does not run or read the hunter's scripts, patches or expected outputs. It writes its own minimal input and its own reference, runs the unpatched code, and gives a verdict: CONFIRMED, CONFIRMED-MINOR, INTENDED, NOT REPRODUCED or KNOWN.
3. Only CONFIRMED and CONFIRMED-MINOR bugs get reported. KNOWN means someone had already reported it, so we drop it.
4. Some authors get a second, independent referee on every bug and a separate read of the exact email text before it goes.

This file puts every bug report in one place, for readers and reviewers who want it in a single document. Each section below is copied word for word from the project's own folder in this repository: the bugs and their fixes, how to run each reproduction, and its before/after output.

---

# glm-tools/pyglmnet

Folder: [glm-tools-pyglmnet](glm-tools-pyglmnet)

Upstream pull requests, state on GitHub on November 18, 2026:

| PR | State |
| --- | --- |
| [glm-tools/pyglmnet#399](https://github.com/glm-tools/pyglmnet/pull/399) | merged 2026-11-08 |
| [glm-tools/pyglmnet#401](https://github.com/glm-tools/pyglmnet/pull/401) | merged 2026-11-08 |
| [glm-tools/pyglmnet#400](https://github.com/glm-tools/pyglmnet/pull/400) | open |

A separate referee's [verdicts](https://github.com/rpinho/ai-biology/blob/main/friends/hugo-fernandes-pyglmnet/referee/VERDICTS.md).

## Report

_Source: [glm-tools-pyglmnet/README.md](glm-tools-pyglmnet/README.md)_

## glm-tools/pyglmnet

Three confirmed defects, reported through the pull requests below in Nov 2026. #399 and #401 were merged on Nov 8; #400 is open. Patches and tests live in the pull requests.

Upstream base commit: [`9339c5c71c908ec31cf4bebda5d9fe47dfed4f1c`](https://github.com/glm-tools/pyglmnet/tree/9339c5c71c908ec31cf4bebda5d9fe47dfed4f1c).

- [#399: FIX: Bernoulli log likelihood is NaN at probabilities 0 and 1, and overflows for large logits](https://github.com/glm-tools/pyglmnet/pull/399). Uses stable Bernoulli likelihood expressions at probability endpoints and large logits.
- [#400: FIX: gamma deviance and pseudo-R2 omit the saturated log likelihood](https://github.com/glm-tools/pyglmnet/pull/400). Includes the gamma saturated log likelihood in deviance and pseudo-R2.
- [#401: FIX: simulate_glm(sample=True) for gamma returns exp(mu) instead of gamma samples](https://github.com/glm-tools/pyglmnet/pull/401). Draws gamma samples with the requested mean instead of returning exp(mu).

### References

- [Jas et al. (2020). Pyglmnet: Python implementation of elastic-net regularized generalized linear models.](https://doi.org/10.21105/joss.01959)
- [Upstream repository](https://github.com/glm-tools/pyglmnet).

---

# omarwagih/rmotifx

Folder: [omarwagih-rmotifx](omarwagih-rmotifx)

## Report

_Source: [omarwagih-rmotifx/README.md](omarwagih-rmotifx/README.md)_

## omarwagih/rmotifx

Pinned commit: [`f13775f07679b86df173ccc2a9112263a1a9052f`](https://github.com/omarwagih/rmotifx/tree/f13775f07679b86df173ccc2a9112263a1a9052f).

1 confirmed defect, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### PB005 : Upper-tail cancellation

[omarwagih/rmotifx · R/motifx-functions.R:96](https://github.com/omarwagih/rmotifx/blob/f13775f07679b86df173ccc2a9112263a1a9052f/R/motifx-functions.R#L96). Twenty `ASA` strings against the 400 strings `aSb` over 20 letters: default score **615.305311 → 52.041200**. Subtraction rounds representable binomial tails to zero, inflating reported motif scores. Correct: two tails `(1/20)^20`, summed as −log10 probabilities ([score definition](https://github.com/omarwagih/rmotifx/blob/f13775f07679b86df173ccc2a9112263a1a9052f/man/motifx.Rd)). Explicit Perl compatibility is preserved. [Repro](omarwagih-rmotifx/repro/PB005/run.sh), [patch](omarwagih-rmotifx/patches/PB005.patch).

### References

- [Wagih et al. (2016). Uncovering phosphorylation-based specificities through functional interaction networks.](https://doi.org/10.1074/mcp.M115.052357)
- [Upstream source at the reported commit](https://github.com/omarwagih/rmotifx/tree/f13775f07679b86df173ccc2a9112263a1a9052f).

## Reproduction: PB005

_Source: [omarwagih-rmotifx/repro/PB005/README.md](omarwagih-rmotifx/repro/PB005/README.md)_

Run `sh repro/PB005/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/PB005.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. For PB003: `python -m pip install numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 statsmodels`. For the R cases: R 4.5.2, with `install.packages(c("caret","gbm","e1071","pROC","doParallel","foreach","dplyr","tibble","tidyr","stringr"))`; the reproduction installs the pinned target package into temporary libraries. Pass `--rscript PATH` if Rscript is outside PATH.

### References

- [Wagih et al. (2016). Uncovering phosphorylation-based specificities through functional interaction networks.](https://doi.org/10.1074/mcp.M115.052357)
- [Upstream source at the reported commit](https://github.com/omarwagih/rmotifx/tree/f13775f07679b86df173ccc2a9112263a1a9052f).

## Before and after: PB005

_Source: [omarwagih-rmotifx/repro/PB005/RESULTS.txt](omarwagih-rmotifx/repro/PB005/RESULTS.txt)_

```text
Exact one-position tail: (1/20)**20 = 9.5367431640625e-27
Default score before=615.305311137178; correct=after=52.0411998265592
The entire normal output (representable tail) and requested Perl compatibility output are unchanged.
```

---

# evocellnet/funscoR

Folder: [evocellnet-funscoR](evocellnet-funscoR)

## Report

_Source: [evocellnet-funscoR/README.md](evocellnet-funscoR/README.md)_

## evocellnet/funscoR

Pinned commit: [`1ed6c74f112fd381626295245da327453d70cbe2`](https://github.com/evocellnet/funscoR/tree/1ed6c74f112fd381626295245da327453d70cbe2).

1 confirmed defect, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### PB004 : Custom parameters crash

[evocellnet/funscoR · R/predict_score.R:58](https://github.com/evocellnet/funscoR/blob/1ed6c74f112fd381626295245da327453d70cbe2/R/predict_score.R#L58). 120 synthetic rows, one repetition, three folds and two trees: **undefined `param` → 3 fitted two-tree models**. Non-NULL `parameters` never initializes `param`, blocking customization. Correct: the supplied settings must be used ([documented interface](https://github.com/evocellnet/funscoR/blob/1ed6c74f112fd381626295245da327453d70cbe2/man/train_funscore.Rd)). [Repro](evocellnet-funscoR/repro/PB004/run.sh), [patch](evocellnet-funscoR/patches/PB004.patch).

```diff
+    param <- parameters
```

### References

- [Ochoa et al. (2020). The functional landscape of the human phosphoproteome.](https://doi.org/10.1038/s41587-019-0344-3)
- [Upstream source at the reported commit](https://github.com/evocellnet/funscoR/tree/1ed6c74f112fd381626295245da327453d70cbe2).

## Reproduction: PB004

_Source: [evocellnet-funscoR/repro/PB004/README.md](evocellnet-funscoR/repro/PB004/README.md)_

Run `sh repro/PB004/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/PB004.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. For PB003: `python -m pip install numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 statsmodels`. For the R cases: R 4.5.2, with `install.packages(c("caret","gbm","e1071","pROC","doParallel","foreach","dplyr","tibble","tidyr","stringr"))`; the reproduction installs the pinned target package into temporary libraries. Pass `--rscript PATH` if Rscript is outside PATH.

### References

- [Ochoa et al. (2020). The functional landscape of the human phosphoproteome.](https://doi.org/10.1038/s41587-019-0344-3)
- [Upstream source at the reported commit](https://github.com/evocellnet/funscoR/tree/1ed6c74f112fd381626295245da327453d70cbe2).

## Before and after: PB004

_Source: [evocellnet-funscoR/repro/PB004/RESULTS.txt](evocellnet-funscoR/repro/PB004/RESULTS.txt)_

```text
Documented contract: supplied parameters determine the fit; custom run must not look up an undefined variable.
Before: object param not found. After: requested 1 repetition, 3 folds, 2 trees each.
Default normal fit: all 15 fitted ensembles and folds byte-identical, excluding runtime metadata.
```

---

# evocellnet/ksea

Folder: [evocellnet-ksea](evocellnet-ksea)

## Report

_Source: [evocellnet-ksea/README.md](evocellnet-ksea/README.md)_

## evocellnet/ksea

Pinned commit: [`126a64541a11df9d8dc16a00cd9ea3ab9f16147f`](https://github.com/evocellnet/ksea/tree/126a64541a11df9d8dc16a00cd9ea3ab9f16147f).

2 confirmed defects, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### PB002 : Null distribution ignores power

[evocellnet/ksea · R/ksea.R:120](https://github.com/evocellnet/ksea/blob/126a64541a11df9d8dc16a00cd9ea3ab9f16147f/R/ksea.R#L120). Ranks A–F, values 6–1, signature A/D, `p=2`, seed 3, 1,000 matched draws: empirical significance **0.154 → 0.277**, observed ES 0.8 unchanged. Null scores use default `p=1`, distorting non-default inference. Correct: apply the same weighted statistic to observed and permuted sets ([definition](https://github.com/evocellnet/ksea/blob/126a64541a11df9d8dc16a00cd9ea3ab9f16147f/man/ksea.Rd)). [Repro](evocellnet-ksea/repro/PB002/run.sh), [patch](evocellnet-ksea/patches/PB002.patch).
#### PB001 : Classic enrichment counts nonmembers

[evocellnet/ksea · R/ksea.R:56](https://github.com/evocellnet/ksea/blob/126a64541a11df9d8dc16a00cd9ea3ab9f16147f/R/ksea.R#L56). Ranks A–F, values 6–1, signature A/D, `p=0`: ES **1/6 → 1/2**. `0^0` counts misses as hits, corrupting classic enrichment. Correct: the walk adds 1/2 only at members and subtracts 1/4 at misses ([running-sum definition](https://github.com/evocellnet/ksea/blob/126a64541a11df9d8dc16a00cd9ea3ab9f16147f/R/ksea.R#L53)). Classic significance also needs PB002. [Repro](evocellnet-ksea/repro/PB001/run.sh), [patch](evocellnet-ksea/patches/PB001.patch).

```diff
-  hitCases <- cumsum(abs(R) ^ p)
+  hitCases <- cumsum((abs(norm_express) ^ p) * HITS)
```

### References

- [Ochoa et al. (2016). An atlas of human kinase regulation.](https://doi.org/10.15252/msb.20167295)
- [Upstream source at the reported commit](https://github.com/evocellnet/ksea/tree/126a64541a11df9d8dc16a00cd9ea3ab9f16147f).

## Reproduction: PB001

_Source: [evocellnet-ksea/repro/PB001/README.md](evocellnet-ksea/repro/PB001/README.md)_

Run `sh repro/PB001/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/PB001.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. For PB003: `python -m pip install numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 statsmodels`. For the R cases: R 4.5.2, with `install.packages(c("caret","gbm","e1071","pROC","doParallel","foreach","dplyr","tibble","tidyr","stringr"))`; the reproduction installs the pinned target package into temporary libraries. Pass `--rscript PATH` if Rscript is outside PATH.

### References

- [Ochoa et al. (2016). An atlas of human kinase regulation.](https://doi.org/10.15252/msb.20167295)
- [Upstream source at the reported commit](https://github.com/evocellnet/ksea/tree/126a64541a11df9d8dc16a00cd9ea3ab9f16147f).

## Before and after: PB001

_Source: [evocellnet-ksea/repro/PB001/RESULTS.txt](evocellnet-ksea/repro/PB001/RESULTS.txt)_

```text
Independent exact walk: ['1/2', '1/4', '0', '1/2', '1/4', '0']
Classic ES: before=0.166666666666667, correct=after=0.5
Default p=1 normal ES and complete running sum unchanged.
```

## Reproduction: PB002

_Source: [evocellnet-ksea/repro/PB002/README.md](evocellnet-ksea/repro/PB002/README.md)_

Run `sh repro/PB002/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/PB002.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. For PB003: `python -m pip install numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 statsmodels`. For the R cases: R 4.5.2, with `install.packages(c("caret","gbm","e1071","pROC","doParallel","foreach","dplyr","tibble","tidyr","stringr"))`; the reproduction installs the pinned target package into temporary libraries. Pass `--rscript PATH` if Rscript is outside PATH.

### References

- [Ochoa et al. (2016). An atlas of human kinase regulation.](https://doi.org/10.15252/msb.20167295)
- [Upstream source at the reported commit](https://github.com/evocellnet/ksea/tree/126a64541a11df9d8dc16a00cd9ea3ab9f16147f).

## Before and after: PB002

_Source: [evocellnet-ksea/repro/PB002/RESULTS.txt](evocellnet-ksea/repro/PB002/RESULTS.txt)_

```text
Requested power=2 observed ES=0.8; 1000 fixed draws
p-value: before=0.154, correct=after=0.277; wrong p=1 null=0.154
Default p=1 ES and p-value unchanged; both independently recomputed.
```

---

# evocellnet/ptm_hotspots

Folder: [evocellnet-ptm_hotspots](evocellnet-ptm_hotspots)

## Report

_Source: [evocellnet-ptm_hotspots/README.md](evocellnet-ptm_hotspots/README.md)_

## evocellnet/ptm_hotspots

Pinned commit: [`15b4b256f7f2945eebe72f622d68115d4bdd5e70`](https://github.com/evocellnet/ptm_hotspots/tree/15b4b256f7f2945eebe72f622d68115d4bdd5e70).

1 confirmed defect, including 1 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### PB003 : Last permutation omitted : minor

[evocellnet/ptm_hotspots · ptm_hotspots.py:203](https://github.com/evocellnet/ptm_hotspots/blob/15b4b256f7f2945eebe72f622d68115d4bdd5e70/ptm_hotspots.py#L203). Two nine-character strings, labels 3/4/5, seed 0: default raw p at the first reported position **0.005796981 → 0.005557604**. Three slices use 99/100 draws; two-draw runs give missing values. Correct: summarize all requested permutations ([CLI contract](https://github.com/evocellnet/ptm_hotspots/blob/15b4b256f7f2945eebe72f622d68115d4bdd5e70/README.md)); user p-values change, with no default classification change demonstrated. [Repro](evocellnet-ptm_hotspots/repro/PB003/run.sh), [patch](evocellnet-ptm_hotspots/patches/PB003.patch).

### References

- [Strumillo et al. (2018). Conserved phosphorylation hotspots in eukaryotic protein domain families (preprint).](https://doi.org/10.1101/391185)
- [Upstream source at the reported commit](https://github.com/evocellnet/ptm_hotspots/tree/15b4b256f7f2945eebe72f622d68115d4bdd5e70).

## Reproduction: PB003

_Source: [evocellnet-ptm_hotspots/repro/PB003/README.md](evocellnet-ptm_hotspots/repro/PB003/README.md)_

Run `sh repro/PB003/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/PB003.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. For PB003: `python -m pip install numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 statsmodels`. For the R cases: R 4.5.2, with `install.packages(c("caret","gbm","e1071","pROC","doParallel","foreach","dplyr","tibble","tidyr","stringr"))`; the reproduction installs the pinned target package into temporary libraries. Pass `--rscript PATH` if Rscript is outside PATH.

### References

- [Strumillo et al. (2018). Conserved phosphorylation hotspots in eukaryotic protein domain families (preprint).](https://doi.org/10.1101/391185)
- [Upstream source at the reported commit](https://github.com/evocellnet/ptm_hotspots/tree/15b4b256f7f2945eebe72f622d68115d4bdd5e70).

## Before and after: PB003

_Source: [evocellnet-ptm_hotspots/repro/PB003/RESULTS.txt](evocellnet-ptm_hotspots/repro/PB003/RESULTS.txt)_

```text
iter2 before p: [nan, nan, nan, nan, 1.0]
iter2 correct=after p: [0.00020347600872247995, 0.00020347600872247995, 0.01694742676234467, 0.01694742676234459, 1.0]
default100 before p: [0.005796980731822921, 0.008244901108369252, 0.0074565772108382755, 0.25676502311302907, 1.0]
default100 correct=after p: [0.005557604382004304, 0.007929386415875735, 0.007170165621883509, 0.2533905759753845, 1.0]
Independent seeded shuffles, sample SD, Gaussian survival and Bonferroni agree.
Normal dispersed nonempty PTMs and empty PTMs, default 100 permutations: all output unchanged.
```

---

# bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model

Folder: [bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model)

## Report

_Source: [bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/README.md](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/README.md)_

## bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model

Pinned commit: [`769ccd389a559085df8fa628047eba2f2d850c15`](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/tree/769ccd389a559085df8fa628047eba2f2d850c15).

2 confirmed defects, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### BENTO-001 : Column-major input misread

[bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model · project_onto_PPM.c:970](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/blob/769ccd389a559085df8fa628047eba2f2d850c15/project_onto_PPM.c#L970). Two-node tree, frequency columns `(1,¼),(1,¾)`, unit weights: equality cost **0.562501 → 0**; fractions become `(¾,¼),(¼,¾)` within 3e−6. Documented column-major tokens are treated as row-major, changing fractions and tree costs. Correct: these feasible fractions give `UM=F` and zero squared residual ([objective](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/blob/769ccd389a559085df8fa628047eba2f2d850c15/test_against_CVX_matlab.m)). Patch also updates the writer and example. Existing row-major multi-sample files need reserialization; MATLAB execution was unavailable. [Repro](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-001/run.sh), [patch](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/patches/BENTO-001.patch).
#### BENTO-002 : Absolute jitter breaks small weights

[bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model · project_onto_PPM.c:917](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/blob/769ccd389a559085df8fa628047eba2f2d850c15/project_onto_PPM.c#L917). Two-node tree, one column `(1,¼)`, both weights 0.0001: inequality fraction **−49.374222 → 0.250000** for the child; cost **0.000049 → 0**. Jitter added after `D²F` scaling can overwhelm data, yielding invalid fractions. Correct: `(¾,¼)` attains zero residual under the [weighted objective](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/blob/769ccd389a559085df8fa628047eba2f2d850c15/test_against_CVX_matlab.m). Scale jitter by `D²`; the existing approximate tie breaker remains, with no guarantee for extreme weight ratios. [Repro](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-002/run.sh), [patch](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/patches/BENTO-002.patch).

```diff
-        data[i] += x;
+        data[i] += x / gamma_init[i / T];
```

### References

- [Jia et al. (2018). Efficient Projection onto the Perfect Phylogeny Model.](https://doi.org/10.48550/arXiv.1811.01129)
- [Upstream source at the reported commit](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/tree/769ccd389a559085df8fa628047eba2f2d850c15).

## Reproduction: BENTO-001

_Source: [bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-001/README.md](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-001/README.md)_

Run `sh repro/BENTO-001/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/BENTO-001.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+ and a C compiler named `cc`. No Python packages are required. Numeric fractions have a 3e-6 tolerance because the retained upstream tie breaker perturbs frequencies by up to 1e-6.

### References

- [Jia et al. (2018). Efficient Projection onto the Perfect Phylogeny Model.](https://doi.org/10.48550/arXiv.1811.01129)
- [Upstream source at the reported commit](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/tree/769ccd389a559085df8fa628047eba2f2d850c15).

## Before and after: BENTO-001

_Source: [bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-001/RESULTS.txt](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-001/RESULTS.txt)_

```text
case: exact rational closed form agrees
before mode 0: 0.562501
0.000000 1.000000 0.250000 0.750000
before mode 1: 0.125000
0.000000 1.000000 0.000000 0.500000
after mode 0: 0.000000
0.749999 0.250001 0.250000 0.750000
after mode 1: 0.000000
0.749999 0.250001 0.249999 0.750000
```

## Reproduction: BENTO-002

_Source: [bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-002/README.md](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-002/README.md)_

Run `sh repro/BENTO-002/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/BENTO-002.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+ and a C compiler named `cc`. No Python packages are required. Numeric fractions have a 3e-6 tolerance because the retained upstream tie breaker perturbs frequencies by up to 1e-6.

### References

- [Jia et al. (2018). Efficient Projection onto the Perfect Phylogeny Model.](https://doi.org/10.48550/arXiv.1811.01129)
- [Upstream source at the reported commit](https://github.com/bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model/tree/769ccd389a559085df8fa628047eba2f2d850c15).

## Before and after: BENTO-002

_Source: [bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-002/RESULTS.txt](bentoayr-Efficient-Projection-onto-the-Perfect-Phylogeny-Model/repro/BENTO-002/RESULTS.txt)_

```text
case: exact rational closed form agrees
before mode 0: 0.000100
0.750000 0.250000
before mode 1: 0.000049
0.000000 -49.374222
after mode 0: 0.000000
0.750000 0.250000
after mode 1: 0.000000
0.749999 0.250000
```

---

# edbosne/pyfdd

Folder: [edbosne-pyfdd](edbosne-pyfdd)

## Report

_Source: [edbosne-pyfdd/README.md](edbosne-pyfdd/README.md)_

## edbosne/pyfdd

Pinned commit: [`6aba44c5c4aaed278e08691f28abe79c724cf1da`](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

7 confirmed defects, including 3 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### B01 : Angular grid distortion

[edbosne/pyfdd · pyfdd/core/patterncreator.py:388](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/patterncreator.py#L388). Library field `10+x+2y`, target coordinates −1,0,1: first row **[6.25,7.5,8.75] → [7,8,9]**; a flat 5×5 self-grid loses **16 → 0** pixels. Index scaling stretches coordinates, changing model shapes and support. Correct: index `(angle−first)/step` follows the [library grid definition](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/lib2dl/lib2dl.py#L109), retaining the existing interpolator. [Repro](edbosne-pyfdd/repro/B01/run.sh), [patch](edbosne-pyfdd/patches/B01.patch).
#### B02 : JSON reload discards backing masks

[edbosne/pyfdd · pyfdd/core/datapattern/datapattern.py:389](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/datapattern/datapattern.py#L389). 3×3 data with one excluded 1,000-count pixel; save, reload, exclude another: included sum **1,035 → 35**. Constructor resets restored backing masks, allowing excluded pixels back into fits. Correct: preserve exclusions serialized by the [JSON writer](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/datapattern/datapattern.py#L704). [Repro](edbosne-pyfdd/repro/B02/run.sh), [patch](edbosne-pyfdd/patches/B02.patch).
#### B03 : Orientation leaves masks behind

[edbosne/pyfdd · pyfdd/core/datapattern/datapattern.py:982](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/datapattern/datapattern.py#L982). Clockwise-rotate a masked 3×3 array, then edit its mask: included sum **1,029 → 36**; rectangular case **IndexError → 17**. Backing masks retain old coordinates, corrupting exclusions or crashing. Correct: transform exclusions with their pixels under the [documented orientation](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/datapattern/datapattern.py#L971). [Repro](edbosne-pyfdd/repro/B03/run.sh), [patch](edbosne-pyfdd/patches/B03.patch).
#### B04 : Background retains earlier exclusions

[edbosne/pyfdd · pyfdd/core/patterncreator.py:425](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/patterncreator.py#L425). Uniform 90-count 3×3 input: render, displace, render original again: **6 masked pixels plus 3×30 → 9×10**. In-place background mutation makes results depend on earlier calls. Correct: identical [requested parameters](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/patterncreator.py#L159) define identical patterns. This concerns default PatternCreator masking; Fit’s masking-false path is outside this finding. [Repro](edbosne-pyfdd/repro/B04/run.sh), [patch](edbosne-pyfdd/patches/B04.patch).
#### B06 : Zero-probability costs omitted : minor

[edbosne/pyfdd · pyfdd/core/fit.py:316](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/fit.py#L316). 7×7 library with a zero plateau, positive observed center: NLL **16.962108 → ∞**, Pearson cost **0.716049 → ∞**. Masked arithmetic drops impossible bins, favoring invalid models. Correct: `−n log(0)=∞` for `n>0` ([likelihood definition](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/fit.py#L381)). Exposure on ordinary positive library patterns is unestablished. [Repro](edbosne-pyfdd/repro/B06/run.sh), [patch](edbosne-pyfdd/patches/B06.patch).
#### B07 : Zero-minimum uncertainty collapse : minor

[edbosne/pyfdd · pyfdd/core/fit.py:368](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/fit.py#L368). Fit total counts to nine ten-count bins: optimum 90 unchanged; standard deviation **3e−10 → 9.486833**. A ratio cap against previous cost zero corrupts curvature, giving extreme overconfidence. Correct: `χ²(t)=(90−t)²/t` has `χ²″(90)=2/90`, giving √90 under the [implemented Hessian convention](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/fit.py#L588). Exact-fit scope only. [Repro](edbosne-pyfdd/repro/B07/run.sh), [patch](edbosne-pyfdd/patches/B07.patch).

```diff
-        elif chi2 > self.previous_cost_value * 1e12:
+        elif self.previous_cost_value > 0 and chi2 > self.previous_cost_value * 1e12:
```
#### B05 : Direct-input degrees of freedom : minor

[edbosne/pyfdd · pyfdd/core/fit.py:273](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/fit.py#L273). Nine bins, six active parameters: scalar-mask array **−5 → 3** degrees of freedom; ndarray **AttributeError → 3**. A scalar mask is counted as one bin and `np.Array` is misspelled, breaking direct Fit usage. Correct: count unmasked bins minus fitted parameters ([definition](https://github.com/edbosne/pyfdd/blob/6aba44c5c4aaed278e08691f28abe79c724cf1da/pyfdd/core/fit.py#L266)). Normal DataPattern masks avoid this. [Repro](edbosne-pyfdd/repro/B05/run.sh), [patch](edbosne-pyfdd/patches/B05.patch).

```diff
-            n_pixels = (~self.data_pattern.mask).sum()
-        elif isinstance(self.data_pattern, np.Array):
+            n_pixels = self.data_pattern.count()
+        elif isinstance(self.data_pattern, np.ndarray):
```

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Reproduction: B01

_Source: [edbosne-pyfdd/repro/B01/README.md](edbosne-pyfdd/repro/B01/README.md)_

Run `sh repro/B01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B01

_Source: [edbosne-pyfdd/repro/B01/RESULTS.txt](edbosne-pyfdd/repro/B01/RESULTS.txt)_

```text
before:
{
  "yield": [
    [
      6.25,
      7.5,
      8.75
    ],
    [
      8.75,
      10.0,
      11.25
    ],
    [
      11.25,
      12.5,
      13.75
    ]
  ],
  "masked_library_grid_pixels": 16,
  "normal": [
    [
      1.0,
      1.0,
      1.0
    ],
    [
      1.0,
      1.0,
      1.0
    ],
    [
      1.0,
      1.0,
      1.0
    ]
  ]
}
after:
{
  "yield": [
    [
      7.0,
      8.0,
      9.0
    ],
    [
      9.0,
      10.0,
      11.0
    ],
    [
      11.0,
      12.0,
      13.0
    ]
  ],
  "masked_library_grid_pixels": 0,
  "normal": [
    [
      1.0,
      1.0,
      1.0
    ],
    [
      1.0,
      1.0,
      1.0
    ],
    [
      1.0,
      1.0,
      1.0
    ]
  ]
}
```

## Reproduction: B02

_Source: [edbosne-pyfdd/repro/B02/README.md](edbosne-pyfdd/repro/B02/README.md)_

Run `sh repro/B02/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B02.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B02

_Source: [edbosne-pyfdd/repro/B02/RESULTS.txt](edbosne-pyfdd/repro/B02/RESULTS.txt)_

```text
before:
{
  "loaded_pixels_mask": [
    [
      false,
      false,
      false
    ],
    [
      false,
      false,
      false
    ],
    [
      false,
      false,
      false
    ]
  ],
  "edited_mask": [
    [
      false,
      false,
      false
    ],
    [
      false,
      false,
      false
    ],
    [
      false,
      false,
      true
    ]
  ],
  "edited_sum": 1035.0,
  "saved_again_sum": 1035.0,
  "normal": {
    "sum": 1035.0,
    "mask": [
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        true
      ]
    ]
  }
}
after:
{
  "loaded_pixels_mask": [
    [
      true,
      false,
      false
    ],
    [
      false,
      false,
      false
    ],
    [
      false,
      false,
      false
    ]
  ],
  "edited_mask": [
    [
      true,
      false,
      false
    ],
    [
      false,
      false,
      false
    ],
    [
      false,
      false,
      true
    ]
  ],
  "edited_sum": 35.0,
  "saved_again_sum": 35.0,
  "normal": {
    "sum": 1035.0,
    "mask": [
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        true
      ]
    ]
  }
}
```

## Reproduction: B03

_Source: [edbosne-pyfdd/repro/B03/README.md](edbosne-pyfdd/repro/B03/README.md)_

Run `sh repro/B03/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B03.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B03

_Source: [edbosne-pyfdd/repro/B03/RESULTS.txt](edbosne-pyfdd/repro/B03/RESULTS.txt)_

```text
before:
{
  "commands": {
    "cw": {
      "mask": [
        [
          true,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 1029.0
    },
    "cc": {
      "mask": [
        [
          true,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 1029.0
    },
    "mh": {
      "mask": [
        [
          true,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 1029.0
    },
    "mv": {
      "mask": [
        [
          true,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 1029.0
    },
    "cw,mh": {
      "mask": [
        [
          true,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 30.0
    }
  },
  "rectangular": {
    "error": "IndexError"
  },
  "normal": {
    "sum": 8.0,
    "mask": [
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        true
      ]
    ]
  }
}
after:
{
  "commands": {
    "cw": {
      "mask": [
        [
          false,
          false,
          true
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 36.0
    },
    "cc": {
      "mask": [
        [
          false,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          true,
          false,
          true
        ]
      ],
      "sum": 32.0
    },
    "mh": {
      "mask": [
        [
          false,
          false,
          true
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 32.0
    },
    "mv": {
      "mask": [
        [
          false,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          true,
          false,
          true
        ]
      ],
      "sum": 36.0
    },
    "cw,mh": {
      "mask": [
        [
          true,
          false,
          false
        ],
        [
          false,
          true,
          false
        ],
        [
          false,
          false,
          true
        ]
      ],
      "sum": 30.0
    }
  },
  "rectangular": {
    "mask": [
      [
        false,
        true
      ],
      [
        false,
        false
      ],
      [
        false,
        true
      ]
    ],
    "sum": 17.0
  },
  "normal": {
    "sum": 8.0,
    "mask": [
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        false
      ],
      [
        false,
        false,
        true
      ]
    ]
  }
}
```

## Reproduction: B04

_Source: [edbosne-pyfdd/repro/B04/README.md](edbosne-pyfdd/repro/B04/README.md)_

Run `sh repro/B04/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B04.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B04

_Source: [edbosne-pyfdd/repro/B04/RESULTS.txt](edbosne-pyfdd/repro/B04/RESULTS.txt)_

```text
before:
{
  "first": [
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ]
  ],
  "after_excursion": [
    [
      null,
      null,
      30.0
    ],
    [
      null,
      null,
      30.0
    ],
    [
      null,
      null,
      30.0
    ]
  ],
  "masked_after_excursion": 6,
  "normal": [
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ]
  ]
}
after:
{
  "first": [
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ]
  ],
  "after_excursion": [
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ]
  ],
  "masked_after_excursion": 0,
  "normal": [
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ],
    [
      10.0,
      10.0,
      10.0
    ]
  ]
}
```

## Reproduction: B05

_Source: [edbosne-pyfdd/repro/B05/README.md](edbosne-pyfdd/repro/B05/README.md)_

Run `sh repro/B05/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B05.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B05

_Source: [edbosne-pyfdd/repro/B05/RESULTS.txt](edbosne-pyfdd/repro/B05/RESULTS.txt)_

```text
before:
{
  "scalar_nomask_dof": -5,
  "ndarray_dof": {
    "error": "AttributeError",
    "message": "module 'numpy' has no attribute 'Array'"
  },
  "normal": {
    "explicit_mask_dof": 2
  }
}
after:
{
  "scalar_nomask_dof": 3,
  "ndarray_dof": 3,
  "normal": {
    "explicit_mask_dof": 2
  }
}
```

## Reproduction: B06

_Source: [edbosne-pyfdd/repro/B06/README.md](edbosne-pyfdd/repro/B06/README.md)_

Run `sh repro/B06/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B06.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B06

_Source: [edbosne-pyfdd/repro/B06/RESULTS.txt](edbosne-pyfdd/repro/B06/RESULTS.txt)_

```text
before:
{
  "positive_count_zero_probability": {
    "nll": 16.96210828960073,
    "chi2": 0.7160493827160492
  },
  "zero_count_zero_probability": {
    "nll": 16.96210828960073,
    "chi2": 0.7160493827160492
  },
  "normal": {
    "nll": 19.775021196025975,
    "chi2": 0.0
  }
}
after:
{
  "positive_count_zero_probability": {
    "nll": "infinity",
    "chi2": "infinity"
  },
  "zero_count_zero_probability": {
    "nll": 16.96210828960073,
    "chi2": 0.7160493827160492
  },
  "normal": {
    "nll": 19.775021196025975,
    "chi2": 0.0
  }
}
```

## Reproduction: B07

_Source: [edbosne-pyfdd/repro/B07/README.md](edbosne-pyfdd/repro/B07/README.md)_

Run `sh repro/B07/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/B07.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. Install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 matplotlib==3.9.4 numdifftools==0.9.42 PyQt5==5.15.11 seaborn==0.13.2`. Qt is imported by the package; the script sets offscreen mode and opens no GUI. No target-package installation is required; its pinned source is imported directly.

### References

- [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- [Upstream source at the reported commit](https://github.com/edbosne/pyfdd/tree/6aba44c5c4aaed278e08691f28abe79c724cf1da).

## Before and after: B07

_Source: [edbosne-pyfdd/repro/B07/RESULTS.txt](edbosne-pyfdd/repro/B07/RESULTS.txt)_

```text
before:
{
  "parameter_scales": {
    "1": {
      "fitted_total": 90.0,
      "std": 3e-10
    },
    "10": {
      "fitted_total": 90.0,
      "std": 3e-09
    }
  },
  "normal": {
    "chi2_at_80_counts": 1.2499999999999991
  }
}
after:
{
  "parameter_scales": {
    "1": {
      "fitted_total": 90.0,
      "std": 9.486833
    },
    "10": {
      "fitted_total": 90.0,
      "std": 9.486833
    }
  },
  "normal": {
    "chi2_at_80_counts": 1.2499999999999991
  }
}
```

---

# borenstein-lab/MUSiCC

Folder: [borenstein-lab-MUSiCC](borenstein-lab-MUSiCC)

## Report

_Source: [borenstein-lab-MUSiCC/README.md](borenstein-lab-MUSiCC/README.md)_

## borenstein-lab/MUSiCC

Pinned commit: [`478c9244cf406935e67abdf7622bdb05421ab1fb`](https://github.com/borenstein-lab/MUSiCC/tree/478c9244cf406935e67abdf7622bdb05421ab1fb).

1 confirmed defect, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### MUSICC-01 : Integer correction truncates abundances

[borenstein-lab/MUSiCC · musicc/core.py:177](https://github.com/borenstein-lab/MUSiCC/blob/478c9244cf406935e67abdf7622bdb05421ab1fb/musicc/core.py#L177). Integer input K01866=1, K00001=1, K01867=2: corrected abundances **[0,1,2] → [0.9914541785,1.0066761508,2.0133523016]**. Assignment into integer storage truncates correction, potentially zeroing positive genes. Correct: retain real-valued division by the [generic bias factor](https://github.com/borenstein-lab/MUSiCC/blob/478c9244cf406935e67abdf7622bdb05421ab1fb/musicc/core.py#L372); decimal encoding of identical input already agrees. [Repro](borenstein-lab-MUSiCC/repro/MUSICC-01/run.sh), [patch](borenstein-lab-MUSiCC/patches/MUSICC-01.patch).

```diff
-    abun = ko_abun_data.values
+    abun = ko_abun_data.values.astype(np.float64)
```

### References

- [Manor and Borenstein (2015). MUSiCC: a marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome.](https://doi.org/10.1186/s13059-015-0610-8)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/MUSiCC/tree/478c9244cf406935e67abdf7622bdb05421ab1fb).

## Reproduction: MUSICC-01

_Source: [borenstein-lab-MUSiCC/repro/MUSICC-01/README.md](borenstein-lab-MUSiCC/repro/MUSICC-01/README.md)_

Run `sh repro/MUSICC-01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/MUSICC-01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. MUSiCC requires `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2`. The R cases require R 4.5.2 with `install.packages(c("data.table","RColorBrewer","igraph","dplyr","tibble","logger"))`. Pass `--rscript PATH` if necessary. The scripts call the actual relevant source functions; they do not run the complete analysis pipelines.

### References

- [Manor and Borenstein (2015). MUSiCC: a marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome.](https://doi.org/10.1186/s13059-015-0610-8)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/MUSiCC/tree/478c9244cf406935e67abdf7622bdb05421ab1fb).

## Before and after: MUSICC-01

_Source: [borenstein-lab-MUSiCC/repro/MUSICC-01/RESULTS.txt](borenstein-lab-MUSiCC/repro/MUSICC-01/RESULTS.txt)_

```text
before:
{
  "mode": "before",
  "actual": {
    "K00001": 1,
    "K01866": 0,
    "K01867": 2
  },
  "independent_expected": {
    "K00001": 1.006676150800693,
    "K01866": 0.991454178451551,
    "K01867": 2.013352301601386
  },
  "integer_matches_reference": false,
  "float_matches_reference": true,
  "normal_input": "saved unpatched output"
}
after:
{
  "mode": "after",
  "actual": {
    "K00001": 1.0066761508006925,
    "K01866": 0.9914541784515506,
    "K01867": 2.013352301601385
  },
  "independent_expected": {
    "K00001": 1.006676150800693,
    "K01866": 0.991454178451551,
    "K01867": 2.013352301601386
  },
  "integer_matches_reference": true,
  "float_matches_reference": true,
  "normal_input": "bit-for-bit unchanged"
}
```

---

# borenstein-lab/mimosa2

Folder: [borenstein-lab-mimosa2](borenstein-lab-mimosa2)

## Report

_Source: [borenstein-lab-mimosa2/README.md](borenstein-lab-mimosa2/README.md)_

## borenstein-lab/mimosa2

Pinned commit: [`581b307dee48577117ac42599a07b33a51b0822d`](https://github.com/borenstein-lab/mimosa2/tree/581b307dee48577117ac42599a07b33a51b0822d).

2 confirmed defects, including 1 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### MIMOSA2-01 : KO dispatch drops options

[borenstein-lab/mimosa2 · R/core_mimosa2_funcs.R:1389](https://github.com/borenstein-lab/mimosa2/blob/581b307dee48577117ac42599a07b33a51b0822d/R/core_mimosa2_funcs.R#L1389). KO abundances 2 and 3, A→B reactions, `normalize=FALSE, relAbund=FALSE, remove_rev=FALSE`: CMP **(−400,400) → (−5,5)**. Dispatch ignores the last two flags, changing units and included reactions. Correct: forward them to the [documented callee](https://github.com/borenstein-lab/mimosa2/blob/581b307dee48577117ac42599a07b33a51b0822d/R/core_mimosa2_funcs.R#L1636); defaults are unchanged. [Repro](borenstein-lab-mimosa2/repro/MIMOSA2-01/run.sh), [patch](borenstein-lab-mimosa2/patches/MIMOSA2-01.patch).

```diff
-    spec_cmps = get_cmp_scores_kos(species_table, network, normalize = normalize, leave_rxns = leave_rxns)
+    spec_cmps = get_cmp_scores_kos(species_table, network, normalize = normalize, relAbund = relAbund, remove_rev = remove_rev, leave_rxns = leave_rxns)
```
#### MIMOSA2-02 : Sparse-zero covariance shares : minor

[borenstein-lab/mimosa2 · R/core_mimosa2_funcs.R:485](https://github.com/borenstein-lab/mimosa2/blob/581b307dee48577117ac42599a07b33a51b0822d/R/core_mimosa2_funcs.R#L485). A=(1,2,3), B=(3,0,1), zero residuals, omit B’s zero row: shares **(A=0,B=0,R=0) → (0,1,0)**. Shortcut uses unequal sample sets, hiding a contributor. Correct: `Cov(B,total)/Var(total)=1` after zero-filling, matching the [default matrix path](https://github.com/borenstein-lab/mimosa2/blob/581b307dee48577117ac42599a07b33a51b0822d/R/core_mimosa2_funcs.R#L485). Only known-zero omissions qualify; sparse semantics are undocumented and normal tables are dense. [Repro](borenstein-lab-mimosa2/repro/MIMOSA2-02/run.sh), [patch](borenstein-lab-mimosa2/patches/MIMOSA2-02.patch).

### References

- [Noecker et al. (2022). MIMOSA2: a metabolic network-based tool for inferring mechanism-supported relationships in microbiome-metabolome data.](https://doi.org/10.1093/bioinformatics/btac003)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/mimosa2/tree/581b307dee48577117ac42599a07b33a51b0822d).

## Reproduction: MIMOSA2-01

_Source: [borenstein-lab-mimosa2/repro/MIMOSA2-01/README.md](borenstein-lab-mimosa2/repro/MIMOSA2-01/README.md)_

Run `sh repro/MIMOSA2-01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/MIMOSA2-01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. MUSiCC requires `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2`. The R cases require R 4.5.2 with `install.packages(c("data.table","RColorBrewer","igraph","dplyr","tibble","logger"))`. Pass `--rscript PATH` if necessary. The scripts call the actual relevant source functions; they do not run the complete analysis pipelines.

### References

- [Noecker et al. (2022). MIMOSA2: a metabolic network-based tool for inferring mechanism-supported relationships in microbiome-metabolome data.](https://doi.org/10.1093/bioinformatics/btac003)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/mimosa2/tree/581b307dee48577117ac42599a07b33a51b0822d).

## Before and after: MIMOSA2-01

_Source: [borenstein-lab-mimosa2/repro/MIMOSA2-01/RESULTS.txt](borenstein-lab-mimosa2/repro/MIMOSA2-01/RESULTS.txt)_

```text
before:
normalize=TRUE relAbund=TRUE remove_rev=TRUE: A=-400, B=400 (matches direct call: TRUE)
normalize=TRUE relAbund=TRUE remove_rev=FALSE: A=-400, B=400 (matches direct call: FALSE)
normalize=TRUE relAbund=FALSE remove_rev=TRUE: A=-400, B=400 (matches direct call: FALSE)
normalize=TRUE relAbund=FALSE remove_rev=FALSE: A=-400, B=400 (matches direct call: FALSE)
normalize=FALSE relAbund=TRUE remove_rev=TRUE: A=-400, B=400 (matches direct call: TRUE)
normalize=FALSE relAbund=TRUE remove_rev=FALSE: A=-400, B=400 (matches direct call: FALSE)
normalize=FALSE relAbund=FALSE remove_rev=TRUE: A=-400, B=400 (matches direct call: FALSE)
normalize=FALSE relAbund=FALSE remove_rev=FALSE: A=-400, B=400 (matches direct call: FALSE)
after:
normalize=TRUE relAbund=TRUE remove_rev=TRUE: A=-400, B=400 (matches direct call: TRUE)
normalize=TRUE relAbund=TRUE remove_rev=FALSE: A=-500, B=500 (matches direct call: TRUE)
normalize=TRUE relAbund=FALSE remove_rev=TRUE: A=-2, B=2 (matches direct call: TRUE)
normalize=TRUE relAbund=FALSE remove_rev=FALSE: A=-2.5, B=2.5 (matches direct call: TRUE)
normalize=FALSE relAbund=TRUE remove_rev=TRUE: A=-400, B=400 (matches direct call: TRUE)
normalize=FALSE relAbund=TRUE remove_rev=FALSE: A=-1000, B=1000 (matches direct call: TRUE)
normalize=FALSE relAbund=FALSE remove_rev=TRUE: A=-2, B=2 (matches direct call: TRUE)
normalize=FALSE relAbund=FALSE remove_rev=FALSE: A=-5, B=5 (matches direct call: TRUE)
Normal/default KO path: unchanged for both normalize settings.
Independent signed-sum check: all 16 output values agree for the eight option combinations.
```

## Reproduction: MIMOSA2-02

_Source: [borenstein-lab-mimosa2/repro/MIMOSA2-02/README.md](borenstein-lab-mimosa2/repro/MIMOSA2-02/README.md)_

Run `sh repro/MIMOSA2-02/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/MIMOSA2-02.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. MUSiCC requires `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2`. The R cases require R 4.5.2 with `install.packages(c("data.table","RColorBrewer","igraph","dplyr","tibble","logger"))`. Pass `--rscript PATH` if necessary. The scripts call the actual relevant source functions; they do not run the complete analysis pipelines.

### References

- [Noecker et al. (2022). MIMOSA2: a metabolic network-based tool for inferring mechanism-supported relationships in microbiome-metabolome data.](https://doi.org/10.1093/bioinformatics/btac003)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/mimosa2/tree/581b307dee48577117ac42599a07b33a51b0822d).

## Before and after: MIMOSA2-02

_Source: [borenstein-lab-mimosa2/repro/MIMOSA2-02/RESULTS.txt](borenstein-lab-mimosa2/repro/MIMOSA2-02/RESULTS.txt)_

```text
before:
model_cov=FALSE: A=0, B=1, Residual=0
model_cov=TRUE: A=0, B=0, Residual=0
after:
model_cov=FALSE: A=0, B=1, Residual=0
model_cov=TRUE: A=0, B=1, Residual=0
Dense normal input: exactly unchanged.
Independent exact-rational check: A=0, B=1, Residual=0; shares sum to 1.
```

---

# borenstein-lab/MAAMOUL

Folder: [borenstein-lab-MAAMOUL](borenstein-lab-MAAMOUL)

## Report

_Source: [borenstein-lab-MAAMOUL/README.md](borenstein-lab-MAAMOUL/README.md)_

## borenstein-lab/MAAMOUL

Pinned commit: [`54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9`](https://github.com/borenstein-lab/MAAMOUL/tree/54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9).

1 confirmed defect, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### MAAMOUL-01 : Complete coverage crashes initialization

[borenstein-lab/MAAMOUL · R/utils.R:102](https://github.com/borenstein-lab/MAAMOUL/blob/54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9/R/utils.R#L102). Two EC nodes and two metabolite nodes, two edges, complete coverage of either type: **row-count error → 4 vertices, 2 edges**; complete-both has zero imputed nodes. Scalar attributes cannot form a zero-row data.frame, blocking valid custom networks. Correct: impute only absent nodes under the [constructor contract](https://github.com/borenstein-lab/MAAMOUL/blob/54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9/R/utils.R#L83); partial coverage is unchanged. [Repro](borenstein-lab-MAAMOUL/repro/MAAMOUL-01/run.sh), [patch](borenstein-lab-MAAMOUL/patches/MAAMOUL-01.patch).

### References

- [Muller, Baum and Borenstein (2026). MAAMOUL: metabolic network-based discovery of microbiome-metabolome shifts in disease.](https://doi.org/10.1093/bioinformatics/btag467)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/MAAMOUL/tree/54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9).

## Reproduction: MAAMOUL-01

_Source: [borenstein-lab-MAAMOUL/repro/MAAMOUL-01/README.md](borenstein-lab-MAAMOUL/repro/MAAMOUL-01/README.md)_

Run `sh repro/MAAMOUL-01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/MAAMOUL-01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11. MUSiCC requires `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2`. The R cases require R 4.5.2 with `install.packages(c("data.table","RColorBrewer","igraph","dplyr","tibble","logger"))`. Pass `--rscript PATH` if necessary. The scripts call the actual relevant source functions; they do not run the complete analysis pipelines.

### References

- [Muller, Baum and Borenstein (2026). MAAMOUL: metabolic network-based discovery of microbiome-metabolome shifts in disease.](https://doi.org/10.1093/bioinformatics/btag467)
- [Upstream source at the reported commit](https://github.com/borenstein-lab/MAAMOUL/tree/54f174c5a3a8d07ebac5b3431c43eb4bbfdc83b9).

## Before and after: MAAMOUL-01

_Source: [borenstein-lab-MAAMOUL/repro/MAAMOUL-01/RESULTS.txt](borenstein-lab-MAAMOUL/repro/MAAMOUL-01/RESULTS.txt)_

```text
before:
partial: 4 vertices, 2 edges, 2 imputed nodes
metabolites_complete: ERROR: arguments imply differing number of rows: 0, 1
ECs_complete: ERROR: arguments imply differing number of rows: 0, 1
both_complete: ERROR: arguments imply differing number of rows: 0, 1
after:
partial: 4 vertices, 2 edges, 2 imputed nodes
metabolites_complete: 4 vertices, 2 edges, 1 imputed nodes
ECs_complete: 4 vertices, 2 edges, 1 imputed nodes
both_complete: 4 vertices, 2 edges, 0 imputed nodes
Normal partial-coverage graph and all attributes: unchanged.
Independent set-based check: all four coverage cases agree; 4 vertices, 2 input edges.
```

---

# glarue/intronIC

Folder: [glarue-intronIC](glarue-intronIC)

## Report

_Source: [glarue-intronIC/README.md](glarue-intronIC/README.md)_

## glarue/intronIC

Pinned commit: [`0db1d54274f1ffdbbc95dea6589a75a833eb831d`](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

5 confirmed defects, including 1 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### R02 : Branch-point windows differ by strand

[glarue/intronIC · src/intronIC/extraction/sequences.py:368](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/extraction/sequences.py#L368). Two mirrored synthetic introns with an ambiguous boundary base: branch-point window/reference mismatches **3 → 0** across strands/access modes. Coordinate conversions select different bases, bypassing ambiguity exclusion. Correct: slice transcript-oriented intron offsets under the [scoring coordinates](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/extraction/sequences.py#L81). [Repro](glarue-intronIC/repro/R02/run.sh), [patch](glarue-intronIC/patches/R02.patch).
#### R01 : Default installation omits pandas

[glarue/intronIC · pyproject.toml:25](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/pyproject.toml#L25). Fresh install with declared dependencies: pandas import **exit 1 → 0**; default classification **abort → completion**. Post-processing requires an undeclared package, blocking clean installs. Correct: declare the dependency used by [post-processing](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/cli/main.py#L327). [Repro](glarue-intronIC/repro/R01/run.sh), [patch](glarue-intronIC/patches/R01.patch).

```diff
+    "pandas>=1.3.0",
```
#### R03 : Short flank empties quality window

[glarue/intronIC · src/intronIC/extraction/sequences.py:353](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/extraction/sequences.py#L353). Two synthetic introns with only three downstream bases and an intronic N: introns passing indexed ambiguity filtering **2 → 0**. A zero-relative stop becomes an empty 3′ quality slice, letting ambiguous inputs through. Correct: absolute half-open indices retain the [specified scoring interval](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/cli/main.py#L2921), including at contig ends. Both extraction and CLI copies are fixed. [Repro](glarue-intronIC/repro/R03/run.sh), [patch](glarue-intronIC/patches/R03.patch).
#### R04 : Header-free classification aborts

[glarue/intronIC · src/intronIC/cli/main.py:5064](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/cli/main.py#L5064). Two toy introns, documented `--no-headers`: **exit 1 → 0**, with header-free score rows. Post-processing reads column names after headers were suppressed, preventing completion. Correct: retain internal headers until readers finish, then remove the single header row required by the [output option](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/cli/main.py). [Repro](glarue-intronIC/repro/R04/run.sh), [patch](glarue-intronIC/patches/R04.patch).
#### R05 : Extraction helper crashes on exhaustion : minor

[glarue/intronIC · src/intronIC/file_io/genome.py:128](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/file_io/genome.py#L128). Exhaust the extraction generator on two toy introns: **2 records then AttributeError → 2 records and exit 0**. Cleanup calls a missing `close()`, breaking direct helper consumers. Correct: release cached state; FASTA streams already close after parsing ([reader implementation](https://github.com/glarue/intronIC/blob/0db1d54274f1ffdbbc95dea6589a75a833eb831d/src/intronIC/file_io/genome.py#L133)). No CLI impact demonstrated. [Repro](glarue-intronIC/repro/R05/run.sh), [patch](glarue-intronIC/patches/R05.patch).

### References

- [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- [Upstream source at the reported commit](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

## Reproduction: R01

_Source: [glarue-intronIC/repro/R01/README.md](glarue-intronIC/repro/R01/README.md)_

Run `sh repro/R01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/R01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+. For R02–R05 install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 biogl==3.0.1 matplotlib==3.9.4 networkx rich smart-open tqdm pyyaml joblib pyfastx`. R01 creates a separate temporary venv and installs the pinned package with its declared dependencies, before and after patching. Fixtures are hand-written toy inputs; no biological measurements are used.

### References

- [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- [Upstream source at the reported commit](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

## Before and after: R01

_Source: [glarue-intronIC/repro/R01/RESULTS.txt](glarue-intronIC/repro/R01/RESULTS.txt)_

```text
before: pandas import exit 1
after: pandas import exit 0
```

## Reproduction: R02

_Source: [glarue-intronIC/repro/R02/README.md](glarue-intronIC/repro/R02/README.md)_

Run `sh repro/R02/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/R02.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+. For R02–R05 install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 biogl==3.0.1 matplotlib==3.9.4 networkx rich smart-open tqdm pyyaml joblib pyfastx`. R01 creates a separate temporary venv and installs the pinned package with its declared dependencies, before and after patching. Fixtures are hand-written toy inputs; no biological measurements are used.

### References

- [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- [Upstream source at the reported commit](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

## Before and after: R02

_Source: [glarue-intronIC/repro/R02/RESULTS.txt](glarue-intronIC/repro/R02/RESULTS.txt)_

```text
before: window/reference mismatches = 3; indexed introns passing ambiguity filter = 2
after: window/reference mismatches = 0; indexed introns passing ambiguity filter = 0
```

## Reproduction: R03

_Source: [glarue-intronIC/repro/R03/README.md](glarue-intronIC/repro/R03/README.md)_

Run `sh repro/R03/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/R03.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+. For R02–R05 install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 biogl==3.0.1 matplotlib==3.9.4 networkx rich smart-open tqdm pyyaml joblib pyfastx`. R01 creates a separate temporary venv and installs the pinned package with its declared dependencies, before and after patching. Fixtures are hand-written toy inputs; no biological measurements are used.

### References

- [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- [Upstream source at the reported commit](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

## Before and after: R03

_Source: [glarue-intronIC/repro/R03/RESULTS.txt](glarue-intronIC/repro/R03/RESULTS.txt)_

```text
before: window/reference mismatches = 4; indexed introns passing ambiguity filter = 2
after: window/reference mismatches = 0; indexed introns passing ambiguity filter = 0
```

## Reproduction: R04

_Source: [glarue-intronIC/repro/R04/README.md](glarue-intronIC/repro/R04/README.md)_

Run `sh repro/R04/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/R04.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+. For R02–R05 install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 biogl==3.0.1 matplotlib==3.9.4 networkx rich smart-open tqdm pyyaml joblib pyfastx`. R01 creates a separate temporary venv and installs the pinned package with its declared dependencies, before and after patching. Fixtures are hand-written toy inputs; no biological measurements are used.

### References

- [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- [Upstream source at the reported commit](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

## Before and after: R04

_Source: [glarue-intronIC/repro/R04/RESULTS.txt](glarue-intronIC/repro/R04/RESULTS.txt)_

```text
before: exit 1
after: exit 0
header-free score rows: 2
```

## Reproduction: R05

_Source: [glarue-intronIC/repro/R05/README.md](glarue-intronIC/repro/R05/README.md)_

Run `sh repro/R05/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/R05.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.10+. For R02–R05 install `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 biogl==3.0.1 matplotlib==3.9.4 networkx rich smart-open tqdm pyyaml joblib pyfastx`. R01 creates a separate temporary venv and installs the pinned package with its declared dependencies, before and after patching. Fixtures are hand-written toy inputs; no biological measurements are used.

### References

- [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- [Upstream source at the reported commit](https://github.com/glarue/intronIC/tree/0db1d54274f1ffdbbc95dea6589a75a833eb831d).

## Before and after: R05

_Source: [glarue-intronIC/repro/R05/RESULTS.txt](glarue-intronIC/repro/R05/RESULTS.txt)_

```text
before: {"chrom": "forward", "body": "GTACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCATTCCATAACTAACTCTCTCTCTCTCTCTCTCTAG"}
{"chrom": "reverse", "body": "GTACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCATTCCATAACTAACTCTCTCTCTCTCTCTCTCTAG"}
AttributeError: GenomeReader has no attribute close
after: {"chrom": "forward", "body": "GTACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCATTCCATAACTAACTCTCTCTCTCTCTCTCTCTAG"}
{"chrom": "reverse", "body": "GTACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCAACGTTGCATTCCATAACTAACTCTCTCTCTCTCTCTCTCTAG"}
EXTRACTION_COMPLETE
exit 0
```

---

# feedzai/deccaf

Folder: [feedzai-deccaf](feedzai-deccaf)

## Report

_Source: [feedzai-deccaf/README.md](feedzai-deccaf/README.md)_

## feedzai/deccaf

Pinned commit: [`b910b48d7e146d53b5f145224b819bdb0962d40a`](https://github.com/feedzai/deccaf/tree/b910b48d7e146d53b5f145224b819bdb0962d40a).

3 confirmed defects, including 2 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### DECCAF-003 : FPR threshold exceeds budget

[feedzai/deccaf · Code/alert_model/hpo_fpr.py:24](https://github.com/feedzai/deccaf/blob/b910b48d7e146d53b5f145224b819bdb0962d40a/Code/alert_model/hpo_fpr.py#L24). Nine negatives at 5%: false positives **9 → 0**; 100 negatives with 20 tied at the boundary: **20 → 0** (budget 5). Index −1 and ties inflate accepted negatives and the optimization objective. Correct: select the most permissive attainable ROC threshold within the [5% constraint](https://github.com/feedzai/deccaf/blob/b910b48d7e146d53b5f145224b819bdb0962d40a/Documents/Paper.pdf), across all four copies. Preprocessing uses strict `>`; the other callers use `>=`. No error is established in the archived 5% validation boundary. [Repro](feedzai-deccaf/repro/DECCAF-003/run.sh), [patch](feedzai-deccaf/patches/DECCAF-003.patch).
#### DECCAF-002 : Batch labels drop cases : minor

[feedzai/deccaf · Code/deferral/run_alert.py:140](https://github.com/feedzai/deccaf/blob/b910b48d7e146d53b5f145224b819bdb0962d40a/Code/deferral/run_alert.py#L140). Two cases with matching capacity row, batch 0: saved rows **0 → 2** in all five methods; batch 2: capacity-aware methods **IndexError → 2 rows**. Loops invent absent labels, breaking relabeling/subsetting. Correct: membership and quotas are unchanged by labels ([batch definition, §3.2](https://github.com/feedzai/deccaf/blob/b910b48d7e146d53b5f145224b819bdb0962d40a/Documents/Paper.pdf)). Arbitrary labels are undocumented; supplied batches use 1. [Repro](feedzai-deccaf/repro/DECCAF-002/run.sh), [patch](feedzai-deccaf/patches/DECCAF-002.patch).
#### DECCAF-001 : Capacity column order changes quotas : minor

[feedzai/deccaf · Code/deferral/run_alert.py:142](https://github.com/feedzai/deccaf/blob/b910b48d7e146d53b5f145224b819bdb0962d40a/Code/deferral/run_alert.py#L142). Two cases, one human slot; reorder named capacity columns: CP **no solution → 2 assignments**, minimum cost **0.2**; OvA **1 → 2 rows**, random allocation **crash → 2 rows**. Positional summation includes metadata, changing the problem. Correct: use named worker quotas ([constraints, §3.3](https://github.com/feedzai/deccaf/blob/b910b48d7e146d53b5f145224b819bdb0962d40a/Documents/Paper.pdf)). Column-order independence is undocumented; supplied files are unaffected. [Repro](feedzai-deccaf/repro/DECCAF-001/run.sh), [patch](feedzai-deccaf/patches/DECCAF-001.patch).

### References

- [Alves et al. (2024). Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints.](https://doi.org/10.48550/arXiv.2403.06906)
- [Upstream source at the reported commit](https://github.com/feedzai/deccaf/tree/b910b48d7e146d53b5f145224b819bdb0962d40a).

## Reproduction: DECCAF-001

_Source: [feedzai-deccaf/repro/DECCAF-001/README.md](feedzai-deccaf/repro/DECCAF-001/README.md)_

Run `sh repro/DECCAF-001/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/DECCAF-001.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 ortools==9.7.2996 pyarrow==17.0.0`. Only function definitions are loaded from the source, avoiding experiment loops. Allocation uses the real solver with one worker. Threshold checks execute the original arithmetic, including the objective threshold block, without model training. These are arithmetic counterexamples, not performance benchmarks.

### References

- [Alves et al. (2024). Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints.](https://doi.org/10.48550/arXiv.2403.06906)
- [Upstream source at the reported commit](https://github.com/feedzai/deccaf/tree/b910b48d7e146d53b5f145224b819bdb0962d40a).

## Before and after: DECCAF-001

_Source: [feedzai-deccaf/repro/DECCAF-001/RESULTS.txt](feedzai-deccaf/repro/DECCAF-001/RESULTS.txt)_

```text
before:
{
  "normal/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  },
  "reordered/deccaf_cp_deferral_func": {
    "returned": null
  },
  "reordered/ova_deferral_func": {
    "assignments": {
      "10": "human"
    },
    "predictions": {
      "10": 0
    },
    "rows": 1
  },
  "reordered/rand_deferral_func": {
    "error": "IndexError: Cannot choose from an empty sequence"
  },
  "reordered/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "reordered/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  }
}
after:
Exact minimum assignment cost: 0.2
{
  "normal/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  },
  "reordered/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "reordered/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "reordered/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "reordered/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "reordered/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  }
}
```

## Reproduction: DECCAF-002

_Source: [feedzai-deccaf/repro/DECCAF-002/README.md](feedzai-deccaf/repro/DECCAF-002/README.md)_

Run `sh repro/DECCAF-002/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/DECCAF-002.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 ortools==9.7.2996 pyarrow==17.0.0`. Only function definitions are loaded from the source, avoiding experiment loops. Allocation uses the real solver with one worker. Threshold checks execute the original arithmetic, including the objective threshold block, without model training. These are arithmetic counterexamples, not performance benchmarks.

### References

- [Alves et al. (2024). Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints.](https://doi.org/10.48550/arXiv.2403.06906)
- [Upstream source at the reported commit](https://github.com/feedzai/deccaf/tree/b910b48d7e146d53b5f145224b819bdb0962d40a).

## Before and after: DECCAF-002

_Source: [feedzai-deccaf/repro/DECCAF-002/RESULTS.txt](feedzai-deccaf/repro/DECCAF-002/RESULTS.txt)_

```text
before:
{
  "normal/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  },
  "label_2/deccaf_cp_deferral_func": {
    "error": "IndexError: single positional indexer is out-of-bounds"
  },
  "label_2/ova_deferral_func": {
    "error": "IndexError: single positional indexer is out-of-bounds"
  },
  "label_2/rand_deferral_func": {
    "error": "IndexError: single positional indexer is out-of-bounds"
  },
  "label_2/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "label_2/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  },
  "label_0/deccaf_cp_deferral_func": {
    "assignments": {},
    "predictions": {},
    "rows": 0
  },
  "label_0/ova_deferral_func": {
    "assignments": {},
    "predictions": {},
    "rows": 0
  },
  "label_0/rand_deferral_func": {
    "assignments": {},
    "predictions": {},
    "rows": 0
  },
  "label_0/full_auto_func": {
    "assignments": {},
    "predictions": {},
    "rows": 0
  },
  "label_0/full_model_func": {
    "assignments": {},
    "predictions": {},
    "rows": 0
  }
}
after:
Exact minimum assignment cost: 0.2
{
  "normal/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "normal/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "normal/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  },
  "label_2/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "label_2/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "label_2/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "label_2/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "label_2/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  },
  "label_0/deccaf_cp_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "label_0/ova_deferral_func": {
    "assignments": {
      "10": "human",
      "20": "model#0"
    },
    "predictions": {
      "10": 0,
      "20": 0
    },
    "rows": 2
  },
  "label_0/rand_deferral_func": {
    "assignments": {
      "10": "model#0",
      "20": "human"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "label_0/full_auto_func": {
    "assignments": {
      "10": "auto-reject",
      "20": "auto-reject"
    },
    "predictions": {
      "10": 1,
      "20": 1
    },
    "rows": 2
  },
  "label_0/full_model_func": {
    "assignments": {
      "10": "model#0",
      "20": "model#0"
    },
    "predictions": {
      "10": 1,
      "20": 0
    },
    "rows": 2
  }
}
```

## Reproduction: DECCAF-003

_Source: [feedzai-deccaf/repro/DECCAF-003/README.md](feedzai-deccaf/repro/DECCAF-003/README.md)_

Run `sh repro/DECCAF-003/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/DECCAF-003.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1 pandas==1.5.3 scikit-learn==1.5.2 ortools==9.7.2996 pyarrow==17.0.0`. Only function definitions are loaded from the source, avoiding experiment loops. Allocation uses the real solver with one worker. Threshold checks execute the original arithmetic, including the objective threshold block, without model training. These are arithmetic counterexamples, not performance benchmarks.

### References

- [Alves et al. (2024). Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints.](https://doi.org/10.48550/arXiv.2403.06906)
- [Upstream source at the reported commit](https://github.com/feedzai/deccaf/tree/b910b48d7e146d53b5f145224b819bdb0962d40a).

## Before and after: DECCAF-003

_Source: [feedzai-deccaf/repro/DECCAF-003/RESULTS.txt](feedzai-deccaf/repro/DECCAF-003/RESULTS.txt)_

```text
before:
{
  "alert_model/hpo_fpr.py/small": {
    "true_positives": 2
  },
  "alert_model/hpo_fpr.py/normal": {
    "true_positives": 2
  },
  "alert_model/hpo_fpr.py/ties": {
    "true_positives": 1
  },
  "alert_model/hpo_fpr.py/rounded_budget": {
    "true_positives": 2
  },
  "alert_model/training_and_predicting.py/small": {
    "true_positives": 2,
    "false_positives": 9,
    "threshold": 0.1,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ]
  },
  "alert_model/training_and_predicting.py/normal": {
    "true_positives": 2,
    "false_positives": 5,
    "threshold": 0.96,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "alert_model/training_and_predicting.py/ties": {
    "true_positives": 1,
    "false_positives": 20,
    "threshold": 0.8,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ]
  },
  "alert_model/training_and_predicting.py/rounded_budget": {
    "true_positives": 2,
    "false_positives": 2,
    "threshold": 0.99,
    "decisions": [
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "data/preprocess.py/small": {
    "true_positives": 2,
    "false_positives": 9,
    "threshold": 0.1,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ]
  },
  "data/preprocess.py/normal": {
    "true_positives": 2,
    "false_positives": 5,
    "threshold": 0.96,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "data/preprocess.py/ties": {
    "true_positives": 1,
    "false_positives": 20,
    "threshold": 0.8,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ]
  },
  "data/preprocess.py/rounded_budget": {
    "true_positives": 2,
    "false_positives": 2,
    "threshold": 0.99,
    "decisions": [
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "HPO.objective/small": {
    "true_positives": 2,
    "false_positives": 9
  },
  "HPO.objective/normal": {
    "true_positives": 2,
    "false_positives": 5
  },
  "HPO.objective/ties": {
    "true_positives": 1,
    "false_positives": 20
  },
  "HPO.objective/rounded_budget": {
    "true_positives": 2,
    "false_positives": 2
  }
}
after:
{
  "alert_model/hpo_fpr.py/small": {
    "true_positives": 1
  },
  "alert_model/hpo_fpr.py/normal": {
    "true_positives": 2
  },
  "alert_model/hpo_fpr.py/ties": {
    "true_positives": 1
  },
  "alert_model/hpo_fpr.py/rounded_budget": {
    "true_positives": 2
  },
  "alert_model/training_and_predicting.py/small": {
    "true_positives": 1,
    "false_positives": 0,
    "threshold": 0.95,
    "decisions": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ]
  },
  "alert_model/training_and_predicting.py/normal": {
    "true_positives": 2,
    "false_positives": 5,
    "threshold": 0.96,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "alert_model/training_and_predicting.py/ties": {
    "true_positives": 1,
    "false_positives": 0,
    "threshold": 0.9,
    "decisions": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ]
  },
  "alert_model/training_and_predicting.py/rounded_budget": {
    "true_positives": 2,
    "false_positives": 1,
    "threshold": 0.995,
    "decisions": [
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "data/preprocess.py/small": {
    "true_positives": 1,
    "false_positives": 0,
    "threshold": 0.95,
    "decisions": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ]
  },
  "data/preprocess.py/normal": {
    "true_positives": 2,
    "false_positives": 5,
    "threshold": 0.96,
    "decisions": [
      1,
      1,
      1,
      1,
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "data/preprocess.py/ties": {
    "true_positives": 1,
    "false_positives": 0,
    "threshold": 0.9,
    "decisions": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      0
    ]
  },
  "data/preprocess.py/rounded_budget": {
    "true_positives": 2,
    "false_positives": 1,
    "threshold": 0.995,
    "decisions": [
      1,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1
    ]
  },
  "HPO.objective/small": {
    "true_positives": 1,
    "false_positives": 0
  },
  "HPO.objective/normal": {
    "true_positives": 2,
    "false_positives": 5
  },
  "HPO.objective/ties": {
    "true_positives": 1,
    "false_positives": 0
  },
  "HPO.objective/rounded_budget": {
    "true_positives": 2,
    "false_positives": 1
  }
}
```

---

# weissmanlab/magic

Folder: [weissmanlab-magic](weissmanlab-magic)

## Report

_Source: [weissmanlab-magic/README.md](weissmanlab-magic/README.md)_

## weissmanlab/magic

Pinned commit: [`87fd0923480d28399c5078ff4efd60c3205c22a0`](https://github.com/weissmanlab/magic/tree/87fd0923480d28399c5078ff4efd60c3205c22a0).

4 confirmed defects, including 0 minor. Reported to the authors, Nov 2026.

Run `sh repro/<ID>/run.sh` from this project folder. Each patch applies individually from the upstream repository root at the pinned commit. Dependencies are listed with each reproduction. No change to published scientific results is established.

#### W01 : Initialization loses final window

[weissmanlab/magic · windower.py:61](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/windower.py#L61). Four 80-base windows, events at 1,81,161,241,320: counts **[1,1,2] → [1,1,1,2]**; retained events **4 → 5**. Too few histogram edges lose terminal data and misassign a boundary, changing inference inputs. Correct: integer window membership gives those four counts under the [producer’s coverage convention](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/combo_prep.py). [Repro](weissmanlab-magic/repro/W01/run.sh), [patch](weissmanlab-magic/patches/W01.patch).

```diff
-	windowcounts = numpy.histogram(SNPs, bins=list(range(1, len(basecoverage)*L0+1, L0)))[0]
+	windowcounts = numpy.histogram(SNPs, bins=list(range(1, (len(basecoverage)+1)*L0+1, L0)))[0]
```
#### M02 : Zero-mass output serialization crashes

[weissmanlab/magic · magic.py:427](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/magic.py#L427). Gamma parameters `[0.5,1,1,0.5]`: **TypeError → rows `[0.5,1,1]` and `[0.5]`**. A scalar zero mass reaches a row iterator, preventing final output after fitting. Correct: the [documented format](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/README.md) requires a one-column final row; no-zero output is unchanged. [Repro](weissmanlab-magic/repro/M02/run.sh), [patch](weissmanlab-magic/patches/M02.patch).

```diff
-			niceparams += [wzero,]
+			niceparams += [[wzero],]
```
#### W02 : Table inputs crash and merge too early

[weissmanlab/magic · windower.py:77](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/windower.py#L77). Count/coverage rows `(1,80)…(4,80)`, either advertised order: **NameError → scale-0 counts [1,2,3,4], scale-1 [3,7]**. RNG initialization is absent and scale 0 is prematurely merged, blocking these inputs. Correct: preserve input rows at their [declared base scale](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/windower.py#L112), merging only at later scales. [Repro](weissmanlab-magic/repro/W02/run.sh), [patch](weissmanlab-magic/patches/W02.patch).
#### M01 : Mean omits infinite tail

[weissmanlab/magic · magic.py:503](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/magic.py#L503). One rate-2 exponential: mean **0 → 0.5**; breaks [0,1], rates [1,2]: **0.632120559 → 0.816060279**, normalized block fraction at zero **1.290988 → 1**. Dropped tail mass understates means and permits fractions above one. Correct: integrate the [implemented survival function](https://github.com/weissmanlab/magic/blob/87fd0923480d28399c5078ff4efd60c3205c22a0/magic.py#L496), including its unbounded last interval. CLI fitting does not call this mean. [Repro](weissmanlab-magic/repro/M01/run.sh), [patch](weissmanlab-magic/patches/M01.patch).

```diff
-		return -np.concatenate((np.diff(self.breakPs), [0])) @ (1/self.rates)
+		return -np.diff(np.concatenate((self.breakPs, [0]))) @ (1/self.rates)
```

### References

- [Weissman and Hallatschek (2017). Minimal-assumption inference from population-genomic data.](https://doi.org/10.7554/eLife.24836)
- [Upstream source at the reported commit](https://github.com/weissmanlab/magic/tree/87fd0923480d28399c5078ff4efd60c3205c22a0).

## Reproduction: M01

_Source: [weissmanlab-magic/repro/M01/README.md](weissmanlab-magic/repro/M01/README.md)_

Run `sh repro/M01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/M01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1`. The scripts call the pinned implementation; M02 also exercises the actual CLI output writer on a synthetic transform. Its short optimization checks serialization rather than parameter recovery.

### References

- [Weissman and Hallatschek (2017). Minimal-assumption inference from population-genomic data.](https://doi.org/10.7554/eLife.24836)
- [Upstream source at the reported commit](https://github.com/weissmanlab/magic/tree/87fd0923480d28399c5078ff4efd60c3205c22a0).

## Before and after: M01

_Source: [weissmanlab-magic/repro/M01/RESULTS.txt](weissmanlab-magic/repro/M01/RESULTS.txt)_

```text
before: {"means": [0.0, 0.6321205588285577, 0.33250708260777784], "normal_pdf": [0.7788007830714049, 0.6065306597126334, 0.7357588823428847, 0.0995741367357279], "normal_cdf": [0.22119921692859512, 0.3934693402873666, 0.6321205588285577, 0.950212931632136], "normal_laplace": [1.0, 0.6964173546864574, 0.5225558805394355, 0.34163117806131066], "block_fraction_at_zero": 1.2909883534346633}
after: {"means": [0.5, 0.8160602794142788, 0.3333333333333333], "normal_pdf": [0.7788007830714049, 0.6065306597126334, 0.7357588823428847, 0.0995741367357279], "normal_cdf": [0.22119921692859512, 0.3934693402873666, 0.6321205588285577, 0.950212931632136], "normal_laplace": [1.0, 0.6964173546864574, 0.5225558805394355, 0.34163117806131066], "block_fraction_at_zero": 1.0}
correct: {"means": [0.4999999999999997, 0.8160602794142786, 0.33333333333333276], "one_piece_definition": 0.5, "two_piece_definition": 0.8160602794142788}
Numerical reference agrees.
```

## Reproduction: M02

_Source: [weissmanlab-magic/repro/M02/README.md](weissmanlab-magic/repro/M02/README.md)_

Run `sh repro/M02/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/M02.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1`. The scripts call the pinned implementation; M02 also exercises the actual CLI output writer on a synthetic transform. Its short optimization checks serialization rather than parameter recovery.

### References

- [Weissman and Hallatschek (2017). Minimal-assumption inference from population-genomic data.](https://doi.org/10.7554/eLife.24836)
- [Upstream source at the reported commit](https://github.com/weissmanlab/magic/tree/87fd0923480d28399c5078ff4efd60c3205c22a0).

## Before and after: M02

_Source: [weissmanlab-magic/repro/M02/RESULTS.txt](weissmanlab-magic/repro/M02/RESULTS.txt)_

```text
before: {"format_error": "TypeError: 'numpy.float64' object is not iterable", "formatted": null, "cli_exit": 1, "cli_error": ["TypeError: 'numpy.float64' object is not iterable"], "cli_final": null, "normal_nozero_output": "0.4 1.0 1.0\n0.6 2.0 3.0"}
after: {"format_error": null, "formatted": "0.5 1.0 1.0\n0.5", "cli_exit": 0, "cli_error": [], "cli_final": "0.4939277580409113 1.0609009303930115 0.9445331276984255\n0.5060722419590887\n", "normal_nozero_output": "0.4 1.0 1.0\n0.6 2.0 3.0"}
correct: {"gamma_row": [0.5, 1.0, 1.0], "zero_row": [0.5], "laplace_points": [[1.0, 0.75], [2.0, 0.6666666666666666], [4.0, 0.6]], "zero_mass_format": "one row containing a single column"}
Numerical reference agrees.
```

## Reproduction: W01

_Source: [weissmanlab-magic/repro/W01/README.md](weissmanlab-magic/repro/W01/README.md)_

Run `sh repro/W01/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/W01.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1`. The scripts call the pinned implementation; M02 also exercises the actual CLI output writer on a synthetic transform. Its short optimization checks serialization rather than parameter recovery.

### References

- [Weissman and Hallatschek (2017). Minimal-assumption inference from population-genomic data.](https://doi.org/10.7554/eLife.24836)
- [Upstream source at the reported commit](https://github.com/weissmanlab/magic/tree/87fd0923480d28399c5078ff4efd60c3205c22a0).

## Before and after: W01

_Source: [weissmanlab-magic/repro/W01/RESULTS.txt](weissmanlab-magic/repro/W01/RESULTS.txt)_

```text
before: {"windows": [[1, 80], [1, 80], [2, 80]], "retained_sites": 4, "normal_histogram": {"0": 1, "1": 1, "2": 1, "3": 1}, "oracle_mismatches": 1368}
after: {"windows": [[1, 80], [1, 80], [1, 80], [2, 80]], "retained_sites": 5, "normal_histogram": {"0": 1, "1": 1, "2": 1, "3": 1}, "oracle_mismatches": 0}
correct: {"windows": [[1, 80], [1, 80], [1, 80], [2, 80]], "histogram": {"1": 3, "2": 1}}
Numerical reference agrees.
```

## Reproduction: W02

_Source: [weissmanlab-magic/repro/W02/README.md](weissmanlab-magic/repro/W02/README.md)_

Run `sh repro/W02/run.sh` from the project folder, or set `PYTHON` to a Python environment with the dependencies below. Git, a network connection and the adjacent `patches/W02.patch` are required. `--source CHECKOUT` uses an existing pinned checkout without changing it. Temporary source copies are removed on exit.

Dependencies tested: Python 3.11 with `numpy==1.26.4 scipy==1.13.1`. The scripts call the pinned implementation; M02 also exercises the actual CLI output writer on a synthetic transform. Its short optimization checks serialization rather than parameter recovery.

### References

- [Weissman and Hallatschek (2017). Minimal-assumption inference from population-genomic data.](https://doi.org/10.7554/eLife.24836)
- [Upstream source at the reported commit](https://github.com/weissmanlab/magic/tree/87fd0923480d28399c5078ff4efd60c3205c22a0).

## Before and after: W02

_Source: [weissmanlab-magic/repro/W02/RESULTS.txt](weissmanlab-magic/repro/W02/RESULTS.txt)_

```text
before: {"windows_no": {"exit": 1, "error": ["NameError: name 'prng' is not defined. Did you mean: 'print'?"], "counts": null}, "windows_down": {"exit": 1, "error": ["NameError: name 'prng' is not defined. Did you mean: 'print'?"], "counts": null}, "windows_up": {"exit": 1, "error": ["NameError: name 'prng' is not defined. Did you mean: 'print'?"], "counts": null}, "reverse_windows_no": {"exit": 1, "error": ["NameError: name 'prng' is not defined. Did you mean: 'print'?"], "counts": null}, "reverse_windows_down": {"exit": 1, "error": ["NameError: name 'prng' is not defined. Did you mean: 'print'?"], "counts": null}, "reverse_windows_up": {"exit": 1, "error": ["NameError: name 'prng' is not defined. Did you mean: 'print'?"], "counts": null}, "normal_sampled_histogram": {"0": 1, "1": 1, "4": 1, "9": 1}, "normal_merge": [[3, 160], [7, 160]]}
after: {"windows_no": {"exit": 0, "error": [], "counts": "1 1, 2 1, 3 1, 4 1\n3 1, 7 1\n"}, "windows_down": {"exit": 0, "error": [], "counts": "64 4\n128 2\n"}, "windows_up": {"exit": 0, "error": [], "counts": "80 4\n160 2\n"}, "reverse_windows_no": {"exit": 0, "error": [], "counts": "1 1, 2 1, 3 1, 4 1\n3 1, 7 1\n"}, "reverse_windows_down": {"exit": 0, "error": [], "counts": "64 4\n128 2\n"}, "reverse_windows_up": {"exit": 0, "error": [], "counts": "80 4\n160 2\n"}, "normal_sampled_histogram": {"0": 1, "1": 1, "4": 1, "9": 1}, "normal_merge": [[3, 160], [7, 160]]}
correct: {"counts_text": "1 1, 2 1, 3 1, 4 1\n3 1, 7 1\n", "default_down_text": "64 4\n128 2\n", "up_text": "80 4\n160 2\n"}
Numerical reference agrees.
```

---

# GO::TermFinder

Folder: [cpan-GO-TermFinder](cpan-GO-TermFinder)

## Report

_Source: [cpan-GO-TermFinder/README.md](cpan-GO-TermFinder/README.md)_

## GO::TermFinder 0.86

Reported to the authors, Nov 2026.

Reproduction inputs and outputs are described below. The supplied bundle contains no reproduction scripts.

Source: CPAN GO-TermFinder-0.86.tar.gz (SHA-256 8daad833bffa65e726684ab98cb175f7c7f97d4e468362a2936fe0cd42bf0ea3). Each bug has a patch in [patches/](cpan-GO-TermFinder/patches/) against pristine 0.86; [patches/all-six.patch](cpan-GO-TermFinder/patches/all-six.patch) applies them together. With all six applied the original 8,116 tests still pass.

Four change results (GTF-001, 004, 005, 009); two are minor (GTF-007, 010). Issues already fixed in the Princeton version are not included.

### GTF-001: Compound NOT qualifiers become positive annotations

- **Location:** `lib/GO/AnnotationProvider/AnnotationParser.pm:583`.
- **Wrong behavior:** skips only a field equal to `NOT`, retaining valid pipe-separated fields such as `NOT|contributes_to` and `NOT|involved_in`.
- **Repro:** Two negated annotations to GO:0000011 produce a positive enrichment result, p = 1/190 = 0.00526315789473685. Correct output contains no result for that term. The two genes also have positive annotations to a different term, so their background membership is unchanged.
- **Fix:** match `NOT` as a complete pipe-delimited token. Positive annotations and bare NOT controls retain their behavior. This is a modern-GAF compatibility defect; the release's documentation predates those formats.
- **Reason / independent check:** [GAF 2.1, column 4](https://geneontology.org/docs/go-annotation-file-gaf-format-2.1/#qualifier-column-4), [GAF 2.2, relation/negation](https://geneontology.org/docs/go-annotation-file-gaf-format-2.2/#relation-column-4). Python splits the field into tokens before constructing annotation sets. Both qualifier orders and GAF 2.2 negation were checked.
- **Effect:** negative biological evidence can become apparently significant positive enrichment. **Confidence: high.**

### GTF-004: Tied p-values have different FDR estimates at the same cutoff

- **Location:** `lib/GO/TermFinder.pm:1977–2012`.
- **Wrong behavior:** divides expected null discoveries by array rank `i+1`; a cutoff at a tied p-value includes every tied hypothesis, not just the first members of the tie.
- **Repro:** Two identical annotation sets yield p = 1/6. With 50 explicitly enumerated draws, average null discoveries = 0.5. Original FDRs: 0.5 and 0.25. Correct: 0.25 and 0.25. With the unchanged standard sampler and seed 17: original 0.44/0.22, corrected 0.22/0.22.
- **Fix:** use the last rank of the tie for both the FDR denominator and the reported expected false positives; scan tie endpoints once. Non-tied FDR control is unchanged.
- **Reason / independent check:** [Boyle et al. 2004](https://web.stanford.edu/group/sherlocklab/pdfs/TERMFINDER_BOYLE_BIOINFORMATICS_2004.pdf), package documentation `TermFinder.pm:473–480, 573–578`: count real hypotheses as good or better than the cutoff. Python recomputes all null p-values from each recorded draw, then counts all real hypotheses at the cutoff.
- **Effect:** reported FDR depends on GO-ID tie ordering and can be inflated for early members of a tie. **Confidence: high.** This package implements a simulation estimator, not BH; replacing it with BH would change the method.

### GTF-005: Duplicate background names/aliases bias simulation sampling

- **Location:** `lib/GO/TermFinder.pm:1774`.
- **Wrong behavior:** background counts resolve and de-duplicate gene IDs, but the simulation pool uses the raw supplied names. A gene listed by ID and alias occupies two sampling slots; nominal two-gene draws can collapse to one gene.
- **Repro:** Four biological genes, but raw population `[g1, alias1, g2, g3, g4]`, where alias1 = g1. Under exhaustive index-subset cycles, corrected p changes from 300/1000 = 0.300 to 333/1000 = 0.333; FDR changes from 0.300 to 0.340 for the prescribed 50 draws. Exact uniform-subset null probability is 2/C(4,2) = 1/3. The finite 50/1000-draw values are not claimed to equal the limiting probability.
- **Fix:** build the sampling pool using the same ID resolution and de-duplication used for background counts.
- **Reason / independent check:** [Boyle et al. 2004](https://web.stanford.edu/group/sherlocklab/pdfs/TERMFINDER_BOYLE_BIOINFORMATICS_2004.pdf): simulations sample gene sets from the background. Python independently enumerates subsets of four distinct genes. With the unchanged random sampler and seed 17, corrected p is 0.308 before and 0.329 after; the patched output exactly matches the canonical unique-ID population. Unique-background normal control is unchanged.
- **Effect:** simulation-corrected p-values and FDR can depend on redundant spellings in the background. This differs from the index-sampling algorithm bias fixed in 0.83. **Confidence: high.**

### GTF-007 (minor): Obsolete status depends on tag order

- **Location:** `lib/GO/OntologyProvider/OboParser.pm:310, 320`.
- **Wrong behavior:** `namespace` resets validity to true, resurrecting a term whose earlier tag was `is_obsolete: true`.
- **Repro:** Original `nodeFromId('GO:0000011')` returns an obsolete node. Correct: absent; the live root and other term remain present.
- **Fix:** retain a separate obsolete flag until the next term stanza. Conventionally ordered obsolete terms continue to be excluded.
- **Reason / independent check:** [OBO 1.2, is_obsolete and serializer conventions](https://owlcollab.github.io/oboformat/doc/GO.format.obo-1_2.html). Parser acceptance must not depend on suggested serializer tag order. Python collects all stanza tags before filtering obsolete terms.
- **Effect:** obsolete terms can enter the graph and enrichment analysis with valid alternative tag layouts. **Confidence: high.**

### GTF-009: Typedef stanzas terminate the entire ontology parse

- **Location:** `lib/GO/OntologyProvider/OboParser.pm:285`.
- **Wrong behavior:** stops at the first `[Typedef]`, ignoring all later terms.
- **Repro:** Put a valid `part_of` definition before the terms. Original: all three queried nodes absent. Correct: all three present, with the same GO graph as when the definition is last.
- **Fix:** finish the preceding term and skip non-term stanza contents, then resume at the next term; do not stop parsing the file.
- **Reason / independent check:** [OBO 1.2, stanza conventions](https://owlcollab.github.io/oboformat/doc/GO.format.obo-1_2.html) actually recommends typedefs before terms. Python discovers term stanzas independently of typedef placement.
- **Effect:** a correctly formatted ontology can load as an empty or incomplete graph. **Confidence: high.**

### GTF-010 (minor): Cyclic ontology input causes uncontrolled recursion

- **Location:** `lib/GO/OntologyProvider/OboParser.pm:616–630`.
- **Wrong behavior:** recursively extends paths without detecting revisited nodes.
- **Repro:** GO:0000011 is_a GO:0000012 and vice versa. Original warns of deep recursion and returns no result before the 0.5-second watchdog kills it. Patched: promptly exits nonzero with `Cycle in ontology involving ...`.
- **Fix:** reject a path that revisits its originating node or an existing ancestor.
- **Reason / independent check:** [Boyle et al. 2004](https://web.stanford.edu/group/sherlocklab/pdfs/TERMFINDER_BOYLE_BIOINFORMATICS_2004.pdf) requires a DAG; [OBO parser requirements](https://owlcollab.github.io/oboformat/doc/GO.format.obo-1_2.html) require graceful failure. A separate Python DFS detects the cycle directly from the edge list. The valid diamond-DAG output is byte-identical.
- **Effect:** malformed user ontologies can hang or exhaust resources instead of producing a useful rejection. This is an invalid-input robustness defect, not a wrong p-value on a valid GO DAG. **Confidence: high.**

### References

- [Boyle et al. (2004). GO::TermFinder: open source software for accessing Gene Ontology information and finding significantly enriched Gene Ontology terms associated with a list of genes.](https://doi.org/10.1093/bioinformatics/bth456)
- [GO::TermFinder 0.86 on CPAN](https://metacpan.org/release/SHERLOCK/GO-TermFinder-0.86).
- [GAF 2.1](https://geneontology.org/docs/go-annotation-file-gaf-format-2.1/) and [GAF 2.2](https://geneontology.org/docs/go-annotation-file-gaf-format-2.2/).
- [OBO format 1.2](https://owlcollab.github.io/oboformat/doc/GO.format.obo-1_2.html).

---

# References

- omarwagih/rmotifx: [Wagih et al. (2016). Uncovering phosphorylation-based specificities through functional interaction networks.](https://doi.org/10.1074/mcp.M115.052357)
- evocellnet/funscoR: [Ochoa et al. (2020). The functional landscape of the human phosphoproteome.](https://doi.org/10.1038/s41587-019-0344-3)
- evocellnet/ksea: [Ochoa et al. (2016). An atlas of human kinase regulation.](https://doi.org/10.15252/msb.20167295)
- evocellnet/ptm_hotspots: [Strumillo et al. (2018). Conserved phosphorylation hotspots in eukaryotic protein domain families (preprint).](https://doi.org/10.1101/391185)
- bentoayr/Efficient-Projection-onto-the-Perfect-Phylogeny-Model: [Jia et al. (2018). Efficient Projection onto the Perfect Phylogeny Model.](https://doi.org/10.48550/arXiv.1811.01129)
- edbosne/pyfdd: [David-Bosne et al. (2024). Electron Emission Channeling for lattice location of radioactive isotopes in single crystals: Improvements from a Timepix3 quad detector and new PyFDD data analysis software.](https://doi.org/10.1016/j.nima.2023.169016)
- borenstein-lab/MUSiCC: [Manor and Borenstein (2015). MUSiCC: a marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome.](https://doi.org/10.1186/s13059-015-0610-8)
- borenstein-lab/mimosa2: [Noecker et al. (2022). MIMOSA2: a metabolic network-based tool for inferring mechanism-supported relationships in microbiome-metabolome data.](https://doi.org/10.1093/bioinformatics/btac003)
- borenstein-lab/MAAMOUL: [Muller, Baum and Borenstein (2026). MAAMOUL: metabolic network-based discovery of microbiome-metabolome shifts in disease.](https://doi.org/10.1093/bioinformatics/btag467)
- glarue/intronIC: [Moyer et al. (2020). Comprehensive database and evolutionary dynamics of U12-type introns.](https://doi.org/10.1093/nar/gkaa464)
- feedzai/deccaf: [Alves et al. (2024). Cost-Sensitive Learning to Defer to Multiple Experts with Workload Constraints.](https://doi.org/10.48550/arXiv.2403.06906)
- weissmanlab/magic: [Weissman and Hallatschek (2017). Minimal-assumption inference from population-genomic data.](https://doi.org/10.7554/eLife.24836)
- GO::TermFinder: [Boyle et al. (2004). GO::TermFinder: open source software for accessing Gene Ontology information and finding significantly enriched Gene Ontology terms associated with a list of genes.](https://doi.org/10.1093/bioinformatics/bth456)
- pyglmnet: [Jas et al. (2020). Pyglmnet: Python implementation of elastic-net regularized generalized linear models.](https://doi.org/10.21105/joss.01959)
