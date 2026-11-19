#!/bin/zsh
# Re-render the PR tables from the GitHub API and push whichever README changed:
# fixing-research-software (all fields), ai-biology (biology rows) and ai-physics (physics link and counts).
# Run after new PRs (open_pr.sh appends to tools/prs.tsv) and daily by launchd (com.ricardo.ai-biology-prs,
# whose ai-biology/tools/update_bio_prs.sh now just runs this).
set -e -o pipefail
HERE=${0:A:h:h}; BIO=~/dev/hubs/ai-biology; PHYS=~/dev/hubs/ai-physics
GH=/Users/ricardo/dev/.bin/gh; export GITHUB_TOKEN=$($GH auth token)
push() {  # repo-dir github-name files...
  local d=$1 name=$2; shift 2
  cd $d
  if git diff --quiet -- "$@"; then echo "$(date '+%F %T') $name: no change"; return 0; fi
  git add -- "$@"
  git -c user.name="Ricardo Pinho" -c user.email="rpinho@users.noreply.github.com" commit -q -m "PRs: refresh status ($(grep -o '^[0-9]* PRs to [0-9]* repositor[a-z]*: [^.]*' README.md | head -1))"
  git -c credential.helper= -c credential.helper="!$GH auth git-credential" push -q https://github.com/rpinho/$name.git HEAD:main
  echo "$(date '+%F %T') $name: pushed"
}
for d in $HERE $BIO $PHYS; do git -C $d pull -q --ff-only; done
python3 $HERE/tools/render_prs.py --bio-readme $BIO/README.md --physics-readme $PHYS/README.md
push $HERE fixing-research-software README.md tools/prs.tsv
push $BIO ai-biology README.md
push $PHYS ai-physics README.md
