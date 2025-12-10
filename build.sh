# make migrations
python3 manage.py makemigrations
python3 manage.py migrate

# collectstatic
python3 manage.py collectstatic --noinput --clear

echo "Build script completed"