#!/usr/bin/env python3
"""赛博教授版本存档与回滚管理器"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime

CORE_FILES = ['research_memory.md', 'advising_persona.md', 'playbook.md', 'SKILL.md', 'meta.json']


def backup(base_dir: str, slug: str):
    skill_dir = os.path.join(base_dir, slug)
    versions_dir = os.path.join(skill_dir, 'versions')
    meta_path = os.path.join(skill_dir, 'meta.json')

    if not os.path.exists(meta_path):
        print("错误：meta.json 不存在", file=sys.stderr)
        sys.exit(1)

    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.load(f)

    current_version = meta.get('version', 'v0')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{current_version}_{timestamp}"
    backup_dir = os.path.join(versions_dir, backup_name)
    os.makedirs(backup_dir, exist_ok=True)

    for fname in CORE_FILES:
        src = os.path.join(skill_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(backup_dir, fname))

    print(f"已备份版本 {backup_name} 到 {backup_dir}")
    return backup_name


def rollback(base_dir: str, slug: str, version: str):
    skill_dir = os.path.join(base_dir, slug)
    versions_dir = os.path.join(skill_dir, 'versions')

    target_dir = None
    for vname in os.listdir(versions_dir):
        if vname.startswith(version) or vname == version:
            target_dir = os.path.join(versions_dir, vname)
            break

    if not target_dir or not os.path.isdir(target_dir):
        print(f"错误：找不到版本 {version}", file=sys.stderr)
        list_versions(base_dir, slug)
        sys.exit(1)

    backup(base_dir, slug)

    for fname in CORE_FILES:
        src = os.path.join(target_dir, fname)
        dst = os.path.join(skill_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)

    print(f"已回滚到版本 {version}")


def list_versions(base_dir: str, slug: str):
    versions_dir = os.path.join(base_dir, slug, 'versions')
    if not os.path.isdir(versions_dir):
        print("没有历史版本。")
        return

    versions = sorted(os.listdir(versions_dir), reverse=True)
    if not versions:
        print("没有历史版本。")
        return

    print(f"历史版本（共 {len(versions)} 个）：\n")
    for v in versions:
        print(f"  {v}")


def main():
    parser = argparse.ArgumentParser(description='赛博教授版本管理器')
    parser.add_argument('--action', required=True, choices=['backup', 'rollback', 'list'])
    parser.add_argument('--slug', required=True, help='教授代号')
    parser.add_argument('--base-dir', default='./.claude/skills', help='基础目录（默认：./.claude/skills）')
    parser.add_argument('--version', help='回滚目标版本')
    args = parser.parse_args()

    if args.action == 'backup':
        backup(args.base_dir, args.slug)
    elif args.action == 'rollback':
        if not args.version:
            print("错误：rollback 需要 --version 参数", file=sys.stderr)
            sys.exit(1)
        rollback(args.base_dir, args.slug, args.version)
    elif args.action == 'list':
        list_versions(args.base_dir, args.slug)


if __name__ == '__main__':
    main()
