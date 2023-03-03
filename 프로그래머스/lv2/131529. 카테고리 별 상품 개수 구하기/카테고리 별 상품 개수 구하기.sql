-- 코드를 입력하세요

select t1.category as CATEGORY,count(t1.category) as PRODUCTS
from (SELECT SUBSTRING(PRODUCT_CODE,1,2) as CATEGORY from PRODUCT) as t1
GROUP BY t1.category
order by t1.category