#/bin/bash
FILE_NAME=SegarraCarlos_CV.tex
PDF_NAME=SegarraCarlos_CV.pdf
if [ -d CV ];
then
    rm -rf CV
fi
git clone git@github.com:csegarragonz/CV.git
#docker run --rm -v $(pwd)/CV/short-w-images:/short -w /short schickling/latex pdflatex $FILE_NAME
docker run --rm -v $(pwd)/CV/short-w-images:/short -w /short moss/xelatex xelatex $FILE_NAME
mv ./CV/short-w-images/$PDF_NAME assets/
rm -rf CV
