1. Install deps:
```
pip install -r requirements.txt
```
2. Run docker:
```
docker run -p 6379:6379 redis
```
3. Castom command (add 5 object)
```
python3 manage.py create_blog_object
```
 4. Run Django web server
```
python3 manage.py create_blog_object
```
5. Enter the URL
```
/blog/(blog id - (1,2,3,4...))
```