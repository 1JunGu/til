import os
import frontmatter # type: ignore
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def slugify(text: str) -> str:
    """简单的 slugify 函数，用于创建锚点链接"""
    return text.lower().replace(" ", "-").replace("/", "-")

def get_til_entries():
    """扫描 tils 目录，解析 markdown 文件"""
    entries_by_topic = defaultdict(list)
    if not TIL_DIR.exists() or not TIL_DIR.is_dir():
        print(f"Warning: TIL directory '{TIL_DIR}' not found.")
        return entries_by_topic

    for md_file in TIL_DIR.rglob("*.md"):
        try:
            # 确定主题：主题是 tils 目录下的第一级子目录名
            # 例如: tils/Python/file.md -> topic is "Python"
            #       tils/Git/Basics/another.md -> topic is "Git" (assuming only one level for topic)
            relative_path_parts = md_file.relative_to(TIL_DIR).parts
            if not relative_path_parts or len(relative_path_parts) < 2: # 必须在子目录中
                print(f"Warning: Skipping '{md_file.name}' as it's not in a topic subdirectory under '{TIL_DIR}'.\
                        expected format: tils/TopicName/file.md")
                continue
            topic_name = relative_path_parts[0]
            post = frontmatter.load(md_file)
            metadata = post.metadata

            # 确保必要字段存在
            if not all(k in metadata for k in ["title", "modify"]):
                print(f"Warning: Skipping '{md_file.name}' due to missing some frontmatter fields (title, modify).")
                continue

            # 确保 modify 是一个有效的日期字符串，方便排序
            try:
                # 尝试解析日期以验证格式，但我们主要用字符串进行排序
                datetime.strptime(str(metadata['modify']), "%Y-%m-%d %H:%M")
            except ValueError:
                print(f"Warning: Skipping '{md_file.name}' due to invalid 'modify' date format. Expected YYYY-MM-DD.")
                continue

            entries_by_topic[topic_name].append({
                "title": metadata['title'],
                "modify": str(metadata['modify']), # 确保是字符串
                "filename": md_file.name, # 用于生成文件链接
                "path": md_file # 获取相对路径
            })
        except Exception as e:
            print(f"Error parsing '{md_file.name}': {e}")

    # 对每个主题下的条目按更新日期降序排序
    for topic in entries_by_topic:
        entries_by_topic[topic].sort(key=lambda x: x['modify'], reverse=True)

    return entries_by_topic

def generate_readme_content(entries_by_topic: defaultdict[str, list]) -> str:
    """生成 README.md 的内容"""
    content = ["# Today I Learned (TIL)\n\nMy personal collection of TILs.\n"]

    if not entries_by_topic:
        content.append("No TILs found yet. Add some Markdown files to the `tils/` directory!")
        return "\n".join(content)

    # 1. Table of Contents (TOC) - 按主题字母顺序
    content.append("## Table of Contents\n")
    sorted_topics = sorted(entries_by_topic.keys())
    for topic in sorted_topics:
        content.append(f"- [{topic}](#{slugify(topic)})")
    content.append("\n---")

    # 2. Content per topic
    for topic in sorted_topics:
        content.append(f"\n## {topic}\n")
        for entry in entries_by_topic[topic]:
            # 假设 TILs 目录在仓库根目录
            file_link = f"{REPO_URL}/blob/main/{entry['path']}".replace("\\", "/")
            # 或者使用相对链接（如果 GitHub Actions 在同一个仓库中运行）
            # file_link = str(entry['path']).replace("\\", "/")
            content.append(f"- [{entry['title']}]({file_link}) - _{entry['modify']}_")
        content.append("") # 添加空行

    return "\n".join(content)

def main():
    entries = get_til_entries()
    print("Starting README generation...")
    readme_content = generate_readme_content(entries)
    try:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"Successfully updated '{README_FILE}'")
    except IOError as e:
        print(f"Error writing to '{README_FILE}': {e}")

if __name__ == "__main__":
    # 设置工作目录为脚本所在目录的父目录 (项目根目录)
    # 这样无论从哪里运行脚本，相对路径都能正确工作
    project_root = Path(__file__).resolve().parent
    os.chdir(project_root)
    print(f"Current working directory: {Path.cwd()}")
    TIL_DIR = Path("tils")
    README_FILE = Path("README.md")
    REPO_URL = "https://github.com/1JunGu/til" # 替换成你的仓库 URL
    print(f"Looking for TILs in: {TIL_DIR.resolve()}")
    main()
