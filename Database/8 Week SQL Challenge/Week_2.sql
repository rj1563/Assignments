CREATE SCHEMA pizza_runner;
SET search_path = pizza_runner;

DROP TABLE IF EXISTS runners;
CREATE TABLE runners (
  "runner_id" INTEGER,
  "registration_date" DATE
);
INSERT INTO runners
  ("runner_id", "registration_date")
VALUES
  (1, '2021-01-01'),
  (2, '2021-01-03'),
  (3, '2021-01-08'),
  (4, '2021-01-15');


DROP TABLE IF EXISTS customer_orders;
CREATE TABLE customer_orders (
  "order_id" INTEGER,
  "customer_id" INTEGER,
  "pizza_id" INTEGER,
  "exclusions" VARCHAR(4),
  "extras" VARCHAR(4),
  "order_time" TIMESTAMP
);

INSERT INTO customer_orders
  ("order_id", "customer_id", "pizza_id", "exclusions", "extras", "order_time")
VALUES
  ('1', '101', '1', '', '', '2020-01-01 18:05:02'),
  ('2', '101', '1', '', '', '2020-01-01 19:00:52'),
  ('3', '102', '1', '', '', '2020-01-02 23:51:23'),
  ('3', '102', '2', '', NULL, '2020-01-02 23:51:23'),
  ('4', '103', '1', '4', '', '2020-01-04 13:23:46'),
  ('4', '103', '1', '4', '', '2020-01-04 13:23:46'),
  ('4', '103', '2', '4', '', '2020-01-04 13:23:46'),
  ('5', '104', '1', 'null', '1', '2020-01-08 21:00:29'),
  ('6', '101', '2', 'null', 'null', '2020-01-08 21:03:13'),
  ('7', '105', '2', 'null', '1', '2020-01-08 21:20:29'),
  ('8', '102', '1', 'null', 'null', '2020-01-09 23:54:33'),
  ('9', '103', '1', '4', '1, 5', '2020-01-10 11:22:59'),
  ('10', '104', '1', 'null', 'null', '2020-01-11 18:34:49'),
  ('10', '104', '1', '2, 6', '1, 4', '2020-01-11 18:34:49');


DROP TABLE IF EXISTS runner_orders;
CREATE TABLE runner_orders (
  "order_id" INTEGER,
  "runner_id" INTEGER,
  "pickup_time" VARCHAR(19),
  "distance" VARCHAR(7),
  "duration" VARCHAR(10),
  "cancellation" VARCHAR(23)
);

INSERT INTO runner_orders
  ("order_id", "runner_id", "pickup_time", "distance", "duration", "cancellation")
VALUES
  ('1', '1', '2020-01-01 18:15:34', '20km', '32 minutes', ''),
  ('2', '1', '2020-01-01 19:10:54', '20km', '27 minutes', ''),
  ('3', '1', '2020-01-03 00:12:37', '13.4km', '20 mins', NULL),
  ('4', '2', '2020-01-04 13:53:03', '23.4', '40', NULL),
  ('5', '3', '2020-01-08 21:10:57', '10', '15', NULL),
  ('6', '3', 'null', 'null', 'null', 'Restaurant Cancellation'),
  ('7', '2', '2020-01-08 21:30:45', '25km', '25mins', 'null'),
  ('8', '2', '2020-01-10 00:15:02', '23.4 km', '15 minute', 'null'),
  ('9', '2', 'null', 'null', 'null', 'Customer Cancellation'),
  ('10', '1', '2020-01-11 18:50:20', '10km', '10minutes', 'null');


DROP TABLE IF EXISTS pizza_names;
CREATE TABLE pizza_names (
  "pizza_id" INTEGER,
  "pizza_name" TEXT
);
INSERT INTO pizza_names
  ("pizza_id", "pizza_name")
VALUES
  (1, 'Meatlovers'),
  (2, 'Vegetarian');


DROP TABLE IF EXISTS pizza_recipes;
CREATE TABLE pizza_recipes (
  "pizza_id" INTEGER,
  "toppings" TEXT
);

INSERT INTO pizza_recipes
  ("pizza_id", "toppings")
