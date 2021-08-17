# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
    FROM Address right join Person
    on Person.PersonId = Address.PersonId;