import os
import ast
import hashlib

# 递归遍历目录，收集所有Python文件路径
def collect_py_files(root_dir):
    py_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith('.py'):
                py_files.append(os.path.join(dirpath, f))
    return py_files

# 解析文件，提取函数和类定义的名称及其代码哈希
def parse_defs(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source)
    defs = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            start_line = node.lineno - 1
            end_line = node.end_lineno if hasattr(node, 'end_lineno') else node.lineno
            code_lines = source.splitlines()[start_line:end_line]
            code_str = '\n'.join(code_lines).strip()
            code_hash = hashlib.md5(code_str.encode('utf-8')).hexdigest()
            defs.append({'name': node.name, 'type': type(node).__name__, 'hash': code_hash, 'file': file_path, 'start_line': start_line+1, 'end_line': end_line})
    return defs

# 主函数，检测重复定义

def detect_redundancies(root_dir):
    py_files = collect_py_files(root_dir)
    all_defs = []
    for f in py_files:
        try:
            defs = parse_defs(f)
            all_defs.extend(defs)
        except Exception as e:
            print(f"Failed to parse {f}: {e}")

    # 按名称和类型分组
    name_type_map = {}
    for d in all_defs:
        key = (d['name'], d['type'])
        if key not in name_type_map:
            name_type_map[key] = []
        name_type_map[key].append(d)

    # 查找同名同类型但代码不同的定义
    redundancies = []
    for key, defs in name_type_map.items():
        if len(defs) > 1:
            hashes = set(d['hash'] for d in defs)
            if len(hashes) > 1:
                redundancies.append({'name': key[0], 'type': key[1], 'instances': defs})

    return redundancies

if __name__ == '__main__':
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    redundancies = detect_redundancies(root)
    if redundancies:
        print("检测到可能的重复定义或多余代码:")
        for item in redundancies:
            print(f"\n名称: {item['name']} 类型: {item['type']}")
            for inst in item['instances']:
                print(f"  文件: {inst['file']} 行: {inst['start_line']}-{inst['end_line']}")
    else:
        print("未检测到明显的重复定义。")