VALUES
  (1, '1, 2, 3, 4, 5, 6, 8, 10'),
  (2, '4, 6, 7, 9, 11, 12');


DROP TABLE IF EXISTS pizza_toppings;
CREATE TABLE pizza_toppings (
  "topping_id" INTEGER,
  "topping_name" TEXT
);
INSERT INTO pizza_toppings
  ("topping_id", "topping_name")
VALUES
  (1, 'Bacon'),
  (2, 'BBQ Sauce'),
  (3, 'Beef'),
  (4, 'Cheese'),
  (5, 'Chicken'),
  (6, 'Mushrooms'),
  (7, 'Onions'),
  (8, 'Pepperoni'),
  (9, 'Peppers'),
  (10, 'Salami'),
  (11, 'Tomatoes'),
  (12, 'Tomato Sauce');

--Data Cleaning & Transformation
UPDATE customer_orders
SET exclusions = NULL WHERE exclusions = 'null' OR exclusions ='';

UPDATE customer_orders
SET extras = NULL WHERE extras = 'null' OR extras = 'NaN' OR extras ='';

UPDATE runner_orders
SET cancellation = NULL WHERE cancellation = 'null' OR cancellation = 'NaN' OR cancellation ='';

UPDATE runner_orders
SET pickup_time = NULL WHERE pickup_time = 'null';

UPDATE runner_orders
SET distance = NULL WHERE distance = 'null';

UPDATE runner_orders
SET distance = TRIM('km' from distance) WHERE distance LIKE '%km';

UPDATE runner_orders
SET duration = NULL WHERE duration = 'null';

UPDATE runner_orders
SET duration = TRIM('mins' from duration) WHERE duration LIKE '%mins';

UPDATE runner_orders
SET duration = TRIM('minute' from duration) WHERE duration LIKE '%minute';

UPDATE runner_orders
SET duration = TRIM('minutes' from duration) WHERE duration LIKE '%minutes';

UPDATE runner_orders
SET cancellation = NULL WHERE cancellation = 'null' OR cancellation ='' OR cancellation = 'NaN';

--A. PIZZA METRICS

--Query 1 How many pizzas were ordered?
SELECT COUNT(order_id) AS total_orders
FROM customer_orders;

--Query 2 How many unique customer orders were made?
SELECT COUNT(DISTINCT order_id) AS unique_customer
FROM customer_orders;

-- Query 3 How many successful orders were delivered by each runner?
SELECT runner_id, COUNT(order_id) AS successful_orders
FROM runner_orders WHERE distance IS NOT NULL
GROUP BY runner_id
ORDER BY runner_id;

-- Query 4 How many of each type of pizza was delivered?
SELECT c.pizza_id, COUNT (c.order_id) AS delivered
FROM customer_orders c
JOIN runner_orders r ON c.order_id=r.order_id
WHERE r.distance IS NOT NULL
GROUP BY c.pizza_id
ORDER BY c.pizza_id; 

--Query 5 How many Vegetarian and Meatlovers were ordered by each customer?
SELECT c.customer_id, p.pizza_name, COUNT(c.pizza_id) AS order_count
FROM customer_orders c
JOIN pizza_names p ON p.pizza_id = c.pizza_id
GROUP BY c.customer_id, pizza_name
ORDER BY c.customer_id;

-- Query 6 What was the maximum number of pizzas delivered in a single order?
WITH CTE AS(
	SELECT c.order_id, COUNT(c.pizza_id) AS max_pizzas
	FROM customer_orders c 
	JOIN runner_orders r ON c.order_id = r.order_id
	WHERE r.distance IS NOT NULL 
	GROUP BY c.order_id
)
SELECT order_id, max_pizzas
FROM cte 
WHERE max_pizzas = (SELECT MAX(max_pizzas) FROM cte)

-- Query 7 For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
SELECT c.customer_id, SUM(
		CASE WHEN c.exclusions IS NOT NULL OR c.extras IS NOT NULL 
		THEN 1
		ELSE 0
		END
		) AS atleast_1_change,
	   SUM(
		CASE WHEN c.exclusions IS NULL AND c.extras IS NULL 
		THEN 1
		ELSE 0
		END
		) AS no_change
