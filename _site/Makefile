TARGETS: build serve git 

all:
	${TARGETS}

serve:
	jekyll serve&

build:
	jekyll build

deploy: 
	rsync -avhz _site/* youri@netbsd-news.me:~/netbsd-news/; 

git:
	git add -A;
	git commit -m 'update';
	git push;
