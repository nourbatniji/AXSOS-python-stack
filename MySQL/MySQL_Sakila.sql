USE sakila;

SELECT city.city_id, customer.first_name, 
customer.last_name , customer.email , 
address.address , city.city, country.country
FROM country
LEFT JOIN city
ON country.country_id = city.country_id
LEFT JOIN address
ON city.city_id = address.city_id
LEFT JOIN customer 
ON address.address_id = customer.address_id
WHERE city.city_id = 312;

SELECT film.film_id, film.title,
 film.description, film.release_year,
 film.rating, film.special_features, 
 category.name
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

SELECT actor.actor_id, CONCAT(first_name, ' ',last_name) AS actor_name, film.title, film.description, film.release_year
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM store
LEFT JOIN customer
ON store.store_id = customer.store_id
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON address.city_id = city.city_id
WHERE store.store_id = 1
AND city.city_id IN (1, 42, 312, 459);

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 15
AND film.rating = "G"
AND film.special_features LIKE "%behind the scenes";


SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ',actor.last_name) AS actor_name
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;


SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99
AND category.name = "Drama";



SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, 
	CONCAT(first_name, ' ',last_name) AS actor_name
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE CONCAT(first_name, ' ',last_name) = "SANDRA KILMER";