FROM customer_orders c
JOIN runner_orders r ON c.order_id = r.order_id
WHERE r.distance IS NOT NULL 
GROUP BY c.customer_id
ORDER BY c.customer_id;

-- Query 8 How many pizzas were delivered that had both exclusions and extras?
SELECT SUM(
	CASE WHEN c.exclusions IS NOT NULL AND c.extras IS NOT NULL THEN 1
	ELSE 0
	END
	) AS altered_pizza
FROM customer_orders c
JOIN runner_orders r ON c.order_id = r.order_id
WHERE r.distance IS NOT NULL;

-- Query 9 What was the total volume of pizzas ordered for each hour of the day?
SELECT order_id, EXTRACT(HOUR FROM order_time) AS order_hour, COUNT(*) AS total_pizzas
FROM customer_orders
GROUP BY order_id, order_hour
ORDER BY order_id, order_hour;

-- Query 10 What was the volume of orders for each day of the week?
SELECT order_id, EXTRACT(DAY FROM order_time) AS order_date, COUNT(*) AS total_pizzas
FROM customer_orders
GROUP BY order_id, order_date
ORDER BY order_id, order_date;

-- B. RUNNER AND CUSTOMER EXPERIENCE

-- Query 1 How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)
SELECT TO_CHAR(registration_date, 'W') week_number, COUNT(runner_id)
FROM runners
GROUP BY week_number
ORDER BY week_number;

-- Query 2 What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pickup the order?
SELECT r.runner_id, AVG(EXTRACT(EPOCH FROM(CAST(r.pickup_time AS timestamp) - c.order_time))/60) AS avg_arrival_time
FROM customer_orders c
JOIN runner_orders r ON c.order_id = r.order_id
GROUP BY r.runner_id
ORDER BY r.runner_id;

-- Query 3 Is there any relationship between the number of pizzas and how long the order takes to prepare?
SELECT c.order_id, COUNT(c.pizza_id) AS no_of_pizzas, EXTRACT(MINUTE FROM (CAST(r.pickup_time AS timestamp) - c.order_time)) AS preparation_time
FROM customer_orders c 
JOIN runner_orders r ON c.order_id = r.order_id
WHERE pickup_time IS NOT NULL
GROUP BY c.order_id, preparation_time
ORDER BY c.order_id;

-- Query 4 What was the average distance travelled for each customer?
SELECT c.customer_id, ROUND(AVG(CAST(distance AS numeric)), 1) AS avg_distance
FROM customer_orders c
JOIN runner_orders r ON c.order_id = r.order_id
GROUP BY c.customer_id
ORDER BY c.customer_id;

-- Query 5 What was the difference between the longest and shortest delivery times for all orders?
SELECT MAX(CAST(duration AS numeric)) - MIN(CAST(duration AS numeric)) AS time_diff
FROM runner_orders;

-- Query 6 What was the average speed for each runner for each delivery and do you notice any trend for these values?
SELECT runner_id, order_id, ROUND(AVG(CAST(distance AS numeric) / CAST(duration AS numeric) * 60), 1) AS avg_speed
FROM runner_orders 
WHERE distance IS NOT NULL
GROUP BY runner_id, order_id
ORDER BY runner_id, order_id;

-- Query 7 What is the successful delivery percentage for each runner?
SELECT runner_id, COUNT(
						CASE WHEN distance IS NOT NULL THEN order_id
						END) *100 / (COUNT(order_id)) AS successful_delivery_percentage
FROM runner_orders
GROUP BY runner_id;

-- C. Ingredient Optimisation

-- Query 1 What are the standard ingredients for each pizza?
WITH CTE AS(
	SELECT pizza_id, UNNEST(string_to_array(toppings, ','))::integer AS topping_id
	FROM pizza_recipes
)

SELECT cte.pizza_id, topping_name
FROM CTE 
JOIN pizza_toppings USING(topping_id)
ORDER BY cte.pizza_id, topping_name;

