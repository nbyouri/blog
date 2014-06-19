TARGETS: build serve git 

all:
	${TARGETS}

build:
	jekyll build

serve: 
	scp _site/* root@saveosx.org:/usr/local/www/saveosx/blog/; 

git:
	git add -A;
	git commit -m 'update';
	git push;
