message=$1
cd /var/www/zyni/answer/
echo ${message}
git log --since=${message} --pretty=format:"%ad,%s"
git log --since=${message} --pretty=format:"%ad,%s" >/var/www/zyni/gitlab_answer_gitlog.log
