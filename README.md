### "CodexZone" 

## Описание

CodexZone - Api для интернет магазин книг для разботчиков и не только.

<br> 
<hr>
<details>
<summary><strong>Документация</strong></summary>
<br>
<h3>db/models/books.py</h3>
<p>
Код определяет несколько моделей ORM SQLAlchemy для приложения по продаже книг.
Таблицы user_roles, book_tags и favorite_books определяются с помощью функции Table() из библиотеки SQLAlchemy.
Модель Book имеет атрибуты id, name, author, description, price, category и is_available. Она имеет отношение многие к одному с моделью User через внешний ключ owner_id, а также отношения многие ко многим с моделью Tag через атрибут tags, который определяется с помощью параметра secondary.</p>
<p>Модель Tag имеет атрибуты id и name. Она имеет отношение многие ко многим с моделью Book через атрибут books, который определяется с помощью параметра secondary.</p>
<p>Модель User имеет атрибуты id, username, email, hashed_password, is_active, is_superuser и is_verified. Она имеет отношение один ко многим с моделью Book через атрибут books, отношение многие ко многим с моделью Book через атрибут favorite_books, который определяется с помощью параметра secondary, и отношения один ко многим с моделями Cart и UserRole через атрибуты carts и roles соответственно.</p>
<p>Модель UserRole имеет атрибуты id, role_name и user_id. Она имеет отношение многие к одному с моделью User через внешний ключ user_id.</p>
<p>Модель Cart имеет атрибуты id, owner_id и total_price. Она имеет отношение один ко многим с моделью CartItem через атрибут items и отношение многие к одному с моделью User через внешний ключ owner_id.</p>
<p>Модель CartItem имеет атрибуты id, cart_id, book_id, quantity и price. Она имеет отношение многие к одному с моделью Cart через внешний ключ cart_id и отношение многие к одному с моделью Book через внешний ключ book_id.</p>
</details>