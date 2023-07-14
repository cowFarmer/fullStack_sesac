-- user.csv
CREATE TABLE user(
    "Id" TEXT,
    "Name" TEXT,
    "Gender" TEXT,
    "Age" INTEGER,
    "Birthdate" TEXT,
    "Address" TEXT
);

-- store.csv
CREATE TABLE store(
    "Id" TEXT,
    "Name" TEXT,
    "Type" TEXT,
    "Address" TEXT
);

-- orderitem.csv
CREATE TABLE orderitem(
    "Id" TEXT,
    "OrderId" TEXT,
    "ItemId" TEXT
);

-- order.csv
CREATE TABLE ordered(
    "Id" TEXT,
    "OrderAt" DATETIME,
    "StoreId" TEXT,
    "UserId" TEXT
);

-- item.csv
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
