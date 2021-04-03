#/bin/bash
THIS_DIR=$(dirname -- $(readlink -f -- $0))
PROJ_ROOT="${THIS_DIR}/.."

pushd ${PROJ_ROOT} >> /dev/null

# Repo's CV information
FILE_NAME=SegarraCarlos_CV.tex
PDF_NAME=SegarraCarlos_CV.pdf
REPO_NAME=csg-projects/csg-cv
REPO_DIR=short-w-images

# Create temporary CV folder
if [ -d CV ];
then
    rm -rf CV
fi

# Clone repository
git clone git@github.com:${CSG_PROJECTS}.git

docker run --rm \
    -v $(pwd)/CV/short-w-images:/short \
    -w /short \
    moss/xelatex xelatex $FILE_NAME
mv ./CV/short-w-images/$PDF_NAME assets/
rm -rf CV

pushd >> /dev/null

