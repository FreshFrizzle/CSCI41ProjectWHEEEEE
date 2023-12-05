
INSERT INTO CUSTOMER (Customer_ID, Last_Name, First_Name, Middle_Initial, Birth_date, Gender) VALUES (1231, Mejilla, EJ, G, 2002-07-16, Male)

INSERT INTO CUSTOMER (Customer_ID, Last_Name, First_Name, Middle_Initial, Birth_date, Gender) VALUES (1001, Smith, John, A, 2003-01-01, Male)

INSERT INTO CUSTOMER (Customer_ID, Last_Name, First_Name, Middle_Initial, Birth_date, Gender) VALUES (0903, Grace, Mary, B, 2003-03-04, Female)

INSERT INTO STATION (Station_ID, Location) VALUES (WES, Cauldron Pool)

INSERT INTO STATION (Station_ID, Location) VALUES (AEN, Allies’ Enclave)

INSERT INTO STATION (Station_ID, Location) VALUES (AAA, Aslan’s Camp)

INSERT INTO TICKET (Ticket_Num, Customer_ID, Date) VALUES (1223, SELECT Customer_ID FROM CUSTOMER WHERE Customer_ID ==’1231’;,2023 -12-05 )

