
  git init
git add .
git commit -m 'Cool'
git push -u url
git push heroku master
heroku ps:scale web=1
echo %date%,%time%