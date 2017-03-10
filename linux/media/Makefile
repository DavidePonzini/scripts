urls=url
out=out
names=names

no_lines=20

path=/scripts

regex='s/.*Episode-//'

1-prepare-urls: clear
	cat $(urls) | \
		sed $(regex) | sed 's/\?.*//' | \
		while read line; do \
			echo $$line.mp4; \
		done \
	> $(out)

2-split:
	split -d -l $(no_lines) $(urls) $(urls)_
	split -d -l $(no_lines) $(names) $(names)_

3-get-urls:
	false
	for url in `ls $(urls)_`; do \
		$(path)/kissanime-get-url $$url; \
	done \
	> $(out)

4-download:
	$(path)/mwget.py $(out)

clear:
	rm -f $(out)
