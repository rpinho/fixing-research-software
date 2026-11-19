# fixing-research-software

![Fixing research software](assets/banner.png)

AI agents look for correctness bugs in open-source research software. A separate referee rebuilds each claim from scratch. Only bugs the referee confirms are listed here. Each bug was reported to the authors before it appears here.

This is the one place for our work on other people's research code: the refereed bug reports in the table below, and every pull request we opened, grouped by field, in [Pull requests](#pull-requests), and small tools we built in [Tools we built](#tools-we-built). The name follows Valerio Capraro's [Fixing humanity's scientific knowledge](https://x.com/ValerioCapraro/status/2123070148743512573) project, which uses AI agents to review and correct published papers. This repo is about the code those papers depend on.

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

## Pull requests

Every pull request we opened on someone else's research code, rendered from the GitHub API by `tools/render_prs.py` and refreshed daily. Bug fixes were confirmed by a referee from a different model family, with a test that fails before the fix; speedups were checked for identical outputs. "Replies" counts maintainers' comments and reviews, not bots.

<!-- auto:prs -->
229 PRs to 61 repositories: 25 merged, 185 open, 19 closed.

### Biology

102 PRs to 32 repositories: 12 merged, 88 open, 2 closed.

| Repo | PR | Type | What it does | Status |
| --- | --- | --- | --- | --- |
| [adaptyvbio/protein-design-skills](https://github.com/adaptyvbio/protein-design-skills) | [#10](https://github.com/adaptyvbio/protein-design-skills/pull/10) | bug fix | The UniProt skill's PDB helper puts the chains, not the resolution, in its chains field | open |
| [adaptyvbio/protein-design-skills](https://github.com/adaptyvbio/protein-design-skills) | [#11](https://github.com/adaptyvbio/protein-design-skills/pull/11) | bug fix | The setup check uses modal token info, since modal token show does not exist | open |
| [Arcadia-Science/agentic-pymol](https://github.com/Arcadia-Science/agentic-pymol) | [#18](https://github.com/Arcadia-Science/agentic-pymol/pull/18) | bug fix | get_model works against real PyMOL (Indexed was imported from the wrong module) | merged 2026-11-16 |
| [Arcadia-Science/agentic-pymol](https://github.com/Arcadia-Science/agentic-pymol) | [#19](https://github.com/Arcadia-Science/agentic-pymol/pull/19) | bug fix | Relative file paths are resolved by PyMOL, as documented, not by the MCP server | open |
| [Arcadia-Science/agentic-pymol](https://github.com/Arcadia-Science/agentic-pymol) | [#21](https://github.com/Arcadia-Science/agentic-pymol/pull/21) | bug fix | types: drop slots from tool result dataclasses so FastMCP publishes output schemas | open |
| [Arcadia-Science/glass-box-umap](https://github.com/Arcadia-Science/glass-box-umap) | [#34](https://github.com/Arcadia-Science/glass-box-umap/pull/34) | bug fix | Float64 Tensor input works in transform and compute_contributions, like NumPy input | open |
| [Arcadia-Science/glass-box-umap](https://github.com/Arcadia-Science/glass-box-umap) | [#35](https://github.com/Arcadia-Science/glass-box-umap/pull/35) | tool | py.typed marker so type checkers use the package's annotations (issue #18) | open |
| [ArcInstitute/cell-eval](https://github.com/ArcInstitute/cell-eval) | [#248](https://github.com/ArcInstitute/cell-eval/pull/248) | bug fix | score_agg_metrics works when one normalization group is empty | open |
| [ArcInstitute/cell-eval](https://github.com/ArcInstitute/cell-eval) | [#249](https://github.com/ArcInstitute/cell-eval/pull/249) | bug fix | Pipeline metric settings no longer leak into other pipelines' defaults | open |
| [ArcInstitute/cell-eval](https://github.com/ArcInstitute/cell-eval) | [#250](https://github.com/ArcInstitute/cell-eval/pull/250) | speedup | sparse pseudobulk and centroids without densifying (3x faster, 4.8x less memory) | open |
| [ArcInstitute/evo2](https://github.com/ArcInstitute/evo2) | [#236](https://github.com/ArcInstitute/evo2/pull/236) | bug fix | An interrupted shard merge no longer leaves a truncated checkpoint that later loads accept | open |
| [ArcInstitute/state](https://github.com/ArcInstitute/state) | [#283](https://github.com/ArcInstitute/state/pull/283) | bug fix | Gene mapping uses the detected gene-name column, so genes named only there aren't dropped | open |
| [bioio-devs/bioio](https://github.com/bioio-devs/bioio) | [#236](https://github.com/bioio-devs/bioio/pull/236) | bug fix | bugfix/preserve-xarray-metadata | open |
| [biotite-dev/biotite](https://github.com/biotite-dev/biotite) | [#1037](https://github.com/biotite-dev/biotite/pull/1037) | bug fix | Fix `check_in_box()` returning atoms inside the box | open |
| [biotite-dev/biotite](https://github.com/biotite-dev/biotite) | [#1038](https://github.com/biotite-dev/biotite/pull/1038) | bug fix | Reject GRO stacks with unequal model lengths | open |
| [biotite-dev/biotite](https://github.com/biotite-dev/biotite) | [#1039](https://github.com/biotite-dev/biotite/pull/1039) | bug fix | Fix GFF annotation grouping for discontinuous features | open |
| [biotite-dev/biotite](https://github.com/biotite-dev/biotite) | [#1040](https://github.com/biotite-dev/biotite/pull/1040) | bug fix | Fix `to_sequence()` chain selection for atom array stacks | open |
| [chaidiscovery/chai-lab](https://github.com/chaidiscovery/chai-lab) | [#437](https://github.com/chaidiscovery/chai-lab/pull/437) | bug fix | Merging A3M files from the same database keeps every file's hits | open |
| [chaidiscovery/chai-lab](https://github.com/chaidiscovery/chai-lab) | [#438](https://github.com/chaidiscovery/chai-lab/pull/438) | bug fix | Template lookup keeps chain names like 001 or NA as strings | open |
| [daler/pybedtools](https://github.com/daler/pybedtools) | [#434](https://github.com/daler/pybedtools/pull/434) | bug fix | preserve input rows when indexing presorted files | open |
| [daler/pybedtools](https://github.com/daler/pybedtools) | [#435](https://github.com/daler/pybedtools/pull/435) | bug fix | fix generator completion in randomstats | open |
| [daler/pybedtools](https://github.com/daler/pybedtools) | [#436](https://github.com/daler/pybedtools/pull/436) | bug fix | accept pathlib paths in intersection database lists | open |
| [daler/pybedtools](https://github.com/daler/pybedtools) | [#437](https://github.com/daler/pybedtools/pull/437) | bug fix | preserve mate position 1 when iterating over BAM | open |
| [daler/pybedtools](https://github.com/daler/pybedtools) | [#438](https://github.com/daler/pybedtools/pull/438) | speedup | count BAM and CRAM records without converting intervals | open |
| [deeptools/deepTools](https://github.com/deeptools/deepTools) | [#1502](https://github.com/deeptools/deepTools/pull/1502) | bug fix | fix: keep computeMatrix groups distinct when filenames match | open |
| [deeptools/deepTools](https://github.com/deeptools/deepTools) | [#1503](https://github.com/deeptools/deepTools/pull/1503) | bug fix | fix: apply zero thresholds in computeMatrix | open |
| [deeptools/deepTools](https://github.com/deeptools/deepTools) | [#1504](https://github.com/deeptools/deepTools/pull/1504) | bug fix | fix: score singleton and two-row heatmap clusters correctly | open |
| [deeptools/deepTools](https://github.com/deeptools/deepTools) | [#1505](https://github.com/deeptools/deepTools/pull/1505) | bug fix | fix: preserve missing signal when clustering heatmaps | open |
| [deeptools/deepTools](https://github.com/deeptools/deepTools) | [#1506](https://github.com/deeptools/deepTools/pull/1506) | bug fix | fix: write final zero-valued bigwigCompare intervals | open |
| [deeptools/deepTools](https://github.com/deeptools/deepTools) | [#1507](https://github.com/deeptools/deepTools/pull/1507) | speedup | perf: average bigWig coverage bins in NumPy | open |
| [EdisonScientific/labbench2](https://github.com/EdisonScientific/labbench2) | [#45](https://github.com/EdisonScientific/labbench2/pull/45) | bug fix | Leading-decimal answers like `.701` keep their value when graded | merged 2026-11-16 |
| [EdisonScientific/labbench2](https://github.com/EdisonScientific/labbench2) | [#46](https://github.com/EdisonScientific/labbench2/pull/46) | bug fix | Report summaries keep metrics whose scores are all 0 | merged 2026-11-16 |
| [EdisonScientific/labbench2](https://github.com/EdisonScientific/labbench2) | [#48](https://github.com/EdisonScientific/labbench2/pull/48) | bug fix | custom runner outputs crash after generation (OSError) | merged 2026-11-17 |
| [EdisonScientific/labbench2](https://github.com/EdisonScientific/labbench2) | [#49](https://github.com/EdisonScientific/labbench2/pull/49) | bug fix | --retry-from ignores the original agent/mode; merges mix configurations | merged 2026-11-17 |
| [EdisonScientific/labbench2](https://github.com/EdisonScientific/labbench2) | [#50](https://github.com/EdisonScientific/labbench2/pull/50) | bug fix | Grade plain Wallace-rule answers with the Wallace formula | open |
| [EdisonScientific/labbench2](https://github.com/EdisonScientific/labbench2) | [#51](https://github.com/EdisonScientific/labbench2/pull/51) | bug fix | Use the attached Km unit for catalytic efficiency scoring | open |
| [eyurtsev/fcsparser](https://github.com/eyurtsev/fcsparser) | [#81](https://github.com/eyurtsev/fcsparser/pull/81) | bug fix | Fix the ANALYSIS segment end offset | open |
| [latchbio/latch](https://github.com/latchbio/latch) | [#624](https://github.com/latchbio/latch/pull/624) | bug fix | Glob patterns match the whole file name (`*.fq` no longer matches `a.fq.gz`) | open |
| [latchbio/latch](https://github.com/latchbio/latch) | [#625](https://github.com/latchbio/latch/pull/625) | bug fix | `generate-metadata` handles nf-core schema patterns that crashed it (55 to 124 of 146 pipelines) | open |
| [latchbio/latch](https://github.com/latchbio/latch) | [#626](https://github.com/latchbio/latch/pull/626) | bug fix | launch: send false Nextflow flags and pick the File/Dir union variant by type | open |
| [latchbio/latch](https://github.com/latchbio/latch) | [#627](https://github.com/latchbio/latch/pull/627) | bug fix | file_glob: put a slash between remote_directory and the file name | open |
| [latchbio/scbench](https://github.com/latchbio/scbench) | [#8](https://github.com/latchbio/scbench/pull/8) | bug fix | scbench batch skips evals/manifest.json instead of counting it as a failed eval | open |
| [levitsky/pyteomics](https://github.com/levitsky/pyteomics) | [#238](https://github.com/levitsky/pyteomics/pull/238) | bug fix | Write MGF retention-time ranges | open |
| [levitsky/pyteomics](https://github.com/levitsky/pyteomics) | [#239](https://github.com/levitsky/pyteomics/pull/239) | bug fix | Apply fixed ProForma modifications at the specified terminus | open |
| [levitsky/pyteomics](https://github.com/levitsky/pyteomics) | [#240](https://github.com/levitsky/pyteomics/pull/240) | bug fix | Check spectrum IDs in MzMLb membership tests | open |
| [levitsky/pyteomics](https://github.com/levitsky/pyteomics) | [#241](https://github.com/levitsky/pyteomics/pull/241) | bug fix | Use the charge state passed to ProForma.composition | open |
| [levitsky/pyteomics](https://github.com/levitsky/pyteomics) | [#242](https://github.com/levitsky/pyteomics/pull/242) | bug fix | Keep PSM identities when streaming FDR-filtered results | open |
| [levitsky/pyteomics](https://github.com/levitsky/pyteomics) | [#243](https://github.com/levitsky/pyteomics/pull/243) | speedup | Reuse log-factorials in q-value correction | open |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | [#2236](https://github.com/mdtraj/mdtraj/pull/2236) | bug fix | Resolve mmCIF connections using label identifiers | open |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | [#2237](https://github.com/mdtraj/mdtraj/pull/2237) | bug fix | Apply atom selection after reading ARC topology | open |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | [#2238](https://github.com/mdtraj/mdtraj/pull/2238) | bug fix | Continue default XTC and TRR frame numbers across writes | open |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | [#2239](https://github.com/mdtraj/mdtraj/pull/2239) | bug fix | Restore integral bond orders when reading HDF5 topology | open |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | [#2240](https://github.com/mdtraj/mdtraj/pull/2240) | bug fix | Use written atom serials in PDB CONECT records | open |
| [mdtraj/mdtraj](https://github.com/mdtraj/mdtraj) | [#2241](https://github.com/mdtraj/mdtraj/pull/2241) | speedup | Build and reduce contact distance groups in bulk | open |
| [MultiQC/MultiQC](https://github.com/MultiQC/MultiQC) | [#3736](https://github.com/MultiQC/MultiQC/pull/3736) | bug fix | A module set only in top_modules no longer runs a second time on all logs | open |
| [MultiQC/MultiQC](https://github.com/MultiQC/MultiQC) | [#3738](https://github.com/MultiQC/MultiQC/pull/3738) | bug fix | Fix grouped sample values in get_general_stats_data | open |
| [MultiQC/MultiQC](https://github.com/MultiQC/MultiQC) | [#3739](https://github.com/MultiQC/MultiQC/pull/3739) | bug fix | Fix module and data-key selection in get_module_data | open |
| [MultiQC/MultiQC](https://github.com/MultiQC/MultiQC) | [#3740](https://github.com/MultiQC/MultiQC/pull/3740) | bug fix | Preserve section order when merging parquet reports | open |
| [nf-core/tools](https://github.com/nf-core/tools) | [#4619](https://github.com/nf-core/tools/pull/4619) | bug fix | create-params-file includes parameters defined at the schema's top level | open, 6 replies |
| [nf-core/tools](https://github.com/nf-core/tools) | [#4620](https://github.com/nf-core/tools/pull/4620) | bug fix | Schema build keeps 0 and 0.0 defaults from the pipeline config | merged 2026-11-18 |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1637](https://github.com/nipy/nibabel/pull/1637) | bug fix | BF: Use output position when slicing frames of an ECAT array proxy | open, 1 reply |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1638](https://github.com/nipy/nibabel/pull/1638) | bug fix | BF: Read AFNI complex sub-bricks as complex64 | merged 2026-11-19 |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1639](https://github.com/nipy/nibabel/pull/1639) | bug fix | BF: Reverse slice timing when reorientation flips the slice axis | open |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1640](https://github.com/nipy/nibabel/pull/1640) | speedup | ENH: Write TCK streamlines in blocks when no affine needs applying | open |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1641](https://github.com/nipy/nibabel/pull/1641) | bug fix | BF: Accept MGH files with an intent code in the version field | open |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1642](https://github.com/nipy/nibabel/pull/1642) | bug fix | BF: Align annotation names with colour table rows when entries are missing | open |
| [nipy/nibabel](https://github.com/nipy/nibabel) | [#1643](https://github.com/nipy/nibabel/pull/1643) | bug fix | BF: Reshape GIFTI MatrixData to 4x4 when values are on one line | merged 2026-11-19 |
| [NVIDIA-BioNeMo/bionemo-recipes](https://github.com/NVIDIA-BioNeMo/bionemo-recipes) | [#1802](https://github.com/NVIDIA-BioNeMo/bionemo-recipes/pull/1802) | bug fix | ESM-2 PEFT validation packing uses val_micro_batch_size | open |
| [open2c/cooler](https://github.com/open2c/cooler) | [#544](https://github.com/open2c/cooler/pull/544) | bug fix | Apply divisive weights in cooler dump | open |
| [open2c/cooler](https://github.com/open2c/cooler) | [#545](https://github.com/open2c/cooler/pull/545) | bug fix | Write the dump header for empty queries | open |
| [open2c/cooler](https://github.com/open2c/cooler) | [#546](https://github.com/open2c/cooler/pull/546) | bug fix | Decode contig names in joined pixels | open |
| [open2c/cooler](https://github.com/open2c/cooler) | [#547](https://github.com/open2c/cooler/pull/547) | speedup | Read the row index for the queried matrix range | open |
| [pyranges/pyranges0](https://github.com/pyranges/pyranges0) | [#413](https://github.com/pyranges/pyranges0/pull/413) | bug fix | Preserve strandedness after a DataFrame round trip | merged 2026-11-19 |
| [pyranges/pyranges0](https://github.com/pyranges/pyranges0) | [#414](https://github.com/pyranges/pyranges0/pull/414) | bug fix | Respect as_df and nrows when reading GTF with full=False | open |
| [pyranges/pyranges1](https://github.com/pyranges/pyranges1) | [#216](https://github.com/pyranges/pyranges1/pull/216) | bug fix | Honor grouping columns in overlap counts | open |
| [pyranges/pyranges1](https://github.com/pyranges/pyranges1) | [#217](https://github.com/pyranges/pyranges1/pull/217) | bug fix | Preserve VCF filter status | open |
| [pysam-developers/pysam](https://github.com/pysam-developers/pysam) | [#1431](https://github.com/pysam-developers/pysam/pull/1431) | bug fix | Allow VariantRecord POS=0 (start=-1), as used for telomeres | open |
| [scikit-bio/scikit-bio](https://github.com/scikit-bio/scikit-bio) | [#2676](https://github.com/scikit-bio/scikit-bio/pull/2676) | speedup | PERF: slice positions from stacked bytes in TabularMSA.iter_positions | open |
| [scikit-bio/scikit-bio](https://github.com/scikit-bio/scikit-bio) | [#2677](https://github.com/scikit-bio/scikit-bio/pull/2677) | bug fix | BUG: accept a sparse basis in ilr and ilr_inv | open |
| [scikit-bio/scikit-bio](https://github.com/scikit-bio/scikit-bio) | [#2678](https://github.com/scikit-bio/scikit-bio/pull/2678) | bug fix | BUG: drop gap columns across all sequences in AlignPath.to_indices | open |
| [scikit-bio/scikit-bio](https://github.com/scikit-bio/scikit-bio) | [#2679](https://github.com/scikit-bio/scikit-bio/pull/2679) | bug fix | BUG: update stored IDs in OrdinationResults.rename | open |
| [scikit-bio/scikit-bio](https://github.com/scikit-bio/scikit-bio) | [#2680](https://github.com/scikit-bio/scikit-bio/pull/2680) | bug fix | BUG: treat missing lengths as zero while climbing in root_at_midpoint | open |
| [scverse/scanpy](https://github.com/scverse/scanpy) | [#4531](https://github.com/scverse/scanpy/pull/4531) | bug fix | fix: match expression layers before reusing marker statistics | open |
| [scverse/scanpy](https://github.com/scverse/scanpy) | [#4532](https://github.com/scverse/scanpy/pull/4532) | bug fix | fix: keep legacy graph metrics usable without anndata.acc | open, 1 reply |
| [scverse/scanpy](https://github.com/scverse/scanpy) | [#4533](https://github.com/scverse/scanpy/pull/4533) | bug fix | fix: derive PCA defaults from the selected representation | open, 1 reply |
| [scverse/scanpy](https://github.com/scverse/scanpy) | [#4534](https://github.com/scverse/scanpy/pull/4534) | bug fix | fix: preserve gene pool alignment in score_genes | open |
| [seqeralabs/nf-metro](https://github.com/seqeralabs/nf-metro) | [#2172](https://github.com/seqeralabs/nf-metro/pull/2172) | bug fix | Converted metro maps keep edges into dead-end processes in other sections | open |
| [seqeralabs/nf-metro](https://github.com/seqeralabs/nf-metro) | [#2173](https://github.com/seqeralabs/nf-metro/pull/2173) | bug fix | Subworkflows with the same short name get separate sections instead of overwriting each other | open |
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | [#372](https://github.com/snap-stanford/Biomni/pull/372) | bug fix | FDA adverse-event summaries count deaths and hospitalizations from the report-level flags | merged 2026-11-16 |
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | [#373](https://github.com/snap-stanford/Biomni/pull/373) | bug fix | `query_openfda` sends its search, sort, count and skip parameters | merged 2026-11-16 |
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | [#376](https://github.com/snap-stanford/Biomni/pull/376) | bug fix | Drug recall search applies the requested classification filter | open |
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | [#377](https://github.com/snap-stanford/Biomni/pull/377) | bug fix | Adverse-event search reports FDA API errors instead of 'no adverse events found' | open |
| [snap-stanford/Biomni](https://github.com/snap-stanford/Biomni) | [#378](https://github.com/snap-stanford/Biomni/pull/378) | bug fix | database REST helper: timeouts and bounded GET retries | open |
| [synthesizebio/pysynthbio](https://github.com/synthesizebio/pysynthbio) | [#77](https://github.com/synthesizebio/pysynthbio/pull/77) | bug fix | `predict_query` no longer writes its options into the caller's query dict | open |
| [tskit-dev/msprime](https://github.com/tskit-dev/msprime) | [#2554](https://github.com/tskit-dev/msprime/pull/2554) | bug fix | Record SLiM mutation model parameters before simulation | open, 2 replies |
| [tskit-dev/msprime](https://github.com/tskit-dev/msprime) | [#2555](https://github.com/tskit-dev/msprime/pull/2555) | bug fix | Preserve initial tables when adding populations | open |
| [tskit-dev/msprime](https://github.com/tskit-dev/msprime) | [#2556](https://github.com/tskit-dev/msprime/pull/2556) | bug fix | Preserve population IDs in ancestry provenance | open |
| [tskit-dev/tskit](https://github.com/tskit-dev/tskit) | [#3510](https://github.com/tskit-dev/tskit/pull/3510) | bug fix | Stabilize trait correlation across trait scales | closed |
| [tskit-dev/tskit](https://github.com/tskit-dev/tskit) | [#3511](https://github.com/tskit-dev/tskit/pull/3511) | bug fix | Preserve edge and migration metadata when trimming | open |
| [tskit-dev/tskit](https://github.com/tskit-dev/tskit) | [#3512](https://github.com/tskit-dev/tskit/pull/3512) | bug fix | Use the converted site mask when validating VCF positions | open, 2 replies |
| [tskit-dev/tskit](https://github.com/tskit-dev/tskit) | [#3513](https://github.com/tskit-dev/tskit/pull/3513) | speedup | Avoid per-site copies when writing VCF | closed |
| [tskit-dev/tskit](https://github.com/tskit-dev/tskit) | [#3514](https://github.com/tskit-dev/tskit/pull/3514) | bug fix | Apply NEXUS node labels to alignment rows | merged 2026-11-19 |

### Physics and astronomy

53 PRs to 14 repositories: 5 merged, 43 open, 5 closed.

| Repo | PR | Type | What it does | Status |
| --- | --- | --- | --- | --- |
| [adrn/gala](https://github.com/adrn/gala) | [#680](https://github.com/adrn/gala/pull/680) | bug fix | Preserve mock stream metadata through HDF5 | open, 1 reply |
| [adrn/gala](https://github.com/adrn/gala) | [#681](https://github.com/adrn/gala/pull/681) | bug fix | Honor the median option for Staeckel focal lengths | open |
| [adrn/gala](https://github.com/adrn/gala) | [#682](https://github.com/adrn/gala/pull/682) | bug fix | Use elapsed time in fast Lyapunov estimates | open |
| [adrn/gala](https://github.com/adrn/gala) | [#683](https://github.com/adrn/gala/pull/683) | bug fix | Use the toy potential time unit when fitting O2GF frequencies | open, 1 reply |
| [adrn/gala](https://github.com/adrn/gala) | [#684](https://github.com/adrn/gala/pull/684) | speedup | Use matrix products for O2GF mode sums | open, 1 reply |
| [astropy/astropy](https://github.com/astropy/astropy) | [#20894](https://github.com/astropy/astropy/pull/20894) | bug fix | Fix sigma_clip rejection masks for Quantity input | closed |
| [astropy/astropy](https://github.com/astropy/astropy) | [#20895](https://github.com/astropy/astropy/pull/20895) | bug fix | Honor zero sigma bounds in SigmaClip | closed |
| [astropy/astropy](https://github.com/astropy/astropy) | [#20896](https://github.com/astropy/astropy/pull/20896) | bug fix | Fix array indexing of scalar Distribution | closed |
| [California-Planet-Search/radvel](https://github.com/California-Planet-Search/radvel) | [#464](https://github.com/California-Planet-Search/radvel/pull/464) | bug fix | Preserve the source basis when converting parameters | open |
| [California-Planet-Search/radvel](https://github.com/California-Planet-Search/radvel) | [#465](https://github.com/California-Planet-Search/radvel/pull/465) | bug fix | Use configured planet letters in dict-based fits | open |
| [California-Planet-Search/radvel](https://github.com/California-Planet-Search/radvel) | [#466](https://github.com/California-Planet-Search/radvel/pull/466) | bug fix | Keep the optimizer's returned fit parameters | open |
| [California-Planet-Search/radvel](https://github.com/California-Planet-Search/radvel) | [#467](https://github.com/California-Planet-Search/radvel/pull/467) | bug fix | Honor fixed jitter in information-criterion comparisons | open |
| [California-Planet-Search/radvel](https://github.com/California-Planet-Search/radvel) | [#468](https://github.com/California-Planet-Search/radvel/pull/468) | bug fix | Sort celerite observation times before initializing the kernel | open |
| [dfm/corner.py](https://github.com/dfm/corner.py) | [#355](https://github.com/dfm/corner.py/pull/355) | bug fix | Fix linestyle aliases in overplot_points | open |
| [dfm/corner.py](https://github.com/dfm/corner.py) | [#356](https://github.com/dfm/corner.py/pull/356) | bug fix | Restore variable selection with ArviZ 1.x | open |
| [dfm/corner.py](https://github.com/dfm/corner.py) | [#357](https://github.com/dfm/corner.py/pull/357) | bug fix | Align divergence markers with selected coordinates | open |
| [dfm/emcee](https://github.com/dfm/emcee) | [#588](https://github.com/dfm/emcee/pull/588) | bug fix | fix: keep autocorrelation error estimates in original steps | open |
| [exoplanet-dev/celerite2](https://github.com/exoplanet-dev/celerite2) | [#208](https://github.com/exoplanet-dev/celerite2/pull/208) | bug fix | Include GP means in PyMC and NumPyro samples | open |
| [exoplanet-dev/celerite2](https://github.com/exoplanet-dev/celerite2) | [#209](https://github.com/exoplanet-dev/celerite2/pull/209) | bug fix | Return negative infinity after quiet factorization failures | open |
| [exoplanet-dev/celerite2](https://github.com/exoplanet-dev/celerite2) | [#210](https://github.com/exoplanet-dev/celerite2/pull/210) | bug fix | Handle PyMC marginal sample sizes | open |
| [exoplanet-dev/celerite2](https://github.com/exoplanet-dev/celerite2) | [#211](https://github.com/exoplanet-dev/celerite2/pull/211) | bug fix | Reallocate non-owning workspaces after pickling | open |
| [healpy/healpy](https://github.com/healpy/healpy) | [#1152](https://github.com/healpy/healpy/pull/1152) | bug fix | Fix mmax handling in harmonic_ud_grade | open |
| [healpy/healpy](https://github.com/healpy/healpy) | [#1153](https://github.com/healpy/healpy/pull/1153) | bug fix | Fix string column names in write_map | open |
| [healpy/healpy](https://github.com/healpy/healpy) | [#1154](https://github.com/healpy/healpy/pull/1154) | bug fix | Fix ud_grade averaging with non-finite pixels | open |
| [joshspeagle/dynesty](https://github.com/joshspeagle/dynesty) | [#529](https://github.com/joshspeagle/dynesty/pull/529) | bug fix | fix iteration count for stopped merged runs | open |
| [joshspeagle/dynesty](https://github.com/joshspeagle/dynesty) | [#530](https://github.com/joshspeagle/dynesty/pull/530) | bug fix | fix information for zero reweighting factors | open |
| [joshspeagle/dynesty](https://github.com/joshspeagle/dynesty) | [#531](https://github.com/joshspeagle/dynesty/pull/531) | bug fix | fix strand IDs when merging independent runs | open |
| [lightkurve/lightkurve](https://github.com/lightkurve/lightkurve) | [#1595](https://github.com/lightkurve/lightkurve/pull/1595) | bug fix | Fixed local FITS time units for reordered columns | open |
| [lightkurve/lightkurve](https://github.com/lightkurve/lightkurve) | [#1596](https://github.com/lightkurve/lightkurve/pull/1596) | bug fix | Fixed stitching light curves with different time formats | open |
| [LSSTDESC/CCL](https://github.com/LSSTDESC/CCL) | [#1329](https://github.com/LSSTDESC/CCL/pull/1329) | bug fix | Reject negative neutrino masses | open |
| [LSSTDESC/CCL](https://github.com/LSSTDESC/CCL) | [#1330](https://github.com/LSSTDESC/CCL/pull/1330) | bug fix | Fix comoving volume in curved cosmologies | open |
| [LSSTDESC/CCL](https://github.com/LSSTDESC/CCL) | [#1331](https://github.com/LSSTDESC/CCL/pull/1331) | bug fix | Include fc_bar in Duffy08 equality and representation | open |
| [LSSTDESC/CCL](https://github.com/LSSTDESC/CCL) | [#1332](https://github.com/LSSTDESC/CCL/pull/1332) | bug fix | Fix fourth-profile bias in the two-halo trispectrum | open |
| [openmc-dev/openmc](https://github.com/openmc-dev/openmc) | [#4240](https://github.com/openmc-dev/openmc/pull/4240) | bug fix | Reshape each mesh filter along its expanded axes | open |
| [openmc-dev/openmc](https://github.com/openmc-dev/openmc) | [#4241](https://github.com/openmc-dev/openmc/pull/4241) | bug fix | Read matrix rotations from mesh filters through the C API | merged 2026-11-19 |
| [openmc-dev/openmc](https://github.com/openmc-dev/openmc) | [#4242](https://github.com/openmc-dev/openmc/pull/4242) | bug fix | Scale shared mesh sources once when setting total strength | merged 2026-11-19 |
| [openmc-dev/openmc](https://github.com/openmc-dev/openmc) | [#4243](https://github.com/openmc-dev/openmc/pull/4243) | bug fix | Preserve mesh identity and transformations when comparing filters | merged 2026-11-19 |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#802](https://github.com/Quandela/Perceval/pull/802) | bug fix | Make BSDistribution(bsd) copy the source distribution | open |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#803](https://github.com/Quandela/Perceval/pull/803) | bug fix | Validate each iteration of a ComputationIterator | open, 1 reply |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#804](https://github.com/Quandela/Perceval/pull/804) | bug fix | Set ERROR status when execute_sync fails with allow_partial_results | open, 1 reply |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#805](https://github.com/Quandela/Perceval/pull/805) | bug fix | Reset the Processor source when its noise model is changed | open, 2 replies |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#806](https://github.com/Quandela/Perceval/pull/806) | bug fix | Fix result insertion for a ComputationIterator without iteration | open |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#807](https://github.com/Quandela/Perceval/pull/807) | bug fix | Fix serialization of detectors without a name | closed |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#808](https://github.com/Quandela/Perceval/pull/808) | bug fix | Keep min_detected_photons_filter(0) through experiment serialization | open, 1 reply |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#809](https://github.com/Quandela/Perceval/pull/809) | speedup | Do not copy the experiment in use_phase_noise when there is no phase noise | merged 2026-11-19 |
| [Quandela/Perceval](https://github.com/Quandela/Perceval) | [#810](https://github.com/Quandela/Perceval/pull/810) | speedup | Compute numeric circuit unitaries by updating row blocks | merged 2026-11-19 |
| [sunpy/sunpy](https://github.com/sunpy/sunpy) | [#8919](https://github.com/sunpy/sunpy/pull/8919) | bug fix | Fixes CROTA fallback for EUI maps | closed |
| [sunpy/sunpy](https://github.com/sunpy/sunpy) | [#8924](https://github.com/sunpy/sunpy/pull/8924) | bug fix | Fixes WCS construction for FITS maps with SIP distortion | open, 1 reply |
| [tenpy/tenpy](https://github.com/tenpy/tenpy) | [#779](https://github.com/tenpy/tenpy/pull/779) | bug fix | Fix MPO expectation values with supplied environments | open, 1 reply |
| [tenpy/tenpy](https://github.com/tenpy/tenpy) | [#780](https://github.com/tenpy/tenpy/pull/780) | bug fix | Fix joint probabilities in MPS.sample_measurements | open, 1 reply |
| [tenpy/tenpy](https://github.com/tenpy/tenpy) | [#781](https://github.com/tenpy/tenpy/pull/781) | bug fix | Fix dropping charges on grouped sites of different dimensions | open, 2 replies |
| [tenpy/tenpy](https://github.com/tenpy/tenpy) | [#782](https://github.com/tenpy/tenpy/pull/782) | bug fix | Fix MPO construction for empty Hamiltonians | open, 1 reply |
| [tenpy/tenpy](https://github.com/tenpy/tenpy) | [#783](https://github.com/tenpy/tenpy/pull/783) | bug fix | Preserve Jordan-Wigner parity for grouped independent charges | open, 1 reply |

### Materials and chemistry

27 PRs to 7 repositories: 0 merged, 17 open, 10 closed.

| Repo | PR | Type | What it does | Status |
| --- | --- | --- | --- | --- |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4787](https://github.com/materialsproject/pymatgen/pull/4787) | speedup | ZSLGenerator: cache super-lattice reductions, vectorize match check (3.3-4.8x, byte-identical) | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4788](https://github.com/materialsproject/pymatgen/pull/4788) | bug fix | Fix GibbsComputedStructureEntry.from_dict for entries with a correction | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4789](https://github.com/materialsproject/pymatgen/pull/4789) | bug fix | Fix QuasiRRHO free-rotor interpolation using vibrational temperatures instead of wavenumbers | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4790](https://github.com/materialsproject/pymatgen/pull/4790) | bug fix | Fix MagneticStructureEnumerator crash when the ferromagnetic strategy is not used | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4791](https://github.com/materialsproject/pymatgen/pull/4791) | bug fix | Fix get_plot and plot_structures with two_theta_range=None | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4792](https://github.com/materialsproject/pymatgen/pull/4792) | bug fix | Fix XAS.stitch in XAFS mode when called on the EXAFS spectrum | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4793](https://github.com/materialsproject/pymatgen/pull/4793) | bug fix | Normalize data["volume"] per formula unit in InsertionVoltagePair | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4794](https://github.com/materialsproject/pymatgen/pull/4794) | bug fix | Fix get_dimensionality_cheon modifying the input structure when standardize=False | closed |
| [materialsproject/pymatgen](https://github.com/materialsproject/pymatgen) | [#4795](https://github.com/materialsproject/pymatgen/pull/4795) | bug fix | Return "intercalated ion" from get_dimensionality_cheon with larger_cell=True | closed |
| [phonopy/phonopy](https://github.com/phonopy/phonopy) | [#1118](https://github.com/phonopy/phonopy/pull/1118) | bug fix | Fix empty arguments in deprecated option name handling | open, 1 reply |
| [phonopy/phonopy](https://github.com/phonopy/phonopy) | [#1119](https://github.com/phonopy/phonopy/pull/1119) | bug fix | Fix loading YAML with a NumPy primitive matrix | open |
| [phonopy/phonopy](https://github.com/phonopy/phonopy) | [#1120](https://github.com/phonopy/phonopy/pull/1120) | bug fix | Preserve symbol distinction when replicating Phonopy | open |
| [phonopy/phonopy](https://github.com/phonopy/phonopy) | [#1121](https://github.com/phonopy/phonopy/pull/1121) | speedup | Speed up thermal displacements by batching mode populations | open |
| [pybamm-team/PyBaMM](https://github.com/pybamm-team/PyBaMM) | [#6070](https://github.com/pybamm-team/PyBaMM/pull/6070) | bug fix | fix: preserve skip_ok on repeated experiment steps | open |
| [pybamm-team/PyBaMM](https://github.com/pybamm-team/PyBaMM) | [#6072](https://github.com/pybamm-team/PyBaMM/pull/6072) | bug fix | fix: keep EIS input ordering stable across solves | open, 1 reply |
| [pybamm-team/PyBaMM](https://github.com/pybamm-team/PyBaMM) | [#6073](https://github.com/pybamm-team/PyBaMM/pull/6073) | bug fix | fix: search experiment tags with string steps | open |
| [rowansci/openconf](https://github.com/rowansci/openconf) | [#19](https://github.com/rowansci/openconf/pull/19) | bug fix | Heavy-atom RMSD searches symmetry mappings, so symmetric conformers compare as identical | open |
| [rowansci/openconf](https://github.com/rowansci/openconf) | [#20](https://github.com/rowansci/openconf/pull/20) | bug fix | random_seed=0 gives reproducible conformers instead of an unseeded run | open |
| [rowansci/openconf](https://github.com/rowansci/openconf) | [#21](https://github.com/rowansci/openconf/pull/21) | bug fix | hybrid: pick low-mode source seeds from the pool after seed insertion | open |
| [rowansci/openconf](https://github.com/rowansci/openconf) | [#22](https://github.com/rowansci/openconf/pull/22) | bug fix | pool: apply energy_window_kcal to the final selection | open |
| [rowansci/rowan-python](https://github.com/rowansci/rowan-python) | [#19](https://github.com/rowansci/rowan-python/pull/19) | bug fix | Scan energy positions, explicit empty pKa element lists, and folder lookup past the first page | closed |
| [rowansci/steamroll](https://github.com/rowansci/steamroll) | [#8](https://github.com/rowansci/steamroll/pull/8) | bug fix | Transition-metal conversions keep input atom order and supplied coordinates | open |
| [rowansci/steamroll](https://github.com/rowansci/steamroll) | [#9](https://github.com/rowansci/steamroll/pull/9) | bug fix | to_rdkit: check transition-metal results against the supplied SMILES | open |
| [spglib/spglib](https://github.com/spglib/spglib) | [#650](https://github.com/spglib/spglib/pull/650) | bug fix | fix: preserve legacy Python error messages | open |
| [spglib/spglib](https://github.com/spglib/spglib) | [#651](https://github.com/spglib/spglib/pull/651) | bug fix | fix: identify magnetic groups in oblique primitive bases | open |
| [spglib/spglib](https://github.com/spglib/spglib) | [#652](https://github.com/spglib/spglib/pull/652) | bug fix | fix(fortran): forward stabilized reciprocal mesh arguments | open |
| [spglib/spglib](https://github.com/spglib/spglib) | [#653](https://github.com/spglib/spglib/pull/653) | speedup | perf: prune lattice symmetry candidates by axis length | open |

### Mathematics

26 PRs to 1 repository: 6 merged, 18 open, 2 closed.

| Repo | PR | Type | What it does | Status |
| --- | --- | --- | --- | --- |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#227](https://github.com/teorth/optimizationproblems/pull/227) | bug fix | C_86: improved upper bound 1.8117251* (Schur–Siegel–Smyth trace constant) | merged 2026-10-18 |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#229](https://github.com/teorth/optimizationproblems/pull/229) | bug fix | C_82: improved upper bound 0.2534449* (essential minimum of the Zhang–Zagier height) | merged 2026-10-18 |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#239](https://github.com/teorth/optimizationproblems/pull/239) | bug fix | C68: lower bound 0.432* for Korenblum’s constant (unrefereed) | merged 2026-10-26 |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#251](https://github.com/teorth/optimizationproblems/pull/251) | bug fix | C42: upper bound 0.6888863712* for Turan's pure power-sum constant (unrefereed) | merged 2026-10-26 |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#258](https://github.com/teorth/optimizationproblems/pull/258) | bug fix | C44: upper bound 4.3576549226* via a degree-three local-weight cap (unrefereed) | merged 2026-10-26 |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#259](https://github.com/teorth/optimizationproblems/pull/259) | bug fix | C70: finite lower bound 1.20194336* and cube-ball limit exp(1/(2e)) (unrefereed) | merged 2026-10-26 |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#294](https://github.com/teorth/optimizationproblems/pull/294) | bug fix | C44: candidate upper bound 1.9916994577* with R4 = 22, R6 <= 107 and R7 <= 227 (unrefereed) | open |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#298](https://github.com/teorth/optimizationproblems/pull/298) | bug fix | C86: upper bound 1.8054939963* with a refined rational density (unrefereed; AI-checked, no human review) | open, 2 replies |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#299](https://github.com/teorth/optimizationproblems/pull/299) | bug fix | C68: candidate lower bound 0.447* via a contact-row moment lemma (unrefereed) | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#300](https://github.com/teorth/optimizationproblems/pull/300) | bug fix | C10a: record Heilman-Jones-Malavolta 1.773 and Peng 1.77987164 (not my bounds) | open |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#301](https://github.com/teorth/optimizationproblems/pull/301) | bug fix | C82: upper bound 0.253091834* with new degree-44 denominators (unrefereed) | closed |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#305](https://github.com/teorth/optimizationproblems/pull/305) | bug fix | 42a: upper bound 0.6863607950* on Bakeas's Theorem A (unrefereed) | closed |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#306](https://github.com/teorth/optimizationproblems/pull/306) | bug fix | 91a: lower bound 0.265988* by canonical alignments, forbidden words and Walsh statistics (unrefereed) | open |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#307](https://github.com/teorth/optimizationproblems/pull/307) | bug fix | 89b: upper bound 0.001648970526* by a binary Cayley step graphon (unrefereed) | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#308](https://github.com/teorth/optimizationproblems/pull/308) | bug fix | 89c: lower bound 0.000033123924116* by exact flag-algebra certificates (unrefereed) | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#310](https://github.com/teorth/optimizationproblems/pull/310) | bug fix | 42a: explicit value 1/2 + 2^-4096* for Biró's strict lower bound (unrefereed) | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#311](https://github.com/teorth/optimizationproblems/pull/311) | bug fix | C57c: record Wikström's bounds and a candidate unrefereed 0.61230* lower bound | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#317](https://github.com/teorth/optimizationproblems/pull/317) | bug fix | C30: add candidate 10.42* lower bound conditional on Norton v3 (stacked on #313) | open, 2 replies |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#321](https://github.com/teorth/optimizationproblems/pull/321) | bug fix | C47: record Tomar's bounds and a candidate unrefereed 1.70311* lower bound | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#324](https://github.com/teorth/optimizationproblems/pull/324) | bug fix | C22b: candidate unrefereed upper bound 7.090412* via unequal superhelices | open |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#328](https://github.com/teorth/optimizationproblems/pull/328) | bug fix | C38: add candidate unrefereed 2.6275696* lower bound from span-18 bridges | open |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#330](https://github.com/teorth/optimizationproblems/pull/330) | bug fix | C82: candidate upper bound 0.2519696460* from a joint degree-104 certificate built on #280 v3, v4 and v5 (unrefereed) | open, 4 replies |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#347](https://github.com/teorth/optimizationproblems/pull/347) | bug fix | C22b: candidate limiting bound 7.087559024* (stacked on #342) | open |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#350](https://github.com/teorth/optimizationproblems/pull/350) | bug fix | C47: candidate lower bound 1.7055913150* (stacked on #341) | open, 2 replies |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#370](https://github.com/teorth/optimizationproblems/pull/370) | bug fix | 49a: candidate lower bound 1.5678643* from a 252303-set two-pendant block (Koshta's block, 21 sets replaced by 32) | open, 1 reply |
| [teorth/optimizationproblems](https://github.com/teorth/optimizationproblems) | [#373](https://github.com/teorth/optimizationproblems/pull/373) | bug fix | 8a: C8 = 2/log γ_1, a corollary of OpenAI's 7/8 quasi-Riemann hypothesis | open |

### General tools

21 PRs to 7 repositories: 2 merged, 19 open, 0 closed.

| Repo | PR | Type | What it does | Status |
| --- | --- | --- | --- | --- |
| [Future-House/aviary](https://github.com/Future-House/aviary) | [#393](https://github.com/Future-House/aviary/pull/393) | bug fix | Tool servers build for tools with list parameters (JSON Schema "array") | open |
| [Future-House/aviary](https://github.com/Future-House/aviary) | [#394](https://github.com/Future-House/aviary/pull/394) | bug fix | Tool servers pass a parameter's declared default when the request leaves it out | open |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | [#1373](https://github.com/Future-House/paper-qa/pull/1373) | bug fix | Text parsing compares page_size_limit with each line's length, not the line count | open |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | [#1374](https://github.com/Future-House/paper-qa/pull/1374) | bug fix | Rebuilding an index with use_absolute_paper_directory keeps unchanged documents | open |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | [#1375](https://github.com/Future-House/paper-qa/pull/1375) | speedup | reuse NumpyVectorStore matrix and norms across retrievals (70x warm, bit-identical) | open |
| [glm-tools/pyglmnet](https://github.com/glm-tools/pyglmnet) | [#399](https://github.com/glm-tools/pyglmnet/pull/399) | bug fix | FIX: Bernoulli log likelihood is NaN at probabilities 0 and 1, and overflows for large logits | merged 2026-11-08 |
| [glm-tools/pyglmnet](https://github.com/glm-tools/pyglmnet) | [#400](https://github.com/glm-tools/pyglmnet/pull/400) | bug fix | FIX: gamma deviance and pseudo-R2 omit the saturated log likelihood | open, 1 reply |
| [glm-tools/pyglmnet](https://github.com/glm-tools/pyglmnet) | [#401](https://github.com/glm-tools/pyglmnet/pull/401) | bug fix | FIX: simulate_glm(sample=True) for gamma returns exp(mu) instead of gamma samples | merged 2026-11-08 |
| [lmfit/lmfit-py](https://github.com/lmfit/lmfit-py) | [#1068](https://github.com/lmfit/lmfit-py/pull/1068) | bug fix | FIX: use component prefixes in eval_uncertainty | open, 1 reply |
| [lmfit/lmfit-py](https://github.com/lmfit/lmfit-py) | [#1069](https://github.com/lmfit/lmfit-py/pull/1069) | bug fix | FIX: handle sequence inputs with nan_policy='omit' | open, 1 reply |
| [lmfit/lmfit-py](https://github.com/lmfit/lmfit-py) | [#1070](https://github.com/lmfit/lmfit-py/pull/1070) | bug fix | FIX: preserve directories when loading saved models from Paths | open, 1 reply |
| [pymc-devs/pymc](https://github.com/pymc-devs/pymc) | [#8643](https://github.com/pymc-devs/pymc/pull/8643) | bug fix | Fix MultiTrace slicing counts and negative strides | open |
| [pymc-devs/pymc](https://github.com/pymc-devs/pymc) | [#8644](https://github.com/pymc-devs/pymc/pull/8644) | bug fix | Initialize variational groups in their variable order | open |
| [pymc-devs/pymc](https://github.com/pymc-devs/pymc) | [#8645](https://github.com/pymc-devs/pymc/pull/8645) | bug fix | Preserve dimension names in ZarrTrace without coordinate labels | open |
| [pymc-devs/pymc](https://github.com/pymc-devs/pymc) | [#8646](https://github.com/pymc-devs/pymc/pull/8646) | bug fix | Flatten start_sigma arrays when initializing ADVI | open |
| [pyro-ppl/numpyro](https://github.com/pyro-ppl/numpyro) | [#2440](https://github.com/pyro-ppl/numpyro/pull/2440) | bug fix | fix(infer): reject scanned sample sites in TraceEnum_ELBO | open, 2 replies |
| [pyro-ppl/numpyro](https://github.com/pyro-ppl/numpyro) | [#2441](https://github.com/pyro-ppl/numpyro/pull/2441) | bug fix | fix(distributions): keep two-sided TruncatedNormal samples within bounds | open, 2 replies |
| [pyro-ppl/numpyro](https://github.com/pyro-ppl/numpyro) | [#2442](https://github.com/pyro-ppl/numpyro/pull/2442) | bug fix | fix(infer): preserve PRNG implementations in Predictive | open, 4 replies |
| [robocurve/inspect-robots](https://github.com/robocurve/inspect-robots) | [#617](https://github.com/robocurve/inspect-robots/pull/617) | bug fix | Rollouts record a copy of each executed action, so a reused policy buffer can't change scores | open |
| [robocurve/inspect-robots](https://github.com/robocurve/inspect-robots) | [#618](https://github.com/robocurve/inspect-robots/pull/618) | bug fix | Trial artifacts stay separate for scene IDs that differ only in case | open |
| [robocurve/inspect-robots](https://github.com/robocurve/inspect-robots) | [#622](https://github.com/robocurve/inspect-robots/pull/622) | speedup | HTML report scans the frame directory once (16x faster, byte-identical) | open |
<!-- /auto -->

## Tools we built

Small libraries and pipelines built around the code we fix.

- [nudged-elastic-band](https://github.com/rpinho/nudged-elastic-band): climbing-image nudged elastic band in plain NumPy, MIT. It answers the NEB item on Rowan's [open-source projects we wish existed](https://www.rowansci.com/blog/open-source-projects-we-wish-existed). It matches ASE's improved-tangent CI-NEB + FIRE step for step. On 23 Baker25 reactions with GFN2-xTB, an independent referee verified a transition state for 7, the same 7 as ASE.
- [lab-instrument-data-pipeline](https://github.com/rpinho/lab-instrument-data-pipeline): a small pipeline on real public instrument files (flow cytometry, a plate reader, nanopore plasmid reads and OME-Zarr imaging), with lineage from every measurement to its raw bytes and five hands-on exercises. Its references link the parser fixes we sent upstream.

## How a bug gets in

The full rules, and the numbers so far, are in [METHOD.md](METHOD.md). The retro is [RETRO.md](RETRO.md).

Every bug in one file, with its report, reproduction and before/after output copied from the project folders: [PAPER.md](PAPER.md).

1. Hunt for a correctness bug in a pinned upstream version.
2. An independent referee rebuilds the claim from scratch.
3. Prepare a patch and a small before/after example.
4. Check normal inputs and record the limits of the fix.

## References

- Valerio Capraro (2026). [Fixing humanity's scientific knowledge](https://x.com/ValerioCapraro/status/2123070148743512573), project launch.
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
