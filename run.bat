docker build -t langchain-test1 .
docker run -it -v "%CD%\models:/usr/src/app/models" -v "%CD%\data:/usr/src/app/data" -p 5000:5000 --rm --name my-running-app -w /usr/src/app langchain-test1
pause