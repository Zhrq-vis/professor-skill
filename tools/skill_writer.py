#!/usr/bin/env python3
"""赛博教授 Skill 文件管理器

管理教授 Skill 的文件操作：列出、初始化目录、生成组合 SKILL.md、完整创建。

Usage:
    python3 skill_writer.py --action <list|init|create|combine> --base-dir <path> [--slug <slug>]
"""

import argparse
import json
import os
import sys
from datetime import datetime


def list_skills(base_dir: str):
    """列出所有已生成的赛博教授 Skill"""
    if not os.path.isdir(base_dir):
        print("还没有创建任何赛博教授 Skill。")
        return

    skills = []
    for slug in sorted(os.listdir(base_dir)):
        meta_path = os.path.join(base_dir, slug, 'meta.json')
        if os.path.exists(meta_path):
            with open(meta_path, 'r', encoding='utf-8') as f:
                meta = json.load(f)
            skills.append({
                'slug': slug,
                'name': meta.get('name', slug),
                'field': meta.get('field', ''),
                'focus': meta.get('focus', ''),
                'institution': meta.get('institution', ''),
                'version': meta.get('version', '?'),
                'updated_at': meta.get('updated_at', '?'),
            })

    if not skills:
        print("还没有创建任何赛博教授 Skill。")
        return

    print(f"共 {len(skills)} 个赛博教授 Skill：\n")
    for s in skills:
        desc = ' · '.join([p for p in [s['field'], s['focus'], s['institution']] if p])
        print(f"  /{s['slug']}  —  {s['name']}")
        if desc:
            print(f"    {desc}")
        print(f"    版本 {s['version']} · 更新于 {s['updated_at'][:10] if len(s['updated_at']) > 10 else s['updated_at']}")
        print()


def init_skill(base_dir: str, slug: str):
    """初始化 Skill 目录结构"""
    skill_dir = os.path.join(base_dir, slug)
    dirs = [
        os.path.join(skill_dir, 'versions'),
        os.path.join(skill_dir, 'sources', 'papers'),
        os.path.join(skill_dir, 'sources', 'lectures'),
        os.path.join(skill_dir, 'sources', 'profiles'),
        os.path.join(skill_dir, 'student_context'),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print(f"已初始化目录：{skill_dir}")


def combine_skill(base_dir: str, slug: str):
    """合并 research_memory + advising_persona + playbook 生成完整 SKILL.md"""
    skill_dir = os.path.join(base_dir, slug)
    meta_path = os.path.join(skill_dir, 'meta.json')
    research_path = os.path.join(skill_dir, 'research_memory.md')
    persona_path = os.path.join(skill_dir, 'advising_persona.md')
    playbook_path = os.path.join(skill_dir, 'playbook.md')
    skill_path = os.path.join(skill_dir, 'SKILL.md')

    if not os.path.exists(meta_path):
        print(f"错误：meta.json 不存在 {meta_path}", file=sys.stderr)
        sys.exit(1)

    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.load(f)

    def read_optional(path: str) -> str:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return ''

    research_content = read_optional(research_path)
    persona_content = read_optional(persona_path)
    playbook_content = read_optional(playbook_path)

    name = meta.get('name', slug)
    field = meta.get('field', '')
    focus = meta.get('focus', '')
    institution = meta.get('institution', '')
    roles = ', '.join(meta.get('roles', []))

    desc_parts = [p for p in [field, focus, institution] if p]
    description = f"{name}，{'，'.join(desc_parts)}" if desc_parts else name

    skill_md = f"""---
name: {slug}
description: {description}
user-invocable: true
---

# {name}

{description}

主要角色：{roles or 'research advisor'}

---

## PART A：Research Memory

{research_content}

---

## PART B：Advising Persona

{persona_content}

---

## PART C：Action Playbook

{playbook_content}

---

## 运行规则

1. 你是“{name}风格的科研导师”，不是空泛聊天助手。
2. 先判断问题定义是否成立，再判断方法是否合理，再判断实验是否足够。
3. 对于来自教授材料的内容，按材料优先；对于通用科研方法论补充，要明确是一般建议。
4. 若用户要求最新文献，而当前上下文没有提供检索结果，则明确提醒用户补充，不要假装看过。
5. 输出优先给：下一步动作、实验清单、写作修改项、代码骨架建议。
6. 允许切换模式：导师模式 / 审稿人模式 / 代码教练模式 / 答辩官模式。
7. 遇到证据不足时，说“材料不足”而不是编造。
"""

    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(skill_md)

    print(f"已生成 {skill_path}")


def create_skill(base_dir: str, slug: str, meta: dict, research_content: str, persona_content: str, playbook_content: str):
    """完整创建 Skill"""
    init_skill(base_dir, slug)

    skill_dir = os.path.join(base_dir, slug)
    now = datetime.now().isoformat()
    meta['slug'] = slug
    meta.setdefault('created_at', now)
    meta['updated_at'] = now
    meta['version'] = 'v1'
    meta.setdefault('roles', ['advisor'])

    with open(os.path.join(skill_dir, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    with open(os.path.join(skill_dir, 'research_memory.md'), 'w', encoding='utf-8') as f:
        f.write(research_content)

    with open(os.path.join(skill_dir, 'advising_persona.md'), 'w', encoding='utf-8') as f:
        f.write(persona_content)

    with open(os.path.join(skill_dir, 'playbook.md'), 'w', encoding='utf-8') as f:
        f.write(playbook_content)

    combine_skill(base_dir, slug)
    print(f"✅ Skill 已创建：{skill_dir}")
    print(f"   触发词：/{slug}")


def main():
    parser = argparse.ArgumentParser(description='赛博教授 Skill 文件管理器')
    parser.add_argument('--action', required=True, choices=['list', 'init', 'create', 'combine'])
    parser.add_argument('--base-dir', default='./.claude/skills', help='基础目录（默认：./.claude/skills）')
    parser.add_argument('--slug', help='教授代号')
    parser.add_argument('--meta', help='meta.json 文件路径（create 时使用）')
    parser.add_argument('--research', help='research_memory.md 内容文件路径（create 时使用）')
    parser.add_argument('--persona', help='advising_persona.md 内容文件路径（create 时使用）')
    parser.add_argument('--playbook', help='playbook.md 内容文件路径（create 时使用）')

    args = parser.parse_args()

    if args.action == 'list':
        list_skills(args.base_dir)
    elif args.action == 'init':
        if not args.slug:
            print("错误：init 需要 --slug 参数", file=sys.stderr)
            sys.exit(1)
        init_skill(args.base_dir, args.slug)
    elif args.action == 'create':
        if not args.slug:
            print("错误：create 需要 --slug 参数", file=sys.stderr)
            sys.exit(1)
        meta = {}
        if args.meta:
            with open(args.meta, 'r', encoding='utf-8') as f:
                meta = json.load(f)
        research_content = ''
        if args.research:
            with open(args.research, 'r', encoding='utf-8') as f:
                research_content = f.read()
        persona_content = ''
        if args.persona:
            with open(args.persona, 'r', encoding='utf-8') as f:
                persona_content = f.read()
        playbook_content = ''
        if args.playbook:
            with open(args.playbook, 'r', encoding='utf-8') as f:
                playbook_content = f.read()
        create_skill(args.base_dir, args.slug, meta, research_content, persona_content, playbook_content)
    elif args.action == 'combine':
        if not args.slug:
            print("错误：combine 需要 --slug 参数", file=sys.stderr)
            sys.exit(1)
        combine_skill(args.base_dir, args.slug)


if __name__ == '__main__':
    main()
