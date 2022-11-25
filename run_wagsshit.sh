echo "Running WagsShit"
python -u /app/manage.py migrate
python -u /app/manage.py runserver 0.0.0.0:8000
echo "WagsShit Ready!"