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
-- 
SELECT c.FirstName||" "||c.LastName AS "Customer Name",
    i.InvoiceId, i.InvoiceDate, i.BillingCountry
FROM customers c LEFT JOIN invoices i ON i.CustomerId = c.CustomerId
WHERE Country = "Brazil";

-- 4. sales_agents.sql: Provide a query showing only the Employees who are Sales Agents.
-- sales agent를 뽑아달라
SELECT * 
FROM employees
WHERE Title = "Sales Support Agent";
-- 
SELECT *
FROM employees 
WHERE title LIKE "Sales%";

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
-- 2009, 2011년의 invoices count
SELECT strftime("%Y", InvoiceDate), COUNT(InvoiceId) AS "Total Invoices"
FROM invoices
WHERE DATE(InvoiceDate) >= DATE("2009-01-01") AND DATE(InvoiceDate) <= DATE("2011-12-31")
GROUP BY strftime("%Y", InvoiceDate);
-- 
SELECT COUNT(i.InvoiceId) AS CountOfInvoices,
    strftime("%Y", i.InvoiceDate) AS InvoiceYear
FROM invoices i
WHERE InvoiceYear IN ("2009", "2011") 
GROUP BY InvoiceYear;

-- 9. total_sales_{year}.sql: What are the respective total sales for each of those years?
-- 년도별 판매 금액 출력하기
SELECT strftime("%Y", invoices.InvoiceDate), SUM(invoice_items.UnitPrice) AS "Total Sales Per Year"
FROM invoices
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY strftime("%Y", invoices.InvoiceDate);

-- 10. invoice_37_line_item_count.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
-- invoice_items의 InvoiceLineId를 보고 InvoiceId 37의 품목 수를 카운트해라
SELECT invoices.InvoiceId,
    COUNT(*) AS "Count Per Invoice Id"
FROM invoice_items
JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
WHERE invoices.InvoiceId = 37;

-- SELECT invoices.InvoiceId,
--     COUNT(*) AS "Count Per Invoice Id"
-- FROM invoice_items
-- JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
-- GROUP BY invoices.InvoiceId;

-- 11. line_items_per_invoice.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
-- invoice_items의 InvoiceLineId를 보고 각 invoice에 대해 카운트하기
SELECT invoices.InvoiceId,
    COUNT(*) AS "Count Per Invoice"
FROM invoice_items
JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
GROUP BY invoices.InvoiceId;
-- 
SELECT invoice_items.InvoiceId,
    COUNT(*) AS "Count Per Invoice"
FROM invoice_items
JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
GROUP BY invoices.InvoiceId;

-- 12. line_item_track.sql: Provide a query that includes the purchased track name with each invoice line item.
-- 각 invoice별 tracks의 Name 출력
SELECT InvoiceId,
    tracks.Name
FROM invoice_items
JOIN tracks ON invoice_items.TrackId = tracks.TrackId;

-- 13. line_item_track_artist.sql: Provide a query that includes the purchased track name AND artist name with each invoice line item.
-- 각 invoice별 track name, artist name 출력
-- 궁금한 점 invoice id를 굳이 invoices를 참조해야 하나?
SELECT 
    invoice_items.InvoiceId,
    tracks.Name,
    artists.Name
FROM invoice_items
JOIN tracks ON invoice_items.TrackId = tracks.TrackId
JOIN albums ON tracks.AlbumId = albums.AlbumId
JOIN artists ON albums.ArtistId = artists.ArtistId;

-- 14. country_invoices.sql: Provide a query that shows the # of invoices per country. HINT: GROUP BY
-- 국가별 invoice 보여주기
-- GROUP BY가 아닌 ORDER BY를 써야하는거 아닌가?
SELECT InvoiceId,
    customers.Country
FROM invoices
JOIN customers ON invoices.CustomerId = customers.CustomerId
GROUP BY customers.Country;

-- SELECT InvoiceId,
--     customers.Country
-- FROM invoices
-- JOIN customers ON invoices.CustomerId = customers.CustomerId
-- ORDER BY InvoiceId;

-- 15. playlists_track_count.sql: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.
-- 각 track의 플레이리스트별 total number를 보여달라, 플레이 리스트 이름 꼭 들어가야함
SELECT tracks.TrackId,
    playlists.Name,
    COUNT(playlists.Name)
FROM tracks
JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
GROUP BY playlists.Name
ORDER BY tracks.TrackId ASC;

-- 16. tracks_no_id.sql: Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.
-- 모든 track에 대해 album name, media type, genre를 보여줘라 단 IDs는 보여주지마
SELECT
    albums.Title,
    media_types.Name,
    genres.Name
FROM tracks
JOIN albums ON tracks.AlbumId = albums.AlbumId
JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
JOIN genres ON tracks.GenreId = genres.GenreId;

-- 17. invoices_line_item_count.sql: Provide a query that shows all Invoices but includes the # of invoice line items.
SELECT invoices.InvoiceId, COUNT(*)
FROM invoices
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY invoice_items.InvoiceId;

-- 18. sales_agent_total_sales.sql: Provide a query that shows total sales made by each sales agent.
-- 각 sales agent별 total sales 보여줘
SELECT
    employees.EmployeeId,
    employees.FirstName||" "||employees.LastName AS "Employees Name",
    employees.Title,
    SUM(invoice_items.UnitPrice)
FROM employees
JOIN customers ON employees.EmployeeId = customers.SupportRepId
JOIN invoices ON customers.CustomerId = invoices.CustomerId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY employees.EmployeeId;

-- 19. top_2009_agent.sql: Which sales agent made the most in sales in 2009?
--     Hint: Use the MAX function on a subquery. top_agent.sql: Which sales agent made the most in sales over all?
-- 2009년에 누가 가장 실적이 좋니?
SELECT EmployeesName, MAX(TotalSale)
    FROM (
        SELECT employees.EmployeeId,
            employees.FirstName||" "||employees.LastName AS EmployeesName,
            SUM(invoice_items.UnitPrice) AS TotalSale
        FROM employees
        JOIN customers ON employees.EmployeeId = customers.SupportRepId
        JOIN invoices ON customers.CustomerId = invoices.CustomerId
        JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        WHERE DATE(invoices.InvoiceDate) >= DATE("2009-01-01") AND DATE(invoices.InvoiceDate) <= DATE("2009-12-31")
        GROUP BY employees.EmployeeId
        );

-- 21. sales_agent_customer_count.sql: Provide a query that shows the count of customers assigned to each sales agent.
-- 22. sales_per_country.sql: Provide a query that shows the total sales per country.
-- 23. top_country.sql: Which country's customers spent the most?


-- 24. top_2013_track.sql: Provide a query that shows the most purchased track of 2013.
-- 25. top_5_tracks.sql: Provide a query that shows the top 5 most purchased songs.
-- 26. top_3_artists.sql: Provide a query that shows the top 3 best selling artists.
-- 27. top_media_type.sql: Provide a query that shows the most purchased Media Type.