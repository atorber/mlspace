# 需要安装 Lance 格式的 Python SDK: pip install pylance
import lance
import pyarrow as pa

if not hasattr(lance, "write_dataset"):
    raise ImportError(
        "当前 'lance' 模块没有 write_dataset。请安装 pylance： pip install pylance"
    )

# 创建数据
table = pa.table({
    "id": [1, 2, 3],
    "vector": [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]],
    "image_bytes": [b"...", b"...", b"..."] 
})

# 写入 Lance 格式（overwrite 便于重复运行 demo）
dataset = lance.write_dataset(table, "./my_dataset.lance", mode="overwrite")

# 读取数据
dataset = lance.dataset("./my_dataset.lance")
table = dataset.to_table()
print("全表:", table)

# 使用 SQL 谓词查询：filter 支持 SQL 表达式，支持列投影、limit、offset
# 只查 id >= 2 的行，只取 id 和 vector 列
filtered = dataset.to_table(
    columns=["id", "vector"],
    filter="id >= 2",
    limit=10,
)
print("SQL 查询 (id >= 2, 列: id, vector):", filtered)

# 单条件
one_row = dataset.to_table(filter="id = 1", columns=["id"])
print("id = 1:", one_row)

# 执行向量搜索 (如果已建立索引)
# results = dataset.search([0.1, 0.2]).limit(10).to_table()