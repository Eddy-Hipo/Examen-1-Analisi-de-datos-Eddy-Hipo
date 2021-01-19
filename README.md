# Examen-1-Analisi-de-datos-Eddy-Hipo

Se trabajó con juegos como datos estraidos de los diferentes lugares.

1.- En el script 1 tomamos datos de Twitter y se los almacena en CouchDB.
En donde la librería utilizada es tweepy y se necesitan credenciales para poder tomar los datos de Twitter, y en las siguientes lineas se toman los datos y se guardan en CouchDB, la base de datos es examen, y se guardaran datos de biedojuegos.

2.- En el script 2 se toman datos de una pagina web de blizzard con webscrapping, y se los guarda en MongoDB Compass.
En las primeras lineas se recopila los datos que se necesitan.
Desde la linea 46 en adelante se procede a enlazarce con la MongoDB Compass y guardar los datos en la base "examen", en la colección llamada "juegos".

3.- En el script 3 se toman los datos de una página de facebooj y se los almacena en mongoDB.
De la línea 1 a la 24 se toman los datos de facebook y se los almacena en una variable.
De la línea 35 en adelante se procede a guardar en la base de datos "examen", pero en una colleción diferente llamada "facebook".

4.- En el Script 4 se toman los datos de SQLite y se ls almacena en mongoDB.
De la línea 1 a la 8 se toman los datos de SQLite y se los transforman a json.
Desde la línea 9 se conecta a la MongoDB y se guarda en la base de datos "examen" en una nueva colleción llamada "SQLiteamongo"

5.- En el script 5 se toma los datos de CouchDB y se los almacena en MongoDB.
Las primeras lineas muestran las conexiones a las dos bases.
Desde la linea 34 son los comandos para guardar los datos en MongoDB en la base "examen", en la colleción "mongoacouch".

6.- En el Script 6 se toman los datos de mongoDb y se los almacna en couchDB.
Desde la primera linea hasta la 49, se realiza la conexión a las respectivas bases de datos.
De la línea 51 en adelante se realiza el proceso para guardar los datoss que se extrajeron de la base de datos "examen" recopilando todas las colecciones existente, y guardandolos en la base da datos llamada "mongocouchexamen" en couchDB.

7.- En el script 7 se toma los datos de CouchDB y se los almacena en MongoDB Atlas.
Las primeras lineas muestran las conexiones a las dos bases.
En la línea 25 se toma el link que nos proporciona nuestro MongoDB Atlas para poder acceder a él 
Desde la linea 34 son los comandos para guardar los datos en MongoDB en la base "examen", en la colleción "couchamongoatlas".

8.- En en script 8 se realiza la conexión desde mongoDB compass a Mongo DB Atlas.
Las primeras lineas muestran las conexiones a las dos bases de Mongo.
De mongoDB Compass se toma toda la base de datos "examen" con todas sus coleciones.
Desde a línea 34 es elcódigo para guardar en mongoDB Atlas en la base "examen", en la colección "mongoamongoatlas".

9 y 10 .- En el script 9 y 10, se toman los datos desde MongoDB Atlas, de la base "examen" y la coleccón "couchamongoatlas".
Desde la línea 19 a 23 toma los datos de mongo y los ponen en un arreglo para posteriormente en ultima línea transdormarlo a un csv.