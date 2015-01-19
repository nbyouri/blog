TARGETS: build serve git 

all:
	${TARGETS}

serve-local:
	jekyll serve&

build:
	jekyll build

serve: 
	rsync -avhz _site/* root@saveosx.org:/usr/local/www/saveosx/blog/; 

git:
	git add -A;
	git commit -m 'update';
	git push;
