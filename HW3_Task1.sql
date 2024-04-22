--Отримати всі завдання певного користувача:
SELECT * FROM tasks WHERE user_id = 100;

--Вибрати завдання за певним статусом:
SELECT * 
FROM tasks 
WHERE status_id = (
    SELECT id 
    FROM status 
    WHERE name = 'new'
);

--Оновити статус конкретного завдання:
UPDATE tasks 
SET status_id = (
    SELECT id 
    FROM status 
    WHERE name = 'in progress'
) 
WHERE id = 1050;

--Отримати список користувачів, які не мають жодного завдання:
select *
from users u 
where id not in 
	(select t.user_id
	from tasks t);

--Додати нове завдання для конкретного користувача:
INSERT INTO tasks (user_id, title, description, status_id)
VALUES (
    (SELECT id FROM users WHERE id = 100), 
    'Завдання',
    'Опис завдання', 
    (SELECT id FROM status WHERE name = 'new')
);

--Отримати всі завдання, які ще не завершено:
SELECT * 
FROM tasks t
WHERE t.status_id != (
    SELECT id 
    FROM status 
    WHERE name = 'completed'
);

--Видалити конкретне завдання:
delete  from tasks 
WHERE id = '3002'

--Знайти користувачів з певною електронною поштою:
select * from users u 
where email = 'volodymyra59@example.net';

--Оновити ім'я користувача:
UPDATE users
SET fullname = 'Нове Ім''я'
WHERE id = '1';

--Отримати кількість завдань для кожного статусу:
select 
	count (t.status_id) as total_tasks,
	s.name
	from tasks t
	join status s on t.status_id = s.id
	group by s."name" ; 

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти:
select *
from tasks t
join users u on t.user_id = u.id 
where u.email like '%@example.com';

--Отримати список завдань, що не мають опису:
SELECT *
FROM tasks t
WHERE t.description = '';

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress':
select * 
from tasks t 
INNER JOIN status s on t.status_id =s.id 
where s."name" = 'in progress';

--Отримати користувачів та кількість їхніх завдань:
select u.fullname, count(t.id)
from tasks t 
left join users u on t.user_id = u.id
group by u.fullname;







