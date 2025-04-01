CREATE SCHEMA dannys_diner;
SET search_path = dannys_diner;
 
CREATE TABLE sales (
  customer_id VARCHAR(1),
  order_date DATE,
  product_id INTEGER
);
 
INSERT INTO sales
  (customer_id, order_date, product_id)
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
 
CREATE TABLE menu (
  product_id INTEGER,
  product_name VARCHAR(5),
  price INTEGER
);
 
INSERT INTO menu
  (product_id, product_name, price)
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
  
 
CREATE TABLE members (
  customer_id VARCHAR(1),
  join_date DATE
);
 
INSERT INTO members
  (customer_id, join_date)
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');
  
-- Query 1 - What is the total amount each customer spent at the restaurant?
SELECT s.customer_id, SUM(m.price) AS total_amount
FROM sales s
LEFT JOIN menu m
ON s.product_id = m.product_id
GROUP BY s.customer_id;
 
-- Query 2 - How many days has each customer visited the restaurant?
SELECT customer_id, COUNT(order_date) AS no_of_visits
FROM sales
GROUP BY customer_id;
 
-- Query 3 - What was the first item from the menu purchased by each customer?
SELECT s.customer_id, m.product_name AS first_item
FROM sales s
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date = (SELECT MIN(s.order_date) FROM sales s)
GROUP BY s.customer_id, m.product_name;
 
-- Query 4 - What is the most purchased item on the menu and how many times was it purchased by all customers?
SELECT m.product_name, COUNT(s.product_id) AS purchase_count
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY purchase_count DESC
LIMIT 1;
 
-- Query 5 - Which item was the most popular for each customer?
SELECT s.customer_id, m.product_name, COUNT(s.product_id) AS most_popular
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id, m.product_name
HAVING COUNT(s.product_id) = (
	SELECT MAX(most_popular)
	FROM (
		SELECT COUNT(*) AS most_popular
	FROM sales
	WHERE customer_id = s.customer_id
    GROUP BY product_id
	) 
) ORDER BY s.customer;

-- Query 6 - Which item was purchased first by the customer after they became a member?
SELECT s.customer_id, u.product_name, s.order_date
FROM sales s
JOIN menu u ON s.product_id = u.product_id
JOIN members m ON m.customer_id = s.customer_id
WHERE s.order_date >= m.join_date
AND s.order_date = (
	SELECT MIN(s.order_date)
	FROM sales s 
	WHERE s.customer_id = m.customer_id
	AND s.order_date >= m.join_date)
ORDER BY s.customer_id;

-- Query 7 - Which item was purchased just before the customer became a member?
SELECT s.customer_id, u.product_name, s.order_date
FROM sales s
JOIN menu u ON s.product_id = u.product_id
JOIN members m ON m.customer_id = s.customer_id
WHERE s.order_date < m.join_date 
AND s.order_date = (
	SELECT MAX(s.order_date)
	FROM sales s
	WHERE s.customer_id = m.customer_id
	AND s.order_date < m.join_date)
ORDER BY s.customer_id;

-- Query 8 - What is the total items and amount spent for each member before they became a member?
SELECT s.customer_id, COUNT(s.product_id) AS total_items, SUM(u.price) AS amount
FROM sales s
JOIN menu u USING(product_id)
JOIN members m USING(customer_id)
WHERE s.order_date < m.join_date
GROUP BY s.customer_id
ORDER BY s.customer_id;

-- Query 9 - If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
SELECT s.customer_id, 
	SUM(
		CASE WHEN u.product_name = 'sushi' THEN u.price * 20 
		ELSE u.price * 10
		END
	) AS total_points
FROM sales s
JOIN menu u ON s.product_id = u.product_id
GROUP BY s.customer_id
ORDER BY s.customer_id;

--  Query 10 - In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
SELECT s.customer_id, 
	SUM(
		CASE 
			WHEN s.order_date BETWEEN m.join_date AND m.join_date + INTERVAL '6 days'
			THEN u.price * 2
		END
	) AS total_points
FROM sales s
JOIN menu u ON s.product_id = u.product_id
LEFT JOIN members m ON s.customer_id = m.customer_id
WHERE s.order_date <= '2021-01-31'
GROUP BY s.customer_id
ORDER BY s.customer_id
LIMIT 2;

-- Bonus ques 1
SELECT s.customer_id, s.order_date, u.product_name, u.price, 
	(CASE WHEN s.order_date >= m.join_date THEN 'Y' ELSE 'N'
	END
	) AS members
FROM sales s
JOIN menu u ON s.product_id = u.product_id
LEFT JOIN members m ON m.customer_id = s.customer_id
ORDER BY s.customer_id, s.order_date;

-- Bonus ques 2 
WITH CTE AS (SELECT s.customer_id, s.order_date, u.product_name, u.price, 
	(CASE WHEN s.order_date >= m.join_date THEN 'Y' ELSE 'N'
	END
	) AS members
FROM sales s
JOIN menu u ON s.product_id = u.product_id
LEFT JOIN members m ON m.customer_id = s.customer_id
ORDER BY s.customer_id, s.order_date)

SELECT *, (CASE WHEN cte.members = 'Y' 
		   THEN RANK() OVER(PARTITION BY customer_id, members ORDER BY order_date)
		   ELSE NULL
		   END) AS ranking
FROM CTE;