-- Query 2 What was the most commonly added extra?
WITH CTE AS(
	SELECT pizza_id, UNNEST(string_to_array(extras, ','))::integer AS topping_id
	FROM customer_orders
)

SELECT cte.topping_id, topping_name AS most_common_extras, COUNT(cte.topping_id) AS max_count
FROM CTE 
JOIN pizza_toppings USING(topping_id)
GROUP BY cte.topping_id, topping_name
ORDER BY max_count DESC
LIMIT 1;

-- Query 3 What was the most common exclusion?
WITH CTE AS(
	SELECT pizza_id, UNNEST(string_to_array(exclusions, ','))::integer AS topping_id
	FROM customer_orders
)

SELECT cte.topping_id, topping_name AS most_common_extras, COUNT(cte.topping_id) AS max_count
FROM CTE 
JOIN pizza_toppings USING(topping_id)
GROUP BY cte.topping_id, topping_name
ORDER BY max_count DESC
LIMIT 1;

-- Query 4 Generate an order item for each record in the customers_orders table in the format of one of the following:
-- Meat Lovers
-- Meat Lovers - Exclude Beef
-- Meat Lovers - Extra Bacon
-- Meat Lovers - Exclude Cheese, Bacon - Extra Mushroom, Peppers

SELECT 
    co.order_id,
    pn.pizza_name || 
    CASE 
        WHEN co.exclusions IS NOT NULL THEN ' - Exclude ' || 
            string_agg(DISTINCT pt_excl.topping_name, ', ') 
        ELSE '' 
    END || 
    CASE 
        WHEN co.extras IS NOT NULL THEN 
            ' - Extra ' || string_agg(DISTINCT pt_extra.topping_name, ', ') 
        ELSE '' 
    END AS order_item
FROM customer_orders co
JOIN pizza_names pn ON co.pizza_id = pn.pizza_id
LEFT JOIN pizza_recipes pr ON co.pizza_id = pr.pizza_id
LEFT JOIN pizza_toppings pt ON pt.topping_id = ANY(string_to_array(pr.toppings, ',')::int[])
LEFT JOIN pizza_toppings pt_extra ON pt_extra.topping_id = ANY(string_to_array(co.extras, ',')::int[])
LEFT JOIN pizza_toppings pt_excl ON pt_excl.topping_id = ANY(string_to_array(co.exclusions, ',')::int[])
GROUP BY co.order_id, pn.pizza_name, co.exclusions, co.extras
ORDER BY co.order_id;

-- Query 5 Generate an alphabetically ordered comma separated ingredient list 
-- for each pizza order from the customer_orders table and add a 2x in front of any
-- relevant ingredients
-- For example: "Meat Lovers: 2xBacon, Beef, ... , Salami"

WITH cte AS (
    SELECT pizza_id, UNNEST(STRING_TO_ARRAY(toppings, ', '))::int AS topping_id
    FROM pizza_recipes
),
ingredients AS (
    SELECT co.order_id, co.pizza_id, 
           CASE 
               WHEN COUNT(pt.topping_name) > 1 THEN '2x ' || pt.topping_name 
               ELSE pt.topping_name 
           END AS ingredient_name
    FROM customer_orders co
    JOIN cte USING (pizza_id)
    JOIN pizza_toppings pt USING (topping_id)
    GROUP BY co.order_id, co.pizza_id, pt.topping_name
),
ordered_list AS (
    SELECT order_id, STRING_AGG(ingredient_name, ', ' ORDER BY ingredient_name) AS list
    FROM ingredients
    GROUP BY order_id
)
SELECT order_id, list
FROM ordered_list
ORDER BY order_id;

-- Query 6 What is the total quantity of each ingredient used in all delivered pizzas 
-- sorted by most frequent first?

WITH cte AS(
	SELECT pizza_id, UNNEST(string_to_array(toppings, ','))::integer AS ingredient_id
	FROM pizza_recipes
),
DeliveredPizzas AS(
	SELECT c.pizza_id 
	FROM customer_orders c
	JOIN runner_orders USING(order_id)
	WHERE distance IS NOT NULL
)

