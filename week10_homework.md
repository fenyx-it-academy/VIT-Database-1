    < ------------------------------------------------- 1. ÖDEV ------------------------------------------------- > 
Table: Employees
| EmployeeID | Name           | Salary     | HireDate   | DepartmentID  | PositionID |
|------------|----------------|------------|------------|---------------|------------|
| 1          | John Smith     | $80,000    | 2015-01-15 | 10            | 100        |
| 2          | Jane Doe       | $95,000    | 2014-06-23 | 20            | 200        |
| 3          | Mike Johnson   | $75,000    | 2016-03-10 | 10            | 300        |
| 4          | Lisa Anderson  | $90,000    | 2013-09-05 | 30            | 400        |


Table: Department

| DepartmentID | Department      |
|--------------|-----------------|
| 10           | Engineering     |
| 20           | Sales           |
| 30           | Human Resources |

Table: Position

| PositionID   | Position        |
|--------------|-----------------|
| 100          | Software        |
| 200          | Sales Manager   |
| 300          | Hardware        |
| 400          | HR Manager      |


    < ------------------------------------------------- 2. ÖDEV ------------------------------------------------- >         


                                                     Uyeler
                                                 ID integer(10)
                                                 isim varchar(255)
                                                 Uyelik_tarihi date
                                                 Alınan_kitaplar.ID integer(10)
                                                            _|_
                             Kategori                        |                          Kitaplar    
                         ID integer(10)     ---|-------------|-------------------->  ID integer(10)
                         isim varchar(255)                   |                       isim varchar(255)
                                                             |       ------------|-- Kategori.ID integer(10)
                                                             |       |               Yazarlar.ID integer(10)
                                                             |       |                       /|\
                         Yazarlar    ---|--------------------|-------|------------------------|
                     ID integer(10)                          |       |
                     isim varchar(255)                      \|/     \|/
                                                         Alınan_kitaplar
                                                     ID integer(10)
                                                     Uyeler.ID integer(10)
                                                     Kitaplar.ID integer(10)
                                                     Alınma_tarihi date



    < ------------------------------------------------- 3. ÖDEV ------------------------------------------------- >
SORULAR:

1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?

    SELECT name,Population FROM country WHERE Population > 100000000

2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?

    SELECT name FROM country WHERE name like '%land'

3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?

    SELECT name, Population FROM city WHERE Population > 500000 AND Population < 100000000

4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.

    SELECT name FROM country WHERE Region LIKE '%Europe'

5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.

    SELECT name,SurfaceArea FROM country ORDER BY SurfaceArea DESC

6- Hollanda’nin (NLD) tum sehirlerini bulunuz.

    SELECT name FROM city WHERE CountryCode = 'NLD'

7- Amsterdam’in nufusu kactir?

    SELECT name,Population FROM city WHERE name = 'Amsterdam'

8- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?

    SELECT name,SurfaceArea FROM country WHERE Continent = 'Africa' ORDER BY SurfaceArea DESC LIMIT 1

9- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?

    SELECT name, SurfaceArea FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 10

10- Yuzolcumu en kucuk olan ulkeyi bulunuz.

    SELECT name, SurfaceArea FROM country ORDER BY SurfaceArea LIMIT 1

11- En kalabalik 10 sehri bulunuz.

    SELECT name,Population FROM city ORDER BY population DESC LIMIT 10

12- Dunyanin nufusunu hesaplayiniz.

    SELECT SUM(population) as DunyaNufus FROM country

13- Asya kitasinda kac ulke bulunmaktadir?

    SELECT count(Continent) FROM country WHERE Continent = 'Asia'

14- En cok ulke bulunan kita hangisidir?

    SELECT Continent ,count(continent) FROM country GROUP by Continent ORDER by count(Continent) DESC limit 1

15- Dunya'nin en dusuk nufuslu ulkesi hangisidir?

    SELECT name, min(population) FROM country 

16- En dusuk nufuslu 10 sehir hangisidir?

    SELECT name, Population FROM city ORDER BY Population limit 10

17- Birden fazla resmi dili (IsOfficial -> T) olan ulkeler hangileridir?

    SELECT country.name, country.code, count(countrylanguage.IsOfficial) as 'Resmi dil sayısı' 
    FROM country 
    INNER JOIN countrylanguage 
    ON country.Code = countrylanguage.CountryCode 
    WHERE countrylanguage.IsOfficial = 'T' 
    GROUP by countrylanguage.CountryCode 
    HAVING count(countrylanguage.isofficial) >= 2

18- Ingilizcenin %90'dan fazla kullanildigi ulkeler hangileridir? (Yalnizca ulke kodlari yeterli, join islemi yapmaniza gerek yoktur)

    SELECT CountryCode FROM countrylanguage WHERE Language = 'English' AND Percentage > 90 

19- Hem Ingilizce'nin hem de Fransizca'nin resmi dil (IsOfficial -> T) oldugu ulkeler hangileridir?

    SELECT country.name
    FROM countrylanguage
    INNER JOIN country 
    ON countrylanguage.CountryCode = country.Code
    WHERE countrylanguage.Language = 'English' AND countrylanguage.IsOfficial = 'T' OR countrylanguage.Language = 'French' AND countrylanguage.IsOfficial = 'T'
    GROUP BY countrylanguage.CountryCode
    HAVING count(countrylanguage.CountryCode) >= 2


20- Ortalama yasam suresi (LifeExpectancy) en yuksek 10 ulke hangileridir?

    SELECT name FROM country ORDER BY LifeExpectancy DESC LIMIT 10

