-- Write your query below

SELECT seller.seller_name
FROM seller
LEFT JOIN orders
    ON seller.seller_id = orders.seller_id
    AND orders.sale_date BETWEEN  '2020-01-01' AND '2020-12-31'
WHERE orders.order_id is NULL
ORDER BY seller.seller_name
