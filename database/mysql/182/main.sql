# Write your MySQL query statement below
SELECT Email from
(
    SELECT Email, count(Email) as num
    from Person
    group by Email
) as statistic
WHERE num > 1;