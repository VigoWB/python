# API - REST - HTTP podstawy

https://flask.palletsprojects.com/en/latest/tutorial/

https://aviary.pl/python-flask/

https://oig.edu.pl/blog/prosty-flask-jak-stworzyc-swoja-pierwsza-aplikacje-webowa/

## HTTP Verbs - czasowniki - akcje w ramach HTTP

- GET - pobiera dane ze wskazanego zasobu, sam w sobie poza adresem nie niesie żadnych informacji
- POST - wysyla dane na wskazany zasób, poza adresem powinien posiadac również body
- PUT - zamienia dane we wzkazanym zasobie, powinien posiadać body
- PATCH - częściowa aktualizacja danych na wskazanym zasobie, powinien posiadac body
- DELETE - kasuje wszkazany zasób, nie powinien nieść żadnych dodatkowych informacji
- HEAD - naglowki - żadko używane
- OPTIONS - żąda opisu komunikacji żadko używane

### Przykłady

`GET /lists` - pobiera wszystkie listy (nie wskazano id)

`GET /lists/2` - pobiera liste o id 2

`POST /lists` - tworzy nowa liste

```json
{
	"name": "Nowa lista"
}
```

`PUT /lists/2` - aktualizuje liste o id 2

```json
{
	"name": "Nowa lista ze zmieniona nazwa"
}
```

`DELTE /lists/2` - kasuje liste o id 2