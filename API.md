Документация к API

SWAGGER - http://locahost:port/

Список активных опросов
```sh
GET https/localhost:port/user/active_quizzes/
```
Список пройденных опросов **РАБОТАЕТ ТОЛЬКО ДЛЯ АДМИНА**
```sh
GET https/localhost:port/user/active_quizzes/
```
Ответить на вопрос. У всех вопросов есть id, у всех ответов есть id, который передаётся в качетсве **choice_id** 
```sh
PATCH https/localhost:port/user/questions/{question_id}/vote/
REQUEST:
{
  "choice_id": {answer_id}
}
RESPONSE:
{
  "Voted"
}
```

QuestionViewSet. Методы: GET, POST, PUT, DELETE
Cписок всех вопросов
```sh
GET https/localhost:port/question/
```
Просмотр вопроса по id
```sh
GET https/localhost:port/question/{id}/
```
Cоздание нового вопроса
```sh
POST https/localhost:port/question/
```
Редактирование вопроса по id
```sh
PUT/PATCH https/localhost:port/question/{id}/
```
Удаление вопроса по id
```sh
DELETE https/localhost:port/question/{id}/
```

QuizViewSet. Методы: GET, POST, PUT, DELETE
Cписок всех опросов
```sh
GET https/localhost:port/quiz/
```
Просмотр опроса по id
```sh
GET https/localhost:port/quiz/{id}/
```

Cоздание нового опроса
```sh
POST https/localhost:port/quiz/
```
Редактирование опроса по id
```sh
PUT/PATCH https/localhost:port/quiz/{id}/
```
Удаление опроса по id
```sh
DELETE https/localhost:port/quiz/{id}/
```