SELECT cte.ingredient_id, COUNT(*) AS total_quantity
FROM cte
JOIN DeliveredPizzas USING(pizza_id)
GROUP BY cte.ingredient_id
ORDER BY total_quantity DESC;

-- D. Pricing and Ratings

-- Query 1 If a Meat Lovers pizza costs $12 and Vegetarian costs $10 and there were no 
-- charges for changes - how much money has Pizza Runner made so far if there are no delivery fees?
SELECT SUM(
		CASE WHEN pizza_id = '1' THEN 12
		ELSE 10
		END
		) AS gain
FROM customer_orders 
JOIN runner_orders USING(order_id)
WHERE distance IS NOT NULL;

-- Query 2 What if there was an additional $1 charge for any pizza extras?
-- Add cheese is $1 extra
SELECT SUM(
	CASE WHEN pizza_id = '1' THEN 12
	ELSE 10
	END +
	(SELECT COUNT(*) FROM UNNEST(string_to_array(extras, ',')))
	) AS total_charge
FROM customer_orders 
JOIN runner_orders USING(order_id)
WHERE distance IS NOT NULL;

-- Query 3 The Pizza Runner team now wants to add an additional ratings system that 
-- allows customers to rate their runner, how would you design an additional table for 
-- this new dataset - generate a schema for this new table and insert your own data for 
-- ratings for each successful customer order between 1 to 5.
DROP TABLE IF EXISTS runner_ratings;
CREATE TABLE runner_ratings(
	"order_id" INTEGER,
	"runner_id" INTEGER,
	"rating" INTEGER CHECK (rating >= 1 AND rating <= 5)
);

INSERT INTO runner_ratings VALUES 
  (1, 1, 2),
  (2, 1, 3),
  (3, 1, 1),
  (4, 2, 2),
  (5, 3, 4),
  (6, 3, 3),
  (7, 2, 4),
  (8, 2, 5),
  (9, 2, 3),
  (10, 1, 5);

SELECT * FROM runner_ratings;

-- Query 4 Using your newly generated table - can you join all of the information 
-- together to form a table which has the following information for successful deliveries?
-- customer_id
-- order_id
-- runner_id
-- rating
-- order_time
-- pickup_time
-- Time between order and pickup
-- Delivery duration
-- Average speed
-- Total number of pizzas
SELECT c.customer_id, c.order_id, r.runner_id, rr.rating, c.order_time, r.pickup_time,
((CAST(pickup_time AS timestamp) - order_time)) AS time_between_order_and_pickup,
CAST(r.duration AS numeric), ROUND(AVG(CAST(distance AS numeric)/CAST(duration AS numeric))),
COUNT(pizza_id) AS total_pizzas
FROM customer_orders c 
JOIN runner_orders r USING(order_id)
JOIN runner_ratings rr USING(order_id)
WHERE r.distance IS NOT NULL
GROUP BY c.customer_id, c.order_id, r.runner_id, rr.rating, c.order_time, r.pickup_time, r.duration
ORDER BY c.customer_id, order_id, runner_id;

-- Query 5 If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost 
-- for extras and each runner is paid $0.30 per kilometre traveled - how much money does 
-- Pizza Runner have left over after these deliveries?
WITH CTE AS(
	SELECT SUM(
		CASE WHEN pizza_id = '1' THEN 12
		ELSE 10
		END
		) AS total_cost
FROM customer_orders 
JOIN runner_orders USING(order_id)
WHERE distance IS NOT NULL)

SELECT cte.total_cost - SUM(0.3 * CAST(distance AS numeric)) AS money_left
FROM cte, runner_orders
GROUP BY cte.total_cost;

-- Bonus Question

-- If Danny wants to expand his range of pizzas - how would this impact the existing 
-- data design? Write an INSERT statement to demonstrate what would happen if a new 
-- Supreme pizza with all the toppings was added to the Pizza Runner menu?
INSERT INTO pizza_names("pizza_id", "pizza_name") VALUES(3, 'Supreme');

INSERT INTO pizza_recipes("pizza_id", "toppings") VALUES(3, '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12');

SELECT * FROM pizza_names;
SELECT * FROM pizza_recipes;