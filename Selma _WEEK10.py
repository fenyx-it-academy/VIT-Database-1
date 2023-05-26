#cevap1
CREATE TABLE 'employees' (
 'id'   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 'name' TEXT,
 'date' INTEGER
 );
 CREATE TABLE 'department' (
 'id'   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 'department' TEXT,
 'position' TEXT,
 'salary' INTEGER
 )
 

#cevap3

#Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
SELECT * FROM country WHERE Population > 100000000

#Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
SELECT name from country Where name like land

# 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
SELECT * FROM city WHERE population BETWEEN 500000 AND 1000000

#Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
SELECT * FROM country WHERE continent="Europe"

#Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
SELECT * FROM country ORDER BY SurfaceArea DESC

#Hollanda’nin (NLD) tum sehirlerini bulunuz.
SELECT * FROM city WHERE CountryCode = "NLD" 

#Amsterdam’in nufusu kactir?
SELECT * FROM city WHERE population ="Amsterdam"

# Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
SELECT * FROM Continent 'Africa' CHECK WHERE country = "max SurfaceArea"

# Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
SELECT * FROM Continent 'Asia' CHECK WHERE SurfaceArea max 10 country

#Yuzolcumu en kucuk olan ulkeyi bulunuz.
SELECT * FROM country ORDER BY SurfaceArea ASC LIMIT 1


#En kalabalik 10 sehri bulunuz.
SELECT * FROM countries ORDER BY area ASC LIMIT 10


#Dunyanin nufusunu hesaplayiniz.
SELECT SUM(population) AS world_population FROM countries

#Asya kitasinda kac ulke bulunmaktadir?
SELECT COUNT * num_countries FROM countries WHERE continent = 'Asia'

#En cok ulke bulunan kita hangisidir?

SELECT continent, COUNT * num_countries FROM countries GROUP BY continent ORDER BY num_countries

#Dunya'nin en dusuk nufuslu ulkesi hangisidir?
SELECT country_name, population FROM countries ="min country"

#En dusuk nufuslu 10 sehir hangisidir?
SELECT city_name, population FROM cities ORDER BY population ASC LIMIT 10


#Birden fazla resmi dili (IsOfficial -> T) olan ulkeler hangileridir?
SELECT country_name FROM countries WHERE IsOfficial = 'T' GROUP BY country_name HAVING COUNT(*) > 1


# Ingilizcenin %90'dan fazla kullanildigi ulkeler hangileridir? 
SELECT country_name FROM countries WHERE (English_Percentage * 100) > 90


#Hem Ingilizce'nin hem de Fransizca'nin resmi dil (IsOfficial -> T) oldugu ulkeler hangileridir?
SELECT country_name FROM countries WHERE IsOfficial = 'T' AND Language IN ('English', 'French') GROUP BY country_name HAVING COUNT(DISTINCT Language) = 2

# Ortalama yasam suresi (LifeExpectancy) en yuksek 10 ulke hangileridir?
SELECT country_name, LifeExpectancy FROM countries ORDER BY LifeExpectancy DESC LIMIT 10
