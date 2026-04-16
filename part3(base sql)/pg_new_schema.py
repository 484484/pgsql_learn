import psycopg2
from psycopg2 import sql

# 数据库连接配置（请根据实际情况修改）
DB_CONFIG = {
    "dbname": "pg_learn",
    "user": "postgres",
    "password": "****",
    "host": "localhost",
    "port": "5432"
}


def create_schema(schema_name: str) -> bool:
    """在 PostgreSQL 中创建新模式（如果不存在）"""
    conn = None
    try:
        # 建立连接
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True  # 自动提交，避免事务阻塞
        cursor = conn.cursor()

        # 使用 SQL 组合安全构建语句（模式名不能直接参数化）
        create_schema_query = sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(
            sql.Identifier(schema_name)
        )
        cursor.execute(create_schema_query)

        print(f"模式 '{schema_name}' 创建成功（或已存在）")
        return True

    except psycopg2.Error as e:
        print(f"数据库错误: {e}")
        return False
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # 要创建的模式名称
    new_schema = "new_schema"
    success = create_schema(new_schema)
    if not success:
        print("创建模式失败")