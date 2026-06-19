USE world;


SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages
ON countries.code = languages.country_code
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;
USE world;


SELECT countries.name, COUNT(cities.id)
FROM countries
JOIN cities
ON countries.code = cities.country_code
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;


SELECT cities.name, cities.population, countries.id
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
WHERE countries.name = "Mexico" AND cities.population >= 500000
ORDER BY population DESC;


SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.code = languages.country_code
WHERE languages.percentage >= 89
ORDER BY languages.percentage DESC;


SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 
AND countries.population >=100000;


SELECT countries.name, countries.capital, countries.government_form, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
AND countries.capital >= 200
AND countries.life_expectancy >= 75;


SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population > 500000;


SELECT countries.region, COUNT(*) AS countries
FROM countries
GROUP BY countries.region



