-- 특정 사용자가 구매한 주문 내역 가져오기
SELECT
    user.Id,
    user.Name,
    ordered.Id,
    ordered.OrderAt,
    item.Name
FROM user
JOIN ordered ON user.Id = ordered.UserId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
-- WHERE user.Id = "0a497257-2b1a-4836-940f-7b95db952e61";
ORDER BY user.Name ASC;

-- 특정 사용자가 주문한 상점명과 상품명 출럭하기
SELECT
    user.Id,
    user.Name,
    store.Id,
    store.Name,
    item.Id,
    item.Name
FROM user
JOIN ordered ON user.Id = ordered.UserId
JOIN store ON ordered.StoreId = store.Id
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
WHERE user.Id = "0a497257-2b1a-4836-940f-7b95db952e61";

-- 특정 사용자가 구매한 주문 내역의 상품명 모두 가져오기
SELECT DISTINCT
    user.Id,
    user.Name,
    item.Id,
    item.Name
FROM user
JOIN ordered ON user.Id = ordered.UserId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
WHERE user.Id = "0a497257-2b1a-4836-940f-7b95db952e61";

-- 특정 사용자가 구매한 매출액의 합산을 구하기
SELECT
    user.Id,
    SUM(item.UnitPrice)
FROM user
JOIN ordered ON user.Id = ordered.UserId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
-- WHERE user.Id = "0a497257-2b1a-4836-940f-7b95db952e61"
GROUP BY user.Id;

-- 상점별 월간 매출액 구하기
SELECT
    store.Id,
    store.Name,
    strftime("%Y-%m", ordered.OrderAt),
    SUM(item.UnitPrice)
FROM store
JOIN ordered ON store.Id = ordered.StoreId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderItem.ItemId = item.Id
GROUP BY store.Id, strftime("%Y-%m", ordered.OrderAt)
ORDER BY store.Name;

-- 금일 주문된 상품 정보 보기
SELECT
    store.Id,
    store.Name,
    ordered.OrderAt,
    item.Name
FROM ordered
JOIN store ON ordered.StoreId = store.Id
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
WHERE date('now') = strftime("%Y-%m-%d", ordered.OrderAt);

-- 제품별 판매 금액 구하기
SELECT
    item.Name,
    SUM(item.UnitPrice)
FROM ordered
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
GROUP BY item.Id;

-- 매출 top5 매장 구하기
SELECT
    store.Id,
    store.Name,
    SUM(item.UnitPrice) AS "total sales"
FROM store
JOIN ordered ON store.Id = ordered.StoreId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
GROUP BY store.Id
ORDER BY "total sales" DESC
LIMIT 5;

-- 매장의 top5 판매 수 구하기
SELECT
    store.Id,
    store.Name,
    COUNT(item.UnitPrice) AS "count total sales"
FROM store
JOIN ordered ON store.Id = ordered.StoreId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
GROUP BY store.Id
ORDER BY "count total sales" DESC
LIMIT 5;

-- 특정 매장의 top5 판매 제품 구하기
SELECT
    store.Id,
    store.Name,
    item.Id,
    item.Name,
    COUNT(item.Id)
FROM store
JOIN ordered ON store.Id = ordered.StoreId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
WHERE store.Id = "69568455-8856-4a61-b7a0-8e2061fd06cd"
GROUP BY item.Id
ORDER BY COUNT(item.Id) DESC
LIMIT 5;

-- 특정 매장의 매출 top5 제품 구하기
SELECT
    store.Id,
    store.Name,
    item.Id,
    item.Name,
    SUM(item.UnitPrice) AS "Total Sales Per Item"
FROM store
JOIN ordered ON store.Id = ordered.StoreId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
WHERE store.Id = "69568455-8856-4a61-b7a0-8e2061fd06cd"
GROUP BY item.Id
ORDER BY "Total Sales Per Item" DESC
LIMIT 5;

-- 특정 매장의 top5 사용자 구하기
SELECT
    store.Id,
    store.Name,
    item.Id,
    item.Name,
    user.Id,
    user.Name,
    COUNT(item.Id) AS "Count user Per Store"
FROM store
JOIN ordered ON store.Id = ordered.StoreId
JOIN user ON ordered.UserId = user.Id
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
WHERE store.Id = "69568455-8856-4a61-b7a0-8e2061fd06cd"
GROUP BY item.Id
ORDER BY "Count user Per Store" DESC
LIMIT 5;

-- 매출액 합산이 가장 높은 사용자 10명을 구하고 매출액을 구하기
SELECT 
    user.Id,
    user.Name,
    SUM(CAST(item.UnitPrice AS INTEGER)) AS TotalRevenue
FROM user
JOIN ordered ON user.Id = ordered.UserId
JOIN orderitem ON ordered.Id = orderitem.OrderId
JOIN item ON orderitem.ItemId = item.Id
GROUP BY user.Id, user.Name
ORDER BY TotalRevenue DESC
LIMIT 10;


-- 전체 매장의 총 매출액 구하기
-- 전체 매장의 총 매출액 월별로 구하기
-- 년도별 특정 매장의 매출액 구하기
-- 년도별 전체 매장의 매출액 구하기
