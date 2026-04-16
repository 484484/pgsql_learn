# SQL语法
## DDL,DML,DQL,DCL,TCL
### DDL（Data Definition Language，数据定义语言）：用于创建、修改、删除数据库对象（如表、视图、索引等）。
- **作用**：定义、修改或删除数据库对象（如表、索引、视图等）
- **主要命令**：`CREATE`、`ALTER`、`DROP`、`TRUNCATE`、`RENAME`
- **示例**：
  ```sql
  CREATE TABLE users (id INT, name VARCHAR(50));
  ALTER TABLE users ADD age INT;
  DROP TABLE users;
  RENAME TABLE users TO users_new;
  ```
### DML（Data Manipulation Language，数据操作语言）：用于对数据库中的数据进行增删改查操作。
- **作用**：对表中的数据进行增、删、改操作

- **主要命令**：INSERT、UPDATE、DELETE
`RENAME`
- **示例**：
    ```sql
    INSERT INTO users (id, name) VALUES (1, '张三');
    UPDATE users SET name = '李四' WHERE id = 1;
    DELETE FROM users WHERE id = 1;
    ```
### DQL（Data Query Language，数据查询语言）：用于查询数据库中的数据。
- **作用**：从数据库中检索数据
- **主要命令**：SELECT
- **示例**：
    ```sql
    SELECT * FROM users WHERE id = 1;
    ```
### DCL（Data Control Language，数据控制语言）：用于控制数据库的访问权限和安全。
- **作用**：管理数据库的用户权限和安全设置
- **主要命令**：GRANT、REVOKE
- **示例**：
    ```sql
    GRANT SELECT ON users TO user1;
    REVOKE ALL ON users FROM user2;
    ```
### TCL（Transaction Control Language，事务控制语言）：用于管理数据库事务。
- **作用**：控制数据库事务的开始、提交、回滚等操作
- **主要命令**：BEGIN、COMMIT、ROLLBACK
- **示例**：
    ```sql
    BEGIN;
    UPDATE users SET name = '王五' WHERE id = 1;
    SAVEPOINT sp1;
    DELETE FROM users WHERE id = 2;
    ROLLBACK TO sp1;   -- 回滚到保存点
    COMMIT;
    ```
## INTEGER,NUMERIC,BIGINT,SMALLINT
* INTEGER：标准整数，通常占用 4 字节，取值范围约为 -2.1×10⁹ 到 2.1×10⁹（有符号）。
* NUMERIC（或 DECIMAL）：精确数值类型，用于存储带小数的数字（如货币金额）。可以指定总位数（精度）和小数位数（刻度），例如 NUMERIC(10,2) 表示总共 10 位数字，其中 2 位是小数。它不会出现浮点舍入误差，但存储和计算开销比整数类型大。
* BIGINT：大整数类型，占用 8 字节，取值范围约为 -9.223372036854775808 到 9.223372036854775807（有符号）。
* SMALLINT：小整数类型，占用 2 字节，取值范围约为 -32768 到 32767（有符号）。
## VARCHAR,CHAR,TEXT
### VARCHAR：可变长度字符串类型，用于存储长度可变的字符串（如用户名、密码等）。可以指定最大长度，例如 VARCHAR(50) 表示最大长度为 50 个字符。
### CHAR：固定长度字符串类型，用于存储固定长度的字符串（如邮政编码、手机号等）。可以指定固定长度，例如 CHAR(10) 表示固定长度为 10 个字符。
### TEXT：大文本类型，用于存储长度非常大的字符串（如长文章、评论等）。它占用的存储空间是字符串长度的 2 倍（因为每个字符占用 2 个字节），但可以存储任意长度的字符串。
## ENUM
### ENUM：枚举类型，用于存储固定值的集合（如性别、状态等）。可以指定多个值，例如 ENUM('男', '女', '未知') 表示性别只能是 '男'、'女' 或 '未知'。
## DATE,TIMESTAMP,TIME
### DATE：日期类型，用于存储日期（如 2023-01-01）。占用 4 字节，存储格式为 YYYY-MM-DD。
### TIMESTAMP：日期戳类型，用于存储日期和时间（如 2023-01-01 12:00:00）。占用 8 字节，存储格式为 YYYY-MM-DD HH:MM:SS。
### TIME：时间类型，用于存储时间（如 12:00:00）。占用 3 字节，存储格式为 HH:MM:SS。
### 示例
```sql
SELECT NOW();
```
## BOOLEAN
### BOOLEAN：布尔类型，用于存储 true 或 false 两个值。占用 1 字节，存储值为 1 或 0。
### 示例
```sql
SELECT TRUE;
SELECT FALSE;
``` 
## JSON
### JSON：JSON 类型，用于存储 JSON 格式的字符串。占用 2 字节，存储格式为 JSON 字符串。
### 示例
```sql
SELECT '{"name": "张三", "age": 30}';
```
