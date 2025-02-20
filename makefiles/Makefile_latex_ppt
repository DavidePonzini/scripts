add_remote:
	git remote add template git@github.com:DavidePonzini/dav_theme.git

rebase:
	git fetch template
	git rebase -X theirs template/main
	git pull --allow-unrelated-histories
	git push
