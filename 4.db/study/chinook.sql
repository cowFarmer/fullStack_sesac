-- 1. non_usa_customers.sql: Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
-- 
SELECT FirstName||" "|| LastName AS "Full Name", CustomerId, Country FROM customers WHERE country != "USA";

-- 2. brazil_customers.sql: Provide a query only showing the Customers from Brazil.
-- 
SELECT * FROM customers WHERE Country = "Brazil";

-- 3. brazil_customers_invoices.sql: Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
-- 브라질 고객의 송장 출력 쿼리; 결과; 고객 전체 이름, 송장 ID, 송장 날짜, 청구 국가
SELECT FirstName||" "||LastName AS "Full Name", InvoiceId, InvoiceDate, BillingCountry
FROM customers
INNER JOIN invoices
ON customers.CustomerId == invoices.CustomerId
WHERE Country = "Brazil";


-- 4. sales_agents.sql: Provide a query showing only the Employees who are Sales Agents.
-- sales agent를 뽑아달라
SELECT * 
FROM employees
WHERE Title = "Sales Support Agent";

-- 5. unique_invoice_countries.sql: Provide a query showing a unique/distinct list of billing countries from the Invoice table.
-- invoice에서 billing country 보여달라
SELECT DISTINCT BillingCountry
FROM invoices;

-- 6. sales_agent_invoices.sql: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
-- invoices의 InvoiceId와 연관이 있는 employees의 sales agent의 full name을 포함해서 보여줘라
SELECT employees.FirstName||" "||employees.LastName AS "Full Name", invoices.*
FROM invoices
JOIN customers ON invoices.CustomerId = customers.CustomerId
JOIN employees ON customers.SupportRepId = employees.EmployeeId
WHERE employees.Title = "Sales Support Agent";

-- 7. invoice_totals.sql: Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
-- 모든 송장과 고객에 대해 송장 총액, 고객 이름, 나라, 담당자 이름을 뽑아줘
SELECT SUM(invoice_items.UnitPrice) AS "Total Price",
    customers.FirstName||" "||customers.LastName AS "Customer Full Name",
    customers.Country,
    employees.FirstName||" "||employees.LastName AS "Employee Full Name"
FROM invoices
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
JOIN customers ON invoices.InvoiceId = customers.CustomerId
JOIN employees ON customers.SupportRepId = employees.EmployeeId
GROUP BY customers.CustomerId;

-- 8. total_invoices_{year}.sql: How many Invoices were there in 2009 and 2011?
-- 2009 ~ 2011년 사이의 invoices count
SELECT COUNT(InvoiceId) AS "Total Invoices"
FROM invoices
WHERE DATE(InvoiceDate) >= DATE("2009-01-01") AND DATE(InvoiceDate) <= DATE("2011-12-31");


-- 9. total_sales_{year}.sql: What are the respective total sales for each of those years?
-- 년도별 판매 금액 출력하기
SELECT strftime("%Y", invoices.InvoiceDate), SUM(invoice_items.UnitPrice) AS "total_salse"
FROM invoices
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY strftime("%Y", invoices.InvoiceDate);

-- 10. invoice_37_line_item_count.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
-- 11. line_items_per_invoice.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
-- 12. line_item_track.sql: Provide a query that includes the purchased track name with each invoice line item.
-- 13. line_item_track_artist.sql: Provide a query that includes the purchased track name AND artist name with each invoice line item.
-- 14. country_invoices.sql: Provide a query that shows the # of invoices per country. HINT: GROUP BY
-- 15. playlists_track_count.sql: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.
-- 16. tracks_no_id.sql: Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.
-- 17. invoices_line_item_count.sql: Provide a query that shows all Invoices but includes the # of invoice line items.
-- 18. sales_agent_total_sales.sql: Provide a query that shows total sales made by each sales agent.
-- 19. top_2009_agent.sql: Which sales agent made the most in sales in 2009?
--     Hint: Use the MAX function on a subquery. top_agent.sql: Which sales agent made the most in sales over all?
-- 21. sales_agent_customer_count.sql: Provide a query that shows the count of customers assigned to each sales agent.
-- 22. sales_per_country.sql: Provide a query that shows the total sales per country.
-- 23. top_country.sql: Which country's customers spent the most?
-- 24. top_2013_track.sql: Provide a query that shows the most purchased track of 2013.
-- 25. top_5_tracks.sql: Provide a query that shows the top 5 most purchased songs.
-- 26. top_3_artists.sql: Provide a query that shows the top 3 best selling artists.
-- 27. top_media_type.sql: Provide a query that shows the most purchased Media Type.