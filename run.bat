docker build -t langchain-test1 .
docker run -it -v "%CD%\models:/usr/src/app/models" --rm --name my-running-app -w /usr/src/app langchain-test1
pause