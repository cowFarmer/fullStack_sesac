user.csv
Id,Name,Gender,Age,Birthdate,Address
CREATE TABLE user(
    "Id" TEXT,
    "Name" TEXT,
    "Gender" TEXT,
    "AGE" INTEGER,
    "Birthdate" TEXT,
    "Address" TEXT
);

store.csv
Id,Name,Type,Address
CREATE TABLE store(
    "Id" TEXT,
    "Name" TEXT,
    "Type" TEXT,
    "Address" TEXT
);

orderitem.csv
Id,OrderId,ItemId
CREATE TABLE orderitem(
    "Id" TEXT,
    "OrderId" TEXT,
    "ItemId" TEXT
);

order.csv
Id,OrderAt,StoreId,UserId
CREATE TABLE ordered(
    "Id" TEXT,
    "OrderAt" TEXT,
    "StoreId" TEXT,
    "UserId" TEXT
);


item.csv
Id,Name,Type,UnitPrice
CREATE TABLE item(
    "Id" TEXT,
    "Name" TEXT,
    "Type" TEXT,
    "UnitPrice" INTEGER
);

.mode csv
.import user.csv user
.import store.csv store
.import orderitem.csv orderitem
.import order.csv ordered
.import item.csv item

DELETE FROM user WHERE Id='Id';
DELETE FROM store WHERE Id='Id';
DELETE FROM orderitem WHERE Id='Id';
DELETE FROM order WHERE Id='Id';
DELETE FROM item WHERE Id='Id';

order.csv
Id,OrderAt,StoreId,UserId
CREATE TABLE ordered2(
    "Id" TEXT,
    "OrderAt" DATETIME,
    "StoreId" TEXT,
    "UserId" TEXT